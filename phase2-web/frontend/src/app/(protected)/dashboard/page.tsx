'use client';

import { useState } from 'react';
import { TaskList } from '@/components/tasks/task-list';
import { TaskForm } from '@/components/tasks/task-form';
import { Task } from '@/lib/types';

export default function DashboardPage() {
  const [refreshTrigger, setRefreshTrigger] = useState(0);
  const [editTask, setEditTask] = useState<Task | null>(null);

  const handleRefresh = () => {
    setRefreshTrigger(prev => prev + 1);
    setEditTask(null);
  };

  const handleEdit = (task: Task) => {
    setEditTask(task);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="space-y-8 px-4 sm:px-0">
      <TaskForm 
        onSuccess={handleRefresh} 
        editTask={editTask} 
        onCancel={() => setEditTask(null)} 
      />
      <TaskList 
        refreshTrigger={refreshTrigger} 
        onEdit={handleEdit} 
      />
    </div>
  );
}