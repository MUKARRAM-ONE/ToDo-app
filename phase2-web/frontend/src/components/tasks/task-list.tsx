'use client';

import React, { useState, useEffect } from 'react';
import { Task } from '@/lib/types';
import { api } from '@/lib/api';
import { useAuth } from '@/context/auth-context';
import { TaskItem } from './task-item';
import { DeleteConfirmation } from './delete-confirmation';
import { Card } from '@/components/ui/card';

interface TaskListProps {
  refreshTrigger: number;
  onEdit: (task: Task) => void;
}

export const TaskList: React.FC<TaskListProps> = ({ refreshTrigger, onEdit }) => {
  const { user } = useAuth();
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  
  const [deleteTask, setDeleteTask] = useState<Task | null>(null);

  const fetchTasks = async () => {
    if (!user) return;
    try {
      const data = await api.getTasks(user.id);
      setTasks(data);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, [user, refreshTrigger]);

  const handleToggle = async (id: number, completed: boolean) => {
    if (!user) return;
    try {
      await api.toggleComplete(user.id, id, completed);
      setTasks(tasks.map(t => t.id === id ? { ...t, completed } : t));
    } catch (err: any) {
      alert(err.message);
    }
  };

  const confirmDelete = async () => {
    if (!user || !deleteTask) return;
    try {
      await api.deleteTask(user.id, deleteTask.id);
      setTasks(tasks.filter(t => t.id !== deleteTask.id));
      setDeleteTask(null);
    } catch (err: any) {
      alert(err.message);
    }
  };

  if (loading) return (
    <div className="flex flex-col items-center justify-center py-20 space-y-4">
      <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      <p className="opacity-60 font-medium">Loading your tasks...</p>
    </div>
  );

  if (error) return (
    <Card className="border-red-200 bg-red-50 dark:bg-red-900/10 p-8 text-center">
      <p className="text-red-600 dark:text-red-400 font-bold">{error}</p>
      <Button variant="outline" size="sm" onClick={fetchTasks} className="mt-4">Try Again</Button>
    </Card>
  );

  if (tasks.length === 0) return (
    <div className="text-center py-20 bg-gray-50/50 dark:bg-gray-800/20 rounded-2xl border-2 border-dashed border-border">
      <div className="bg-blue-100 dark:bg-blue-900/30 text-blue-600 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
        <svg className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
        </svg>
      </div>
      <h3 className="text-xl font-bold opacity-80">No tasks found</h3>
      <p className="opacity-60 mt-1 max-w-xs mx-auto">Get started by creating your first task above!</p>
    </div>
  );

  return (
    <>
      <Card className="p-0 overflow-hidden border-none shadow-xl">
        <div className="divide-y divide-border">
          {tasks.map(task => (
            <TaskItem
              key={task.id}
              task={task}
              onToggle={handleToggle}
              onDelete={() => setDeleteTask(task)}
              onEdit={onEdit}
            />
          ))}
        </div>
      </Card>

      <DeleteConfirmation
        isOpen={!!deleteTask}
        title={deleteTask?.title || ''}
        onConfirm={confirmDelete}
        onCancel={() => setDeleteTask(null)}
      />
    </>
  );
};