import React from 'react';

export const Input: React.FC<React.InputHTMLAttributes<HTMLInputElement>> = ({ className, ...props }) => {
  return (
    <input
      className={`mt-1 block w-full px-4 py-2 bg-background border border-border rounded-md shadow-sm transition-all duration-200 
      focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 
      placeholder:text-gray-400 dark:placeholder:text-gray-500
      hover:border-gray-400 dark:hover:border-gray-500
      text-foreground ${className}`}
      {...props}
    />
  );
};
