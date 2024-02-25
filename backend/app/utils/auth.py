import jwt
from django.conf import settings
from app.models import Task
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework import exceptions
from django.contrib.auth.models import AnonymousUser

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        if isinstance(raw_token, bytes):
            raw_token = raw_token.decode('utf-8')

        try:
            payload = jwt.decode(raw_token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError as e:
            raise exceptions.AuthenticationFailed(f'Invalid token: {str(e)}')

        try:
            task_id = payload.get('id')
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            raise AuthenticationFailed('Task does not exist')
        except Exception as e:
            raise exceptions.AuthenticationFailed(f'Error retrieving task: {str(e)}')

        request.task_id = task_id
        user = AnonymousUser()
        user.is_active = True
        return (user, None)
