'use client';

import React, { useState } from 'react';
import { useAuth } from '@/context/auth-context';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card } from '@/components/ui/card';
import Link from 'next/link';

interface AuthFormProps {
  type: 'signin' | 'signup';
}

export const AuthForm: React.FC<AuthFormProps> = ({ type }) => {
  const { signin, signup } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      if (type === 'signin') {
        await signin({ email, password });
      } else {
        await signup({ email, password, name });
      }
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="w-full max-w-md p-8 border-none shadow-xl">
      <form onSubmit={handleSubmit} className="space-y-6">
        <h2 className="text-3xl font-extrabold text-center">
          {type === 'signin' ? 'Sign In' : 'Sign Up'}
        </h2>
        
        {error && (
          <div className="bg-red-50 dark:bg-red-900/20 border-l-4 border-red-500 p-4 rounded">
            <p className="text-red-700 dark:text-red-400 text-sm">{error}</p>
          </div>
        )}
        
        <div className="space-y-4">
          {type === 'signup' && (
            <div>
              <label className="block text-sm font-semibold opacity-70 mb-1">Full Name</label>
              <Input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Enter your name"
                required
              />
            </div>
          )}
          
          <div>
            <label className="block text-sm font-semibold opacity-70 mb-1">Email Address</label>
            <Input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="name@example.com"
              required
            />
          </div>
          
          <div>
            <label className="block text-sm font-semibold opacity-70 mb-1">Password</label>
            <Input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              required
            />
          </div>
        </div>

        <Button
          type="submit"
          disabled={loading}
          className="w-full py-4 text-lg font-bold"
        >
          {loading ? 'Processing...' : type === 'signin' ? 'Sign In' : 'Sign Up'}
        </Button>
        
        <div className="text-center pt-2">
          {type === 'signin' ? (
            <p className="text-sm opacity-70">
              Don't have an account?{' '}
              <Link href="/signup" className="text-blue-600 hover:underline font-bold">Sign Up</Link>
            </p>
          ) : (
            <p className="text-sm opacity-70">
              Already have an account?{' '}
              <Link href="/signin" className="text-blue-600 hover:underline font-bold">Sign In</Link>
            </p>
          )}
        </div>
      </form>
    </Card>
  );
};