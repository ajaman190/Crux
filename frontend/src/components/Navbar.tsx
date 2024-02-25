import React from 'react';
import { useNavigate } from 'react-router-dom';

import logo from '../assets/icons/logo.svg';
import { Avatar, AvatarFallback } from './ui/avatar';

const Navbar: React.FC = () => {
  const navigate = useNavigate();

  return (
    <nav className="bg-white shadow-md">
      <div className="flex justify-between items-center py-2 max-w-screen-2xl mx-auto px-2">
        <button onClick={() => navigate('/')} className="flex items-center">
          <img src={logo} alt="Crux" className="h-8 w-8 mr-2"/>
          <span className="font-semibold text-gray-500 text-lg text-primary">Crux</span>
        </button>
        <Avatar className="mr-2 border">
          <AvatarFallback>PP</AvatarFallback>
        </Avatar>
      </div>
    </nav>
  );
};

export default Navbar;
