import { ProtectedRoute } from "@/components/auth/protected-route";
import { DashboardHeader } from "@/components/layout/dashboard-header";
import { Navbar } from "@/components/layout/navbar";
import { Footer } from "@/components/layout/footer";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <ProtectedRoute>
      <div className="flex flex-col min-h-screen">
        <Navbar />
        <div className="flex-grow bg-gray-100">
          <DashboardHeader />
          <main>
            <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
              {children}
            </div>
          </main>
        </div>
        <Footer />
      </div>
    </ProtectedRoute>
  );
}