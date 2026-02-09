import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'danger' | 'outline';
  size?: 'sm' | 'md' | 'lg';
}

export const Button: React.FC<ButtonProps> = ({ variant = 'primary', size = 'md', className, ...props }) => {
  const baseStyles = 'rounded-md font-medium transition-all duration-200 disabled:opacity-50 inline-flex items-center justify-center active:scale-95 focus:outline-none focus:ring-2 focus:ring-offset-2 select-none shadow-sm hover:shadow-md';
  
  const sizes = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-5 py-2.5',
    lg: 'px-8 py-4 text-lg',
  };

  const variants = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500 shadow-blue-200',
    secondary: 'bg-gray-100 text-gray-800 hover:bg-gray-200 focus:ring-gray-300 dark:bg-gray-800 dark:text-gray-100 dark:hover:bg-gray-700',
    danger: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500 shadow-red-200',
    outline: 'bg-transparent border-2 border-gray-300 text-gray-700 hover:bg-gray-50 hover:border-blue-600 hover:text-blue-600 focus:ring-blue-500 dark:text-gray-200 dark:border-gray-600 dark:hover:bg-gray-800',
  };

  return (
    <button className={`${baseStyles} ${sizes[size]} ${variants[variant]} ${className}`} {...props} />
  );
};
