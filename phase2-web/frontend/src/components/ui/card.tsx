import React from 'react';

export const Card: React.FC<{ children: React.ReactNode; className?: string }> = ({ children, className }) => {
  return (
    <div className={`bg-card text-card-foreground p-6 rounded-lg shadow-md border border-border transition-colors duration-200 ${className}`}>
      {children}
    </div>
  );
};
