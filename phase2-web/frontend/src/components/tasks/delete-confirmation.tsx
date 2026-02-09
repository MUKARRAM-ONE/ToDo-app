'use client';

import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';

interface DeleteConfirmationProps {
  isOpen: boolean;
  onConfirm: () => void;
  onCancel: () => void;
  title: string;
}

export const DeleteConfirmation: React.FC<DeleteConfirmationProps> = ({ isOpen, onConfirm, onCancel, title }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4 z-50 transition-all duration-300">
      <Card className="max-w-md w-full shadow-2xl border-none p-8 animate-in fade-in zoom-in duration-200">
        <div className="bg-red-100 dark:bg-red-900/30 text-red-600 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
          </svg>
        </div>
        
        <h3 className="text-2xl font-bold text-center mb-2">Delete Task?</h3>
        <p className="opacity-70 text-center mb-8 text-lg">
          Are you sure you want to delete <span className="font-extrabold text-foreground">"{title}"</span>? This action is permanent.
        </p>
        
        <div className="flex flex-col sm:flex-row gap-3">
          <Button 
            variant="outline" 
            onClick={onCancel}
            className="flex-grow py-3"
          >
            Keep Task
          </Button>
          <Button 
            variant="danger" 
            onClick={onConfirm}
            className="flex-grow py-3 font-bold"
          >
            Yes, Delete
          </Button>
        </div>
      </Card>
    </div>
  );
};