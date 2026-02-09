'use client';

import React, { useState } from 'react';
import { Navbar } from '@/components/layout/navbar';
import { Footer } from '@/components/layout/footer';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';
import { Input } from '@/components/ui/input';

export default function ContactPage() {
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <div className="flex flex-col min-h-screen bg-background text-foreground transition-colors duration-300">
      <Navbar />
      <main className="flex-grow py-20 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h1 className="text-4xl font-extrabold sm:text-5xl">Contact Us</h1>
            <p className="mt-4 text-xl opacity-70">Have questions? We're here to help.</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
            <Card className="p-8 border-none shadow-xl">
              {submitted ? (
                <div className="text-center py-12">
                  <div className="bg-green-100 dark:bg-green-900/30 text-green-600 dark:text-green-400 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                    <svg className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <h2 className="text-2xl font-bold">Message Sent!</h2>
                  <p className="opacity-70 mt-2">Thank you for reaching out. We'll get back to you soon.</p>
                  <Button className="mt-8" onClick={() => setSubmitted(false)}>Send another message</Button>
                </div>
              ) : (
                <form onSubmit={handleSubmit} className="space-y-6">
                  <div>
                    <label className="block text-sm font-semibold opacity-70 mb-1">Full Name</label>
                    <Input type="text" placeholder="John Doe" required />
                  </div>
                  <div>
                    <label className="block text-sm font-semibold opacity-70 mb-1">Email Address</label>
                    <Input type="email" placeholder="john@example.com" required />
                  </div>
                  <div>
                    <label className="block text-sm font-semibold opacity-70 mb-1">Subject</label>
                    <Input type="text" placeholder="How can we help?" required />
                  </div>
                  <div>
                    <label className="block text-sm font-semibold opacity-70 mb-1">Message</label>
                    <textarea
                      className="mt-1 block w-full px-4 py-3 bg-background border border-border rounded-md shadow-sm focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500 text-foreground outline-none transition-all duration-200"
                      rows={4}
                      placeholder="Your message here..."
                      required
                    ></textarea>
                  </div>
                  <Button type="submit" className="w-full py-4 text-lg font-bold">Send Message</Button>
                </form>
              )}
            </Card>

            <div className="flex flex-col justify-center space-y-8">
              <div>
                <h3 className="text-xl font-bold mb-2">Our Office</h3>
                <p className="opacity-70">
                  123 Productivity Way<br />
                  Suite 456<br />
                  Tech City, TC 12345
                </p>
              </div>
              <div>
                <h3 className="text-xl font-bold mb-2">Email Us</h3>
                <p className="opacity-70 font-medium">support@todoapp.com</p>
                <p className="opacity-70 font-medium">info@todoapp.com</p>
              </div>
              <div>
                <h3 className="text-xl font-bold mb-2">Follow Us</h3>
                <div className="flex space-x-6 mt-2">
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-bold transition-colors">Twitter</a>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-bold transition-colors">LinkedIn</a>
                  <a href="#" className="text-blue-600 hover:text-blue-700 font-bold transition-colors">GitHub</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}
