'use client';

import Link from 'next/link';
import { useAuth } from '@/context/auth-context';
import { useTheme } from '@/context/theme-context';
import { Button } from '@/components/ui/button';

export const Navbar = () => {
  const { user, signout } = useAuth();
  const { theme, toggleTheme } = useTheme();

  return (
    <nav className="bg-white border-b border-gray-200 sticky top-0 z-50 dark:bg-gray-900 dark:border-gray-800 transition-colors">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link href="/" className="flex-shrink-0 flex items-center">
              <span className="text-2xl font-bold text-blue-600">TodoApp</span>
            </Link>
            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
              <Link
                href="/"
                className="border-transparent text-gray-500 hover:border-blue-600 hover:text-blue-600 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium transition-colors"
              >
                Home
              </Link>
              <Link
                href="/features"
                className="border-transparent text-gray-500 hover:border-blue-600 hover:text-blue-600 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium transition-colors"
              >
                Features
              </Link>
              <Link
                href="/contact"
                className="border-transparent text-gray-500 hover:border-blue-600 hover:text-blue-600 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium transition-colors"
              >
                Contact
              </Link>
            </div>
          </div>
          <div className="flex items-center space-x-4">
            <Button
              variant="outline"
              size="sm"
              onClick={toggleTheme}
              className="rounded-full w-10 h-10 p-0 flex items-center justify-center border-none hover:bg-gray-100 dark:hover:bg-gray-800"
              title={`Switch to ${theme === 'light' ? 'dark' : 'light'} mode`}
            >
              {theme === 'light' ? (
                <svg className="h-5 w-5 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
                </svg>
              ) : (
                <svg className="h-5 w-5 text-yellow-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
                </svg>
              )}
            </Button>
            {user ? (
              <>
                <Link href="/dashboard">
                  <Button variant="outline">Dashboard</Button>
                </Link>
                <Button variant="outline" onClick={signout} className="text-red-600 border-red-200 hover:bg-red-50">
                  Sign Out
                </Button>
              </>
            ) : (
              <>
                <Link href="/signin">
                  <Button variant="outline">Sign In</Button>
                </Link>
                <Link href="/signup">
                  <Button>Sign Up</Button>
                </Link>
              </>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
};
