'use client';

import { useAuth } from '@/context/auth-context';
import { Button } from '@/components/ui/button';

export const DashboardHeader = () => {
  const { user, signout } = useAuth();

  return (
    <header className="bg-background border-b border-border shadow-sm transition-colors duration-200">
      <div className="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
        <div>
          <h1 className="text-4xl font-extrabold tracking-tight">My Tasks</h1>
          {user && <p className="text-sm opacity-60 mt-1 italic">Welcome back, {user.name}</p>}
        </div>
        <Button 
          variant="outline"
          size="sm"
          onClick={signout}
          className="text-red-600 border-red-200 hover:bg-red-50 hover:border-red-600 dark:hover:bg-red-900/20"
        >
          Sign Out
        </Button>
      </div>
    </header>
  );
};