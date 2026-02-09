import { AuthResponse, User, Task } from './types';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

class ApiClient {
  private token: string | null = null;

  constructor() {
    if (typeof window !== 'undefined') {
      this.token = localStorage.getItem('token');
    }
  }

  setToken(token: string | null) {
    this.token = token;
    if (token) {
      localStorage.setItem('token', token);
    } else {
      localStorage.removeItem('token');
    }
  }

  async fetch(endpoint: string, options: RequestInit = {}) {
    const headers: any = {
      'Content-Type': 'application/json',
      ...(this.token ? { Authorization: `Bearer ${this.token}` } : {}),
      ...options.headers,
    };

    const response = await fetch(`${API_URL}${endpoint}`, {
      ...options,
      headers,
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Something went wrong');
    }

    if (response.status === 204) return null;
    return response.json();
  }

  async signup(data: any): Promise<AuthResponse> {
    return this.fetch('/api/auth/signup', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  async signin(data: any): Promise<AuthResponse> {
    return this.fetch('/api/auth/signin', {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  async signout() {
    this.setToken(null);
    return this.fetch('/api/auth/signout', { method: 'POST' });
  }

  async getTasks(userId: string, status: string = 'all'): Promise<Task[]> {
    return this.fetch(`/api/tasks/${userId}/tasks?status=${status}`);
  }

  async createTask(userId: string, data: any): Promise<Task> {
    return this.fetch(`/api/tasks/${userId}/tasks`, {
      method: 'POST',
      body: JSON.stringify(data),
    });
  }

  async updateTask(userId: string, id: number, data: any): Promise<Task> {
    return this.fetch(`/api/tasks/${userId}/tasks/${id}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  }

  async deleteTask(userId: string, id: number): Promise<void> {
    return this.fetch(`/api/tasks/${userId}/tasks/${id}`, {
      method: 'DELETE',
    });
  }

  async toggleComplete(userId: string, id: number, completed: boolean): Promise<Task> {
    return this.fetch(`/api/tasks/${userId}/tasks/${id}/complete`, {
      method: 'PATCH',
      body: JSON.stringify({ completed }),
    });
  }
}

export const api = new ApiClient();