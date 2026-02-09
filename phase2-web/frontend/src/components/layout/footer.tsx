export const Footer = () => {
  return (
    <footer className="bg-background border-t border-border transition-colors duration-300">
      <div className="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row justify-between items-center gap-8">
          <div className="flex flex-col items-center md:items-start space-y-2">
            <span className="text-2xl font-black text-blue-600 tracking-tighter">TodoApp</span>
            <span className="opacity-50 text-sm font-medium">© {new Date().getFullYear()} Precision Productivity Inc.</span>
          </div>
          <div className="flex flex-wrap justify-center gap-x-8 gap-y-4">
            <a href="/features" className="opacity-60 hover:opacity-100 hover:text-blue-600 transition-all font-semibold">
              Features
            </a>
            <a href="/contact" className="opacity-60 hover:opacity-100 hover:text-blue-600 transition-all font-semibold">
              Contact
            </a>
            <a href="#" className="opacity-60 hover:opacity-100 hover:text-blue-600 transition-all font-semibold">
              Privacy
            </a>
            <a href="#" className="opacity-60 hover:opacity-100 hover:text-blue-600 transition-all font-semibold">
              Terms
            </a>
          </div>
        </div>
        <div className="mt-12 border-t border-border pt-8 text-center">
          <p className="text-sm opacity-40 font-medium">
            Engineered with <span className="text-blue-500">Next.js</span>, <span className="text-blue-500">FastAPI</span>, and <span className="text-blue-500">Tailwind CSS</span>.
          </p>
        </div>
      </div>
    </footer>
  );
};
