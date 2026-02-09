import { AuthForm } from '@/components/auth/auth-form';
import { Navbar } from '@/components/layout/navbar';
import { Footer } from '@/components/layout/footer';

export default function SignupPage() {
  return (
    <div className="flex flex-col min-h-screen">
      <Navbar />
      <main className="flex-grow flex flex-col items-center justify-center bg-gray-50 px-4 py-12">
        <AuthForm type="signup" />
      </main>
      <Footer />
    </div>
  );
}