import { useEffect } from 'react';
import { Toaster } from "react-hot-toast"
import Navbar    from "./components/Navbar"
import Hero      from "./components/Hero"
import About     from "./components/About"
import Skills    from "./components/Skills"
import Projects  from "./components/Projects"
import Experience from "./components/Experience"
import Contact   from "./components/Contact"
import Footer    from "./components/Footer"

export default function App() {
  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/api/visitor`,  {
      method: 'POST'
    });
  }, []);
  return (
    
    <div className="bg-dark text-white min-h-screen">
      <Toaster position="top-right" toastOptions={{
        style: { background: "#1a1a1a", color: "#fff", border: "1px solid rgba(255,255,255,0.1)" }
      }} />
      <Navbar />
      <Hero />
      <About />
      <Skills />
      <Projects />
      <Experience />
      <Contact />
      <Footer />
    </div>
  )
}
