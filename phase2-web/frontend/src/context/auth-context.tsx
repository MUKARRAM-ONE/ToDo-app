'use client';

import React, { createContext, useContext, useState, useEffect } from 'react';
import { User } from '@/lib/types';
import { api } from '@/lib/api';
import { useRouter } from 'next/navigation';

interface AuthContextType {
  user: User | null;
  loading: boolean;
  signin: (data: any) => Promise<void>;
  signup: (data: any) => Promise<void>;
  signout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    const savedUser = localStorage.getItem('user');
    const savedToken = localStorage.getItem('token');
    if (savedUser && savedToken) {
      setUser(JSON.parse(savedUser));
      api.setToken(savedToken);
    }
    setLoading(false);
  }, []);

  const signin = async (data: any) => {
    const res = await api.signin(data);
    api.setToken(res.access_token);
    setUser(res.user);
    localStorage.setItem('user', JSON.stringify(res.user));
    router.push('/dashboard');
  };

  const signup = async (data: any) => {
    const res = await api.signup(data);
    api.setToken(res.access_token);
    setUser(res.user);
    localStorage.setItem('user', JSON.stringify(res.user));
    router.push('/dashboard');
  };

  const signout = () => {
    api.signout();
    setUser(null);
    localStorage.removeItem('user');
    localStorage.removeItem('token');
    router.push('/signin');
  };

  return (
    <AuthContext.Provider value={{ user, loading, signin, signup, signout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
