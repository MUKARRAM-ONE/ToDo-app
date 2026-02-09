'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { Navbar } from '@/components/layout/navbar';
import { Footer } from '@/components/layout/footer';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Input } from '@/components/ui/input';

export default function DemoEntryPage() {
  const [showDemo, setShowDemo] = useState(false);

  if (showDemo) {
    return <DemoDashboard />;
  }

  return (
    <div className="flex flex-col min-h-screen bg-gray-50">
      <Navbar />
      <main className="flex-grow flex items-center justify-center px-4 py-12">
        <div className="max-w-2xl w-full">
          <Card className="p-8 md:p-12 text-center shadow-xl">
            <div className="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6">
              <svg className="h-8 w-8 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h1 className="text-3xl font-extrabold text-gray-900 mb-4">Interactive Live Demo</h1>
            <p className="text-lg text-gray-600 mb-8">
              Experience the full power of TodoApp without creating an account. 
              This demo is completely interactive, but please note that it is 
              <span className="font-bold"> not connected to a database</span>.
            </p>
            
            <div className="bg-yellow-50 border-l-4 border-yellow-400 p-4 mb-8 text-left">
              <h3 className="text-sm font-bold text-yellow-800 uppercase tracking-wide">Instructions & Limitations</h3>
              <ul className="mt-2 text-sm text-yellow-700 space-y-1 list-disc list-inside">
                <li>Create, edit, and complete tasks just like the real app.</li>
                <li>Your data is stored only in your browser's current session.</li>
                <li>Refreshing the page or leaving the site will reset all progress.</li>
                <li>To save your work permanently, please sign up for a free account.</li>
              </ul>
            </div>

            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button 
                onClick={() => setShowDemo(true)}
                className="px-10 py-4 text-lg"
              >
                Continue as Guest User
              </Button>
              <Link href="/signup">
                <Button variant="outline" className="px-10 py-4 text-lg w-full sm:w-auto">
                  Sign Up Instead
                </Button>
              </Link>
            </div>
          </Card>
        </div>
      </main>
      <Footer />
    </div>
  );
}

