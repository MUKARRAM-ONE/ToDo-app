'use client';

import React, { useState, useEffect } from 'react';
import { useAuth } from '@/context/auth-context';
import { api } from '@/lib/api';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card } from '@/components/ui/card';
import { Task } from '@/lib/types';

interface TaskFormProps {
  onSuccess: () => void;
  editTask: Task | null;
  onCancel: () => void;
}

export const TaskForm: React.FC<TaskFormProps> = ({ onSuccess, editTask, onCancel }) => {
  const { user } = useAuth();
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (editTask) {
      setTitle(editTask.title);
      setDescription(editTask.description || '');
    } else {
      setTitle('');
      setDescription('');
    }
  }, [editTask]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!user) return;
    setLoading(true);
    try {
      if (editTask) {
        await api.updateTask(user.id, editTask.id, { title, description });
      } else {
        await api.createTask(user.id, { title, description });
      }
      setTitle('');
      setDescription('');
      onSuccess();
    } catch (err: any) {
      alert(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className="mb-8 p-6 transition-all duration-300 border-none shadow-lg bg-gray-50/50 dark:bg-gray-800/30">
      <form onSubmit={handleSubmit} className="space-y-6">
        <h3 className="text-2xl font-bold tracking-tight">
          {editTask ? 'Update Task' : 'Create New Task'}
        </h3>
        
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-semibold opacity-70 mb-1">Task Title</label>
            <Input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              required
              placeholder="What needs to be done?"
              className="bg-white dark:bg-gray-900"
            />
          </div>
          
          <div>
            <label className="block text-sm font-semibold opacity-70 mb-1">Detailed Description (optional)</label>
            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="mt-1 block w-full px-4 py-3 bg-white dark:bg-gray-900 border border-border rounded-md shadow-sm 
              focus:outline-none focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 transition-all duration-200
              placeholder:text-gray-400 text-foreground outline-none"
              placeholder="Add some context or details..."
              rows={3}
            />
          </div>
        </div>

        <div className="flex space-x-3">
          <Button 
            type="submit" 
            disabled={loading}
            className="px-8"
          >
            {loading ? 'Processing...' : editTask ? 'Save Changes' : 'Create Task'}
          </Button>
          {editTask && (
            <Button 
              type="button" 
              variant="secondary" 
              onClick={onCancel}
              className="px-8"
            >
              Cancel
            </Button>
          )}
        </div>
      </form>
    </Card>
  );
};