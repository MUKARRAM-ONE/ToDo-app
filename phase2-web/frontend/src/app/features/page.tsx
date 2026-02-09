'use client';

import React from 'react';
import { Navbar } from '@/components/layout/navbar';
import { Footer } from '@/components/layout/footer';
import { Card } from '@/components/ui/card';

export default function FeaturesPage() {
  const features = [
    {
      title: "Smart Task Organization",
      description: "Automatically categorize and prioritize your tasks. Our intuitive system helps you focus on what matters most right now.",
      icon: (
        <svg className="h-10 w-10 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
        </svg>
      )
    },
    {
      title: "Seamless Authentication",
      description: "Secure, JWT-based login system that keeps your data private across all your devices. Quick signup gets you started in seconds.",
      icon: (
        <svg className="h-10 w-10 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
        </svg>
      )
    },
    {
      title: "Real-time Persistence",
      description: "Your data is instantly synced to our cloud database. Never worry about losing your progress or notes again.",
      icon: (
        <svg className="h-10 w-10 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4" />
        </svg>
      )
    },
    {
      title: "Mobile-First Design",
      description: "A fully responsive interface that looks and works beautifully on smartphones, tablets, and desktop computers.",
      icon: (
        <svg className="h-10 w-10 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
        </svg>
      )
    },
    {
      title: "Intuitive UX/UI",
      description: "Clean, modern design inspired by Material Design principles. Minimize friction and maximize your productivity.",
      icon: (
        <svg className="h-10 w-10 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
        </svg>
      )
    },
    {
      title: "Advanced Filtering",
      description: "Powerful search and filter options allow you to quickly find specific tasks or view them by status and date.",
      icon: (
        <svg className="h-10 w-10 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
        </svg>
      )
    }
  ];

  return (
    <div className="flex flex-col min-h-screen bg-background text-foreground transition-colors duration-300">
      <Navbar />
      <main className="flex-grow py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-20">
            <h1 className="text-4xl font-extrabold sm:text-5xl lg:text-6xl">
              Powerful Features for <span className="text-blue-600">Power Users</span>
            </h1>
            <p className="mt-4 text-xl opacity-70 max-w-3xl mx-auto">
              Everything you need to manage your personal and professional life in one beautiful application.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
            {features.map((feature, index) => (
              <Card key={index} className="p-8 hover:shadow-xl transition-all border-none bg-gray-50/50 dark:bg-gray-800/30">
                <div className="mb-6">{feature.icon}</div>
                <h3 className="text-xl font-bold mb-3">{feature.title}</h3>
                <p className="opacity-70 leading-relaxed">{feature.description}</p>
              </Card>
            ))}
          </div>

          <div className="mt-20 bg-blue-600 rounded-3xl p-12 text-center text-white">
            <h2 className="text-3xl font-bold mb-4">Ready to boost your productivity?</h2>
            <p className="text-blue-100 text-lg mb-8 max-w-2xl mx-auto">
              Join thousands of users who have transformed the way they manage their daily tasks.
            </p>
            <div className="flex flex-col sm:flex-row justify-center gap-4">
              <a href="/signup" className="bg-white text-blue-600 px-8 py-3 rounded-md font-bold hover:bg-blue-50 transition-colors">
                Start for Free
              </a>
              <a href="/demo" className="bg-blue-700 text-white px-8 py-3 rounded-md font-bold hover:bg-blue-800 transition-colors">
                Try Live Demo
              </a>
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}
