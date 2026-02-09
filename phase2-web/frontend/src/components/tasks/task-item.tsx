import React from 'react';
import { Task } from '@/lib/types';
import { Button } from '@/components/ui/button';

interface TaskItemProps {
  task: Task;
  onToggle: (id: number, completed: boolean) => void;
  onDelete: (id: number) => void;
  onEdit: (task: Task) => void;
}

export const TaskItem: React.FC<TaskItemProps> = ({ task, onToggle, onDelete, onEdit }) => {
  return (
    <div className={`flex items-center justify-between p-5 border-b border-border hover:bg-gray-50 dark:hover:bg-gray-800/40 transition-all duration-200 group ${task.completed ? 'opacity-75' : ''}`}>
      <div className="flex items-center space-x-5 flex-grow">
        <div className="relative flex items-center">
          <input
            type="checkbox"
            checked={task.completed}
            onChange={(e) => onToggle(task.id, e.target.checked)}
            className="h-6 w-6 rounded border-border text-blue-600 focus:ring-blue-500/50 cursor-pointer transition-all hover:scale-110"
          />
        </div>
        <div className="flex-grow min-w-0 pr-4">
          <h3 className={`text-lg font-bold truncate transition-all ${task.completed ? 'line-through opacity-40' : 'text-foreground'}`}>
            {task.title}
          </h3>
          {task.description && (
            <p className="text-sm opacity-60 truncate max-w-xl mt-0.5">{task.description}</p>
          )}
        </div>
      </div>
      <div className="flex space-x-3 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
        <Button 
          variant="secondary" 
          size="sm" 
          onClick={() => onEdit(task)}
          className="bg-transparent hover:bg-gray-200 dark:hover:bg-gray-700"
        >
          <svg className="h-4 w-4 mr-1.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
          </svg>
          Edit
        </Button>
        <Button 
          variant="outline" 
          size="sm" 
          onClick={() => onDelete(task.id)}
          className="text-red-500 border-none hover:bg-red-50 dark:hover:bg-red-900/20 hover:text-red-600"
        >
          <svg className="h-4 w-4 mr-1.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
          </svg>
          Delete
        </Button>
      </div>
    </div>
  );
};