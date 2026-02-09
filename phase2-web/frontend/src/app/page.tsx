'use client';

import Link from 'next/link';
import { useAuth } from '@/context/auth-context';
import { Navbar } from '@/components/layout/navbar';
import { Footer } from '@/components/layout/footer';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';

export default function LandingPage() {
  const { user } = useAuth();

  return (
    <div className="flex flex-col min-h-screen bg-background text-foreground transition-colors duration-300">
      <Navbar />
      
      <main className="flex-grow">
        {/* Hero Section */}
        <section className="bg-gradient-to-b from-background to-blue-50/20 dark:to-blue-900/10 py-24 px-4 sm:px-6 lg:px-8">
          <div className="max-w-7xl mx-auto text-center">
            <h1 className="text-5xl tracking-tight font-extrabold sm:text-6xl md:text-7xl">
              <span className="block">Master your time,</span>{' '}
              <span className="block text-blue-600">conquer your goals</span>
            </h1>
            <p className="mt-6 max-w-2xl mx-auto text-lg opacity-80 sm:text-xl">
              The professional todo list application designed for clarity, 
              focus, and productivity. Join thousands who have organized their lives with TodoApp.
            </p>
            <div className="mt-10 flex flex-col sm:flex-row justify-center gap-4">
              {user ? (
                <Link href="/dashboard">
                  <Button size="lg" className="px-12 py-4">
                    Go to Dashboard
                  </Button>
                </Link>
              ) : (
                <>
                  <Link href="/signup">
                    <Button size="lg" className="px-12 py-4">
                      Get Started for Free
                    </Button>
                  </Link>
                  <Link href="/demo">
                    <Button variant="outline" size="lg" className="px-12 py-4">
                      Explore Live Demo
                    </Button>
                  </Link>
                </>
              )}
            </div>
          </div>
        </section>

        {/* Value Proposition */}
        <section className="py-24 bg-background px-4 sm:px-6 lg:px-8 border-y border-border">
          <div className="max-w-7xl mx-auto">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
              <div>
                <div className="bg-blue-100 dark:bg-blue-900/30 text-blue-600 w-12 h-12 rounded-lg flex items-center justify-center mx-auto mb-6 transition-colors">
                  <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                  </svg>
                </div>
                <h3 className="text-xl font-bold mb-2">Lightning Fast</h3>
                <p className="opacity-70">Built for speed so you can update your tasks in milliseconds.</p>
              </div>
              <div>
                <div className="bg-blue-100 dark:bg-blue-900/30 text-blue-600 w-12 h-12 rounded-lg flex items-center justify-center mx-auto mb-6 transition-colors">
                  <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                  </svg>
                </div>
                <h3 className="text-xl font-bold mb-2">Private & Secure</h3>
                <p className="opacity-70">Your data is yours alone. We use bank-grade security for your todos.</p>
              </div>
              <div>
                <div className="bg-blue-100 dark:bg-blue-900/30 text-blue-600 w-12 h-12 rounded-lg flex items-center justify-center mx-auto mb-6 transition-colors">
                  <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" />
                  </svg>
                </div>
                <h3 className="text-xl font-bold mb-2">Cloud Sync</h3>
                <p className="opacity-70">Access your tasks from your phone, tablet, or computer instantly.</p>
              </div>
            </div>
          </div>
        </section>

        {/* Call to Action */}
        <section className="py-24 bg-gray-50 dark:bg-gray-900/50 px-4 sm:px-6 lg:px-8">
          <div className="max-w-5xl mx-auto bg-blue-600 rounded-3xl overflow-hidden shadow-2xl flex flex-col md:flex-row">
            <div className="p-12 md:w-1/2 text-white">
              <h2 className="text-3xl font-bold mb-4">Start organizing your life today.</h2>
              <p className="text-blue-100 mb-8">
                Join our community of over 50,000 professionals who use TodoApp to keep their lives on track.
              </p>
              <Link href="/signup">
                <Button variant="secondary" size="lg" className="w-full sm:w-auto">
                  Get Started Now
                </Button>
              </Link>
            </div>
            <div className="bg-blue-500 md:w-1/2 p-12 flex items-center justify-center">
               <div className="bg-white/10 backdrop-blur-md rounded-xl p-6 w-full border border-white/20">
                  <div className="h-2 w-24 bg-white/20 rounded mb-4"></div>
                  <div className="space-y-3">
                    <div className="h-8 w-full bg-white/20 rounded flex items-center px-3">
                      <div className="h-4 w-4 rounded-full border border-white/40 mr-3"></div>
                      <div className="h-2 w-32 bg-white/40 rounded"></div>
                    </div>
                    <div className="h-8 w-full bg-white/20 rounded flex items-center px-3">
                      <div className="h-4 w-4 rounded-full border border-white/40 mr-3"></div>
                      <div className="h-2 w-24 bg-white/40 rounded"></div>
                    </div>
                    <div className="h-8 w-full bg-white/20 rounded flex items-center px-3">
                      <div className="h-4 w-4 bg-white/40 rounded-full mr-3 flex items-center justify-center">
                        <svg className="h-3 w-3 text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"/></svg>
                      </div>
                      <div className="h-2 w-40 bg-white/20 rounded"></div>
                    </div>
                  </div>
               </div>
            </div>
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
}