function DemoDashboard() {
  const [tasks, setTasks] = useState([
    { id: 1, title: 'Explore the TodoApp', description: 'Try adding your own tasks!', completed: false },
    { id: 2, title: 'Master productivity', description: 'Mark this as complete to feel good.', completed: true },
  ]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [editId, setEditId] = useState<number | null>(null);

  const addTask = (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim()) return;

    if (editId !== null) {
      setTasks(tasks.map(t => t.id === editId ? { ...t, title, description } : t));
      setEditId(null);
    } else {
      const newTask = {
        id: Date.now(),
        title,
        description,
        completed: false
      };
      setTasks([...tasks, newTask]);
    }
    setTitle('');
    setDescription('');
  };

  const toggleTask = (id: number) => {
    setTasks(tasks.map(t => t.id === id ? { ...t, completed: !t.completed } : t));
  };

  const deleteTask = (id: number) => {
    setTasks(tasks.filter(t => t.id !== id));
  };

  const startEdit = (task: any) => {
    setEditId(task.id);
    setTitle(task.title);
    setDescription(task.description || '');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="min-h-screen bg-background text-foreground transition-colors duration-300">
      <nav className="bg-card shadow-sm border-b border-border transition-colors duration-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex justify-between items-center">
          <Link href="/" className="flex items-center hover:opacity-80 transition-opacity">
            <span className="text-xl font-bold text-blue-600">TodoApp <span className="text-xs bg-blue-100 dark:bg-blue-900/40 text-blue-600 px-2 py-1 rounded ml-2 uppercase tracking-wider">Demo</span></span>
          </Link>
          <Link href="/">
            <Button variant="outline" size="sm" className="font-bold border-blue-200 hover:border-blue-600 hover:text-blue-600">
              Exit Demo
            </Button>
          </Link>
        </div>
      </nav>

      <div className="max-w-4xl mx-auto py-12 px-4">
        <div className="bg-blue-600 rounded-2xl p-8 mb-12 text-white shadow-xl relative overflow-hidden group">
          <div className="relative z-10">
            <h2 className="text-3xl font-black">Welcome to the Playground</h2>
            <p className="opacity-90 mt-2 text-lg">This is a fully interactive local demo. Your data stays only in this session.</p>
          </div>
          <div className="absolute top-0 right-0 -mt-4 -mr-4 bg-white/10 w-32 h-32 rounded-full transition-transform group-hover:scale-150 duration-700"></div>
        </div>

        <Card className="mb-12 p-8 border-none shadow-2xl bg-gray-50/50 dark:bg-gray-800/20">
          <form onSubmit={addTask} className="space-y-6">
            <h3 className="text-2xl font-black tracking-tight">{editId !== null ? 'Update Task' : 'Quick Add'}</h3>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-bold opacity-60 mb-1">Task Title</label>
                <Input
                  type="text"
                  value={title}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) => setTitle(e.target.value)}
                  placeholder="What's on your mind?"
                  className="bg-background"
                  required
                />
              </div>
              <div>
                <label className="block text-sm font-bold opacity-60 mb-1">Details (optional)</label>
                <textarea
                  value={description}
                  onChange={(e: React.ChangeEvent<HTMLTextAreaElement>) => setDescription(e.target.value)}
                  className="mt-1 block w-full px-4 py-3 bg-background border border-border rounded-md shadow-sm focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 text-foreground outline-none transition-all"
                  rows={2}
                  placeholder="Add some more context..."
                />
              </div>
              <div className="flex gap-3 pt-2">
                <Button 
                  type="submit" 
                  className="flex-grow py-4 text-lg font-black"
                >
                  {editId !== null ? 'Save Changes' : 'Add Task'}
                </Button>
                {editId !== null && (
                  <Button 
                    type="button" 
                    variant="secondary" 
                    onClick={() => { setEditId(null); setTitle(''); setDescription(''); }}
                    className="px-8"
                  >
                    Cancel
                  </Button>
                )}
              </div>
            </div>
          </form>
        </Card>

        <div className="space-y-6">
          <h3 className="text-2xl font-black text-foreground/80 px-1">Your Tasks</h3>
          {tasks.length === 0 ? (
            <div className="text-center py-20 bg-card rounded-2xl border-2 border-dashed border-border group hover:border-blue-500/50 transition-colors">
              <div className="bg-blue-100 dark:bg-blue-900/30 text-blue-600 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform">
                <svg className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
                </svg>
              </div>
              <p className="opacity-60 text-lg font-bold">Your task list is empty.</p>
              <p className="opacity-40 text-sm">Add something above to get started!</p>
            </div>
          ) : (
            <Card className="p-0 overflow-hidden border-none shadow-2xl">
              <div className="divide-y divide-border">
                {tasks.map((task) => (
                  <div 
                    key={task.id} 
                    className={`flex items-center justify-between p-6 hover:bg-blue-50/50 dark:hover:bg-blue-900/10 transition-all cursor-pointer group ${task.completed ? 'opacity-60' : ''}`}
                    onClick={() => startEdit(task)}
                  >
                    <div className="flex items-center space-x-6 flex-grow" onClick={(e) => e.stopPropagation()}>
                      <input
                        type="checkbox"
                        checked={task.completed}
                        onChange={() => toggleTask(task.id)}
                        className="h-6 w-6 text-blue-600 rounded-md border-border focus:ring-blue-500/50 cursor-pointer transition-transform hover:scale-110"
                      />
                      <div className="min-w-0 pr-4">
                        <h4 className={`text-lg font-bold transition-all ${task.completed ? 'line-through opacity-40' : 'text-foreground'}`}>
                          {task.title}
                        </h4>
                        {task.description && <p className="text-sm opacity-60 truncate mt-1">{task.description}</p>}
                      </div>
                    </div>
                    <div className="flex space-x-3 opacity-0 group-hover:opacity-100 transition-opacity">
                      <button 
                        onClick={(e) => { e.stopPropagation(); startEdit(task); }}
                        className="p-2.5 text-blue-600 bg-blue-50 dark:bg-blue-900/30 hover:bg-blue-600 hover:text-white rounded-xl transition-all"
                        title="Edit Task"
                      >
                        <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                        </svg>
                      </button>
                      <button 
                        onClick={(e) => { e.stopPropagation(); deleteTask(task.id); }}
                        className="p-2.5 text-red-600 bg-red-50 dark:bg-red-900/30 hover:bg-red-600 hover:text-white rounded-xl transition-all"
                        title="Delete Task"
                      >
                        <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                        </svg>
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </Card>
          )}
        </div>

        <div className="mt-12 text-center text-gray-500 text-sm">
          Enjoying the app? <Link href="/signup" className="text-blue-600 font-medium underline">Create an account</Link> to start saving your real tasks.
        </div>
      </div>
      <Footer />
    </div>
  );
}
