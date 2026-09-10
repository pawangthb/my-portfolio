#!/usr/bin/env python3
import os

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f'  ✓ {path}')

base = '/data/portfolio'

# ─── FRONTEND ──────────────────────────────────────────────────────────────────

write(f'{base}/frontend/package.json', '''{
  "name": "alphaxcoder-portfolio",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "framer-motion": "^11.0.0",
    "react-icons": "^5.0.0",
    "axios": "^1.6.0",
    "react-hot-toast": "^2.4.1",
    "react-intersection-observer": "^9.5.3",
    "react-type-animation": "^3.2.0",
    "react-scroll": "^1.9.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.0",
    "@vitejs/plugin-react": "^4.2.0",
    "autoprefixer": "^10.4.17",
    "postcss": "^8.4.35",
    "tailwindcss": "^3.4.1",
    "vite": "^5.0.0"
  }
}
''')

write(f'{base}/frontend/vite.config.js', '''import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: { port: 3000 },
  build: { outDir: 'dist', sourcemap: false }
})
''')

write(f'{base}/frontend/tailwind.config.js', '''/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: { sans: ['Inter', 'sans-serif'] },
      colors: {
        primary: '#2783DE',
        accent:  '#5E9FE8',
        dark:    '#0d0d0d',
        surface: '#111111',
        card:    '#1a1a1a',
        border:  'rgba(255,255,255,0.08)',
      },
      animation: {
        'gradient-x': 'gradient-x 8s ease infinite',
        'float': 'float 6s ease-in-out infinite',
        'pulse-slow': 'pulse 4s cubic-bezier(0.4,0,0.6,1) infinite',
      },
      keyframes: {
        'gradient-x': {
          '0%,100%': { backgroundPosition: '0% 50%' },
          '50%':     { backgroundPosition: '100% 50%' },
        },
        float: {
          '0%,100%': { transform: 'translateY(0px)' },
          '50%':     { transform: 'translateY(-20px)' },
        },
      },
    },
  },
  plugins: [],
}
''')

write(f'{base}/frontend/postcss.config.js', '''export default {
  plugins: { tailwindcss: {}, autoprefixer: {} }
}
''')

write(f'{base}/frontend/index.html', '''<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Alphaxcoder - Full Stack Developer Portfolio" />
  <meta property="og:title" content="Alphaxcoder | Developer" />
  <meta property="og:description" content="Building scalable products with clean code." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="icon" type="image/svg+xml" href="/vite.svg" />
  <title>Alphaxcoder | Developer</title>
</head>
<body>
  <div id="root"></div>
  <script type="module" src="/src/main.jsx"></script>
</body>
</html>
''')

write(f'{base}/frontend/src/index.css', '''@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  body {
    background: #0d0d0d;
    color: #ffffff;
    font-family: \'Inter\', sans-serif;
    -webkit-font-smoothing: antialiased;
  }
  ::-webkit-scrollbar { width: 4px; }
  ::-webkit-scrollbar-track { background: #0d0d0d; }
  ::-webkit-scrollbar-thumb { background: #2783DE; border-radius: 2px; }
}

@layer utilities {
  .glass {
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08);
  }
  .gradient-text {
    background: linear-gradient(135deg, #2783DE, #5E9FE8, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    background-size: 200% 200%;
    animation: gradient-x 6s ease infinite;
  }
  .glow {
    box-shadow: 0 0 40px rgba(39,131,222,0.25), 0 0 80px rgba(39,131,222,0.10);
  }
  .card-hover {
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
  }
  .card-hover:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 60px rgba(39,131,222,0.2);
    border-color: rgba(39,131,222,0.4);
  }
  .section-pad { padding: 100px 0; }
}
''')

write(f'{base}/frontend/src/main.jsx', '''import React from "react"
import ReactDOM from "react-dom/client"
import App from "./App"
import "./index.css"

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode><App /></React.StrictMode>
)
''')

write(f'{base}/frontend/src/App.jsx', '''import { Toaster } from "react-hot-toast"
import Navbar    from "./components/Navbar"
import Hero      from "./components/Hero"
import About     from "./components/About"
import Skills    from "./components/Skills"
import Projects  from "./components/Projects"
import Experience from "./components/Experience"
import Contact   from "./components/Contact"
import Footer    from "./components/Footer"

export default function App() {
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
''')

# Navbar
write(f'{base}/frontend/src/components/Navbar.jsx', '''import { useState, useEffect } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { Link } from "react-scroll"

const links = ["About","Skills","Projects","Experience","Contact"]

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false)
  const [open, setOpen] = useState(false)

  useEffect(() => {
    const h = () => setScrolled(window.scrollY > 20)
    window.addEventListener("scroll", h)
    return () => window.removeEventListener("scroll", h)
  }, [])

  return (
    <motion.nav
      initial={{ y: -80, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6 }}
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled ? "glass border-b border-border" : ""
      }`}
    >
      <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
        <motion.span
          className="text-xl font-bold gradient-text cursor-pointer"
          whileHover={{ scale: 1.05 }}
        >
          &lt;Alphaxcoder /&gt;
        </motion.span>

        {/* Desktop */}
        <ul className="hidden md:flex items-center gap-8">
          {links.map(l => (
            <li key={l}>
              <Link
                to={l.toLowerCase()} smooth duration={600} offset={-70}
                className="text-sm text-gray-400 hover:text-white transition-colors cursor-pointer relative group"
              >
                {l}
                <span className="absolute -bottom-1 left-0 w-0 h-px bg-primary transition-all duration-300 group-hover:w-full" />
              </Link>
            </li>
          ))}
          <li>
            <Link to="contact" smooth duration={600} offset={-70}>
              <motion.button
                whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.97 }}
                className="px-5 py-2 text-sm rounded-full bg-primary text-white font-medium hover:bg-accent transition-colors"
              >
                Hire Me
              </motion.button>
            </Link>
          </li>
        </ul>

        {/* Mobile burger */}
        <button onClick={() => setOpen(!open)} className="md:hidden flex flex-col gap-1.5 p-1">
          <span className={`block w-6 h-0.5 bg-white transition-all ${open?"rotate-45 translate-y-2":""}`}/>
          <span className={`block w-6 h-0.5 bg-white transition-all ${open?"opacity-0":""}`}/>
          <span className={`block w-6 h-0.5 bg-white transition-all ${open?"-rotate-45 -translate-y-2":""}`}/>
        </button>
      </div>

      <AnimatePresence>
        {open && (
          <motion.div
            initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: "auto" }} exit={{ opacity: 0, height: 0 }}
            className="md:hidden glass border-t border-border px-6 pb-6"
          >
            {links.map(l => (
              <Link key={l} to={l.toLowerCase()} smooth duration={600} offset={-70}
                onClick={() => setOpen(false)}
                className="block py-3 text-gray-400 hover:text-white transition-colors cursor-pointer"
              >{l}</Link>
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </motion.nav>
  )
}
''')

# Hero
write(f'{base}/frontend/src/components/Hero.jsx', '''import { motion } from "framer-motion"
import { TypeAnimation } from "react-type-animation"
import { Link } from "react-scroll"
import { FiGithub, FiLinkedin, FiTwitter, FiArrowDown } from "react-icons/fi"

const socials = [
  { icon: <FiGithub />,   href: "https://github.com/alphaxcoder" },
  { icon: <FiLinkedin />, href: "https://linkedin.com/in/alphaxcoder" },
  { icon: <FiTwitter />,  href: "https://twitter.com/alphaxcoder" },
]

export default function Hero() {
  return (
    <section id="hero" className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Animated background orbs */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-[500px] h-[500px] bg-primary/10 rounded-full blur-[120px] animate-pulse-slow" />
        <div className="absolute bottom-1/4 right-1/4 w-[400px] h-[400px] bg-purple-500/10 rounded-full blur-[100px] animate-pulse-slow" style={{animationDelay:"2s"}} />
        <div className="absolute top-1/2 left-1/2 w-[300px] h-[300px] bg-accent/5 rounded-full blur-[80px] animate-float" />
      </div>

      {/* Grid pattern */}
      <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,.02)_1px,transparent_1px)] bg-[size:60px_60px] [mask-image:radial-gradient(ellipse_80%_80%_at_50%_50%,#000_40%,transparent_100%)]" />

      <div className="relative z-10 max-w-6xl mx-auto px-6 text-center">
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
        >
          {/* Badge */}
          <motion.div
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.5 }}
            className="inline-flex items-center gap-2 px-4 py-2 glass rounded-full text-sm text-primary mb-8"
          >
            <span className="w-2 h-2 rounded-full bg-green-400 animate-pulse" />
            Available for opportunities
          </motion.div>

          <h1 className="text-5xl md:text-7xl lg:text-8xl font-extrabold leading-tight mb-6">
            Hi, I\'m
            <span className="block gradient-text">Alphaxcoder</span>
          </h1>

          <div className="text-xl md:text-2xl text-gray-400 mb-8 h-8">
            <TypeAnimation
              sequence={[
                "Full Stack Developer", 2000,
                "React Specialist", 2000,
                "Node.js Engineer", 2000,
                "Open Source Contributor", 2000,
                "Problem Solver", 2000,
              ]}
              repeat={Infinity}
              wrapper="span"
            />
          </div>

          <p className="max-w-2xl mx-auto text-gray-400 text-lg leading-relaxed mb-12">
            I build scalable, performant web applications with clean code and intuitive UX.
            Passionate about turning complex problems into elegant solutions.
          </p>

          {/* CTA buttons */}
          <div className="flex flex-wrap items-center justify-center gap-4 mb-16">
            <Link to="projects" smooth duration={600} offset={-70}>
              <motion.button
                whileHover={{ scale: 1.05, boxShadow: "0 0 30px rgba(39,131,222,0.4)" }}
                whileTap={{ scale: 0.97 }}
                className="px-8 py-4 bg-primary text-white font-semibold rounded-full text-base transition-all"
              >
                View My Work
              </motion.button>
            </Link>
            <Link to="contact" smooth duration={600} offset={-70}>
              <motion.button
                whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.97 }}
                className="px-8 py-4 glass text-white font-semibold rounded-full text-base hover:border-primary/50 transition-all"
              >
                Get In Touch
              </motion.button>
            </Link>
          </div>

          {/* Socials */}
          <div className="flex items-center justify-center gap-4">
            {socials.map((s, i) => (
              <motion.a key={i} href={s.href} target="_blank" rel="noreferrer"
                whileHover={{ scale: 1.2, y: -4 }} whileTap={{ scale: 0.9 }}
                className="w-11 h-11 glass rounded-full flex items-center justify-center text-gray-400 hover:text-primary hover:border-primary/50 transition-all"
              >
                {s.icon}
              </motion.a>
            ))}
          </div>
        </motion.div>

        {/* Scroll indicator */}
        <motion.div
          animate={{ y: [0, 10, 0] }} transition={{ repeat: Infinity, duration: 2 }}
          className="absolute bottom-10 left-1/2 -translate-x-1/2 text-gray-600"
        >
          <FiArrowDown size={24} />
        </motion.div>
      </div>
    </section>
  )
}
''')

# About
write(f'{base}/frontend/src/components/About.jsx', '''import { motion } from "framer-motion"
import { useInView } from "react-intersection-observer"
import { FiCode, FiCoffee, FiHeart, FiTarget } from "react-icons/fi"

const stats = [
  { label: "Projects Built", value: "20+" },
  { label: "Years Coding",   value: "3+" },
  { label: "Technologies",   value: "15+" },
  { label: "Cups of Coffee", value: "∞" },
]

const traits = [
  { icon: <FiCode />,   title: "Clean Code",     desc: "I write maintainable, readable code following best practices and design patterns." },
  { icon: <FiTarget />, title: "Goal-Oriented",  desc: "I focus on delivering results that actually matter and move projects forward." },
  { icon: <FiHeart />,  title: "Passionate",     desc: "Genuinely love what I build — that passion shows in the quality of my work." },
  { icon: <FiCoffee />, title: "Always Learning",desc: "Tech evolves fast. I make sure to keep up and embrace new tools and patterns." },
]

export default function About() {
  const [ref, inView] = useInView({ threshold: 0.1, triggerOnce: true })

  return (
    <section id="about" className="section-pad" ref={ref}>
      <div className="max-w-6xl mx-auto px-6">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={inView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <span className="text-primary text-sm font-semibold tracking-widest uppercase">About Me</span>
          <h2 className="text-4xl md:text-5xl font-bold mt-3">Who I Am</h2>
        </motion.div>

        <div className="grid lg:grid-cols-2 gap-16 items-center mb-20">
          {/* Text */}
          <motion.div
            initial={{ opacity: 0, x: -40 }}
            animate={inView ? { opacity: 1, x: 0 } : {}}
            transition={{ duration: 0.7, delay: 0.2 }}
          >
            <p className="text-gray-400 text-lg leading-relaxed mb-6">
              I\'m a <span className="text-white font-semibold">Full Stack Developer</span> from Noida,
              currently pursuing engineering at NIET. I love crafting products that are not just
              functional but genuinely delightful to use.
            </p>
            <p className="text-gray-400 text-lg leading-relaxed mb-6">
              When I\'m not coding, I\'m exploring new technologies, contributing to open source,
              or mentoring fellow students. I believe great software is built at the intersection
              of technical excellence and empathy for the user.
            </p>
            <div className="flex gap-4 flex-wrap">
              <span className="px-4 py-2 glass rounded-full text-sm text-primary">📍 Noida, India</span>
              <span className="px-4 py-2 glass rounded-full text-sm text-green-400">🎓 B.Tech CSE</span>
              <span className="px-4 py-2 glass rounded-full text-sm text-purple-400">💼 Open to Work</span>
            </div>
          </motion.div>

          {/* Stats */}
          <motion.div
            initial={{ opacity: 0, x: 40 }}
            animate={inView ? { opacity: 1, x: 0 } : {}}
            transition={{ duration: 0.7, delay: 0.3 }}
            className="grid grid-cols-2 gap-4"
          >
            {stats.map((s, i) => (
              <motion.div key={i}
                whileHover={{ scale: 1.03 }}
                className="glass rounded-2xl p-6 text-center card-hover"
              >
                <div className="text-4xl font-extrabold gradient-text mb-2">{s.value}</div>
                <div className="text-gray-400 text-sm">{s.label}</div>
              </motion.div>
            ))}
          </motion.div>
        </div>

        {/* Traits */}
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {traits.map((t, i) => (
            <motion.div key={i}
              initial={{ opacity: 0, y: 30 }}
              animate={inView ? { opacity: 1, y: 0 } : {}}
              transition={{ duration: 0.5, delay: 0.1 * i }}
              whileHover={{ scale: 1.03 }}
              className="glass rounded-2xl p-6 card-hover"
            >
              <div className="w-12 h-12 bg-primary/10 rounded-xl flex items-center justify-center text-primary text-xl mb-4">{t.icon}</div>
              <h3 className="font-semibold text-white mb-2">{t.title}</h3>
              <p className="text-gray-400 text-sm leading-relaxed">{t.desc}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
''')

# Skills
write(f'{base}/frontend/src/components/Skills.jsx', '''import { motion } from "framer-motion"
import { useInView } from "react-intersection-observer"
import { FiLayout, FiServer, FiDatabase, FiTool } from "react-icons/fi"

const categories = [
  {
    icon: <FiLayout />, title: "Frontend", color: "text-blue-400", bg: "bg-blue-400/10",
    skills: [
      { name: "React",       level: 90 },
      { name: "TypeScript",  level: 80 },
      { name: "Tailwind CSS",level: 92 },
      { name: "Next.js",     level: 78 },
      { name: "Framer Motion",level: 75 },
    ],
  },
  {
    icon: <FiServer />, title: "Backend", color: "text-green-400", bg: "bg-green-400/10",
    skills: [
      { name: "Node.js",    level: 88 },
      { name: "Express.js", level: 85 },
      { name: "REST APIs",  level: 90 },
      { name: "Python",     level: 72 },
      { name: "WebSockets", level: 65 },
    ],
  },
  {
    icon: <FiDatabase />, title: "Database", color: "text-yellow-400", bg: "bg-yellow-400/10",
    skills: [
      { name: "MongoDB",   level: 85 },
      { name: "PostgreSQL",level: 75 },
      { name: "Redis",     level: 60 },
      { name: "Prisma",    level: 70 },
      { name: "Firebase",  level: 78 },
    ],
  },
  {
    icon: <FiTool />, title: "Tools & DevOps", color: "text-purple-400", bg: "bg-purple-400/10",
    skills: [
      { name: "Git / GitHub",  level: 90 },
      { name: "Docker",        level: 68 },
      { name: "Vercel / Netlify", level: 88 },
      { name: "Linux",         level: 72 },
      { name: "Postman",       level: 85 },
    ],
  },
]

export default function Skills() {
  const [ref, inView] = useInView({ threshold: 0.05, triggerOnce: true })

  return (
    <section id="skills" className="section-pad bg-surface/30" ref={ref}>
      <div className="max-w-6xl mx-auto px-6">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={inView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <span className="text-primary text-sm font-semibold tracking-widest uppercase">Skills</span>
          <h2 className="text-4xl md:text-5xl font-bold mt-3">Tech Stack</h2>
        </motion.div>

        <div className="grid md:grid-cols-2 gap-8">
          {categories.map((cat, ci) => (
            <motion.div key={ci}
              initial={{ opacity: 0, y: 30 }}
              animate={inView ? { opacity: 1, y: 0 } : {}}
              transition={{ duration: 0.6, delay: ci * 0.1 }}
              className="glass rounded-2xl p-8 card-hover"
            >
              <div className="flex items-center gap-3 mb-6">
                <div className={`w-10 h-10 ${cat.bg} rounded-xl flex items-center justify-center ${cat.color} text-lg`}>{cat.icon}</div>
                <h3 className="text-lg font-semibold">{cat.title}</h3>
              </div>
              <div className="space-y-4">
                {cat.skills.map((sk, si) => (
                  <div key={si}>
                    <div className="flex justify-between text-sm mb-1">
                      <span className="text-gray-300">{sk.name}</span>
                      <span className={cat.color}>{sk.level}%</span>
                    </div>
                    <div className="h-1.5 bg-white/5 rounded-full overflow-hidden">
                      <motion.div
                        className={`h-full rounded-full bg-gradient-to-r from-primary to-accent`}
                        initial={{ width: 0 }}
                        animate={inView ? { width: `${sk.level}%` } : {}}
                        transition={{ duration: 0.8, delay: ci * 0.1 + si * 0.07 }}
                      />
                    </div>
                  </div>
                ))}
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}
''')

# Projects
write(f'{base}/frontend/src/components/Projects.jsx', '''import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { useInView } from "react-intersection-observer"
import { FiGithub, FiExternalLink } from "react-icons/fi"

const projects = [
  {
    title: "ScaleChat — Real-time Messaging",
    desc: "A high-performance chat platform supporting 10k+ concurrent users. Built with Socket.io, Redis pub/sub, and horizontal scaling via Docker Swarm.",
    tech: ["React", "Node.js", "Socket.io", "Redis", "MongoDB", "Docker"],
    github: "#", live: "#",
    color: "from-blue-500/20 to-primary/10",
    tag: "Full Stack",
  },
  {
    title: "DevFlow — GitHub Analytics",
    desc: "A developer productivity dashboard aggregating GitHub data into visual insights. REST API with caching layer, deployed on Vercel Edge.",
    tech: ["Next.js", "TypeScript", "GitHub API", "Tailwind", "Chart.js"],
    github: "#", live: "#",
    color: "from-purple-500/20 to-pink-500/10",
    tag: "Frontend",
  },
  {
    title: "ShopX — E-commerce Platform",
    desc: "A production-grade e-commerce API with payment integration, inventory management, and a React storefront. Stripe + Razorpay support.",
    tech: ["React", "Express", "PostgreSQL", "Prisma", "Stripe", "Redux"],
    github: "#", live: "#",
    color: "from-green-500/20 to-emerald-500/10",
    tag: "Full Stack",
  },
  {
    title: "AuthKit — Auth Microservice",
    desc: "A plug-and-play authentication microservice. JWT + refresh tokens, OAuth2 (Google, GitHub), rate limiting, and detailed audit logs.",
    tech: ["Node.js", "Express", "JWT", "Redis", "PostgreSQL", "OAuth2"],
    github: "#", live: "#",
    color: "from-orange-500/20 to-yellow-500/10",
    tag: "Backend",
  },
  {
    title: "NoteMind — AI Notes App",
    desc: "An AI-powered note-taking app with semantic search, auto-tagging, and smart summaries powered by OpenAI API.",
    tech: ["React", "Node.js", "OpenAI", "MongoDB", "Tailwind"],
    github: "#", live: "#",
    color: "from-cyan-500/20 to-blue-500/10",
    tag: "AI / ML",
  },
  {
    title: "TaskFlow — Project Manager",
    desc: "A Jira-inspired project management tool with drag-and-drop boards, team collaboration, and sprint analytics.",
    tech: ["React", "TypeScript", "Express", "MongoDB", "dnd-kit"],
    github: "#", live: "#",
    color: "from-red-500/20 to-pink-500/10",
    tag: "Full Stack",
  },
]

const tags = ["All", "Full Stack", "Frontend", "Backend", "AI / ML"]

export default function Projects() {
  const [active, setActive] = useState("All")
  const [ref, inView] = useInView({ threshold: 0.05, triggerOnce: true })
  const filtered = active === "All" ? projects : projects.filter(p => p.tag === active)

  return (
    <section id="projects" className="section-pad" ref={ref}>
      <div className="max-w-6xl mx-auto px-6">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={inView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.6 }}
          className="text-center mb-12"
        >
          <span className="text-primary text-sm font-semibold tracking-widest uppercase">Portfolio</span>
          <h2 className="text-4xl md:text-5xl font-bold mt-3">Projects</h2>
        </motion.div>

        {/* Filter tabs */}
        <div className="flex flex-wrap justify-center gap-3 mb-12">
          {tags.map(t => (
            <motion.button key={t} onClick={() => setActive(t)}
              whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.97 }}
              className={`px-5 py-2 rounded-full text-sm font-medium transition-all ${
                active === t
                  ? "bg-primary text-white shadow-lg shadow-primary/25"
                  : "glass text-gray-400 hover:text-white"
              }`}
            >{t}</motion.button>
          ))}
        </div>

        <AnimatePresence mode="popLayout">
          <motion.div layout className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filtered.map((p, i) => (
              <motion.div key={p.title}
                layout
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.9 }}
                transition={{ duration: 0.3, delay: i * 0.05 }}
                whileHover={{ y: -6 }}
                className="glass rounded-2xl p-6 flex flex-col card-hover group"
              >
                <div className={`h-2 rounded-full bg-gradient-to-r ${p.color} mb-6`} />
                <div className="flex items-start justify-between mb-3">
                  <span className="text-xs px-2.5 py-1 rounded-full glass text-primary">{p.tag}</span>
                  <div className="flex gap-2">
                    <a href={p.github} target="_blank" rel="noreferrer"
                      className="text-gray-500 hover:text-white transition-colors"><FiGithub /></a>
                    <a href={p.live} target="_blank" rel="noreferrer"
                      className="text-gray-500 hover:text-primary transition-colors"><FiExternalLink /></a>
                  </div>
                </div>
                <h3 className="text-lg font-semibold mb-3 group-hover:text-primary transition-colors">{p.title}</h3>
                <p className="text-gray-400 text-sm leading-relaxed mb-6 flex-1">{p.desc}</p>
                <div className="flex flex-wrap gap-2">
                  {p.tech.map(t => (
                    <span key={t} className="text-xs px-2.5 py-1 rounded-md bg-white/5 text-gray-400">{t}</span>
                  ))}
                </div>
              </motion.div>
            ))}
          </motion.div>
        </AnimatePresence>
      </div>
    </section>
  )
}
''')

# Experience
write(f'{base}/frontend/src/components/Experience.jsx', '''import { motion } from "framer-motion"
import { useInView } from "react-intersection-observer"
import { FiBriefcase, FiBook } from "react-icons/fi"

const work = [
  {
    role: "Full Stack Developer Intern",
    org:  "TechStartup Co.",
    period: "Jun 2024 – Present",
    desc: [
      "Built REST APIs serving 50k+ requests/day using Node.js and Express.",
      "Reduced page load by 40% through code-splitting and lazy loading in React.",
      "Integrated Razorpay payment gateway — handled INR 5M+ in transactions.",
    ],
  },
  {
    role: "Open Source Contributor",
    org:  "Various GitHub Projects",
    period: "2023 – Present",
    desc: [
      "40+ merged PRs across React, Node.js, and documentation projects.",
      "Maintained a CLI tool with 200+ GitHub stars.",
    ],
  },
  {
    role: "Freelance Developer",
    org:  "Self-employed",
    period: "2022 – Present",
    desc: [
      "Delivered 10+ projects for clients across India and USA.",
      "Full lifecycle: scoping, design, development, deployment, and support.",
    ],
  },
]

const edu = [
  {
    degree: "B.Tech — Computer Science & Engineering",
    org:    "NIET, Greater Noida",
    period: "2021 – 2025",
    desc:   ["CGPA: 8.2 / 10", "Core CS, DSA, OS, DBMS, Networks"],
  },
  {
    degree: "Higher Secondary (Class XII)",
    org:    "CBSE Board",
    period: "2021",
    desc:   ["Science with Computer Science — 92%"],
  },
]

function TimelineItem({ item, icon, i, inView }) {
  return (
    <motion.div
      initial={{ opacity: 0, x: -30 }}
      animate={inView ? { opacity: 1, x: 0 } : {}}
      transition={{ duration: 0.5, delay: i * 0.1 }}
      className="flex gap-4"
    >
      <div className="flex flex-col items-center">
        <div className="w-10 h-10 glass rounded-xl flex items-center justify-center text-primary shrink-0">{icon}</div>
        {true && <div className="w-px flex-1 bg-border mt-2" />}
      </div>
      <div className="glass rounded-2xl p-6 mb-6 flex-1 card-hover">
        <div className="flex items-start justify-between flex-wrap gap-2 mb-2">
          <h3 className="font-semibold text-white">{item.role || item.degree}</h3>
          <span className="text-xs text-primary glass px-3 py-1 rounded-full">{item.period}</span>
        </div>
        <p className="text-gray-400 text-sm mb-3">{item.org}</p>
        <ul className="space-y-1">
          {item.desc.map((d, di) => (
            <li key={di} className="text-gray-400 text-sm flex gap-2">
              <span className="text-primary mt-1">▹</span> {d}
            </li>
          ))}
        </ul>
      </div>
    </motion.div>
  )
}

export default function Experience() {
  const [ref, inView] = useInView({ threshold: 0.05, triggerOnce: true })

  return (
    <section id="experience" className="section-pad bg-surface/30" ref={ref}>
      <div className="max-w-6xl mx-auto px-6">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={inView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <span className="text-primary text-sm font-semibold tracking-widest uppercase">Journey</span>
          <h2 className="text-4xl md:text-5xl font-bold mt-3">Experience & Education</h2>
        </motion.div>

        <div className="grid lg:grid-cols-2 gap-12">
          <div>
            <h3 className="text-xl font-semibold mb-8 flex items-center gap-2">
              <FiBriefcase className="text-primary" /> Work Experience
            </h3>
            {work.map((w, i) => <TimelineItem key={i} item={w} icon={<FiBriefcase size={16}/>} i={i} inView={inView} />)}
          </div>
          <div>
            <h3 className="text-xl font-semibold mb-8 flex items-center gap-2">
              <FiBook className="text-primary" /> Education
            </h3>
            {edu.map((e, i) => <TimelineItem key={i} item={e} icon={<FiBook size={16}/>} i={i} inView={inView} />)}
          </div>
        </div>
      </div>
    </section>
  )
}
''')

# Contact
write(f'{base}/frontend/src/components/Contact.jsx', '''import { useState } from "react"
import { motion } from "framer-motion"
import { useInView } from "react-intersection-observer"
import { FiMail, FiMapPin, FiSend, FiLinkedin, FiGithub } from "react-icons/fi"
import axios from "axios"
import toast from "react-hot-toast"

const API = import.meta.env.VITE_API_URL || "http://localhost:5000"

export default function Contact() {
  const [ref, inView] = useInView({ threshold: 0.1, triggerOnce: true })
  const [form, setForm] = useState({ name: "", email: "", subject: "", message: "" })
  const [loading, setLoading] = useState(false)

  const handle = e => setForm({ ...form, [e.target.name]: e.target.value })

  const submit = async e => {
    e.preventDefault()
    if (!form.name || !form.email || !form.message) {
      toast.error("Please fill in all required fields.")
      return
    }
    setLoading(true)
    try {
      await axios.post(`${API}/api/contact`, form)
      toast.success("Message sent! I\'ll reply within 24 hours. 🚀")
      setForm({ name: "", email: "", subject: "", message: "" })
    } catch {
      toast.error("Something went wrong. Try emailing me directly.")
    } finally {
      setLoading(false)
    }
  }

  const info = [
    { icon: <FiMail />,   label: "Email",    val: "0221cseh048@niet.co.in" },
    { icon: <FiMapPin />, label: "Location",  val: "Noida, Uttar Pradesh, India" },
    { icon: <FiLinkedin />,label:"LinkedIn",  val: "linkedin.com/in/alphaxcoder" },
    { icon: <FiGithub />, label: "GitHub",   val: "github.com/alphaxcoder" },
  ]

  const inputClass = "w-full bg-white/5 border border-border rounded-xl px-4 py-3.5 text-white placeholder-gray-500 focus:outline-none focus:border-primary/60 transition-colors text-sm"

  return (
    <section id="contact" className="section-pad" ref={ref}>
      <div className="max-w-6xl mx-auto px-6">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={inView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <span className="text-primary text-sm font-semibold tracking-widest uppercase">Contact</span>
          <h2 className="text-4xl md:text-5xl font-bold mt-3">Let\'s Connect</h2>
          <p className="text-gray-400 mt-4 max-w-xl mx-auto">Open for freelance projects, full-time roles, or a coffee chat. Drop a message!</p>
        </motion.div>

        <div className="grid lg:grid-cols-5 gap-12">
          {/* Info */}
          <motion.div
            initial={{ opacity: 0, x: -30 }}
            animate={inView ? { opacity: 1, x: 0 } : {}}
            transition={{ duration: 0.7, delay: 0.2 }}
            className="lg:col-span-2 space-y-6"
          >
            {info.map((item, i) => (
              <div key={i} className="flex items-start gap-4">
                <div className="w-11 h-11 bg-primary/10 rounded-xl flex items-center justify-center text-primary shrink-0">{item.icon}</div>
                <div>
                  <p className="text-xs text-gray-500 uppercase tracking-wider mb-1">{item.label}</p>
                  <p className="text-gray-300 text-sm">{item.val}</p>
                </div>
              </div>
            ))}

            <div className="pt-4">
              <div className="glass rounded-2xl p-6 text-center glow">
                <div className="w-3 h-3 rounded-full bg-green-400 animate-pulse mx-auto mb-3" />
                <p className="text-sm text-gray-400">Available for new projects</p>
                <p className="text-white font-semibold mt-1">Usually reply within 24h</p>
              </div>
            </div>
          </motion.div>

          {/* Form */}
          <motion.form
            onSubmit={submit}
            initial={{ opacity: 0, x: 30 }}
            animate={inView ? { opacity: 1, x: 0 } : {}}
            transition={{ duration: 0.7, delay: 0.3 }}
            className="lg:col-span-3 glass rounded-2xl p-8 space-y-5"
          >
            <div className="grid sm:grid-cols-2 gap-5">
              <div>
                <label className="text-xs text-gray-500 uppercase tracking-wider mb-1.5 block">Name *</label>
                <input name="name" value={form.name} onChange={handle} className={inputClass} placeholder="Your name" />
              </div>
              <div>
                <label className="text-xs text-gray-500 uppercase tracking-wider mb-1.5 block">Email *</label>
                <input name="email" type="email" value={form.email} onChange={handle} className={inputClass} placeholder="you@example.com" />
              </div>
            </div>
            <div>
              <label className="text-xs text-gray-500 uppercase tracking-wider mb-1.5 block">Subject</label>
              <input name="subject" value={form.subject} onChange={handle} className={inputClass} placeholder="What\'s this about?" />
            </div>
            <div>
              <label className="text-xs text-gray-500 uppercase tracking-wider mb-1.5 block">Message *</label>
              <textarea name="message" value={form.message} onChange={handle} rows={6} className={`${inputClass} resize-none`} placeholder="Tell me about your project or idea..." />
            </div>
            <motion.button
              type="submit" disabled={loading}
              whileHover={{ scale: 1.02, boxShadow: "0 0 30px rgba(39,131,222,0.4)" }}
              whileTap={{ scale: 0.98 }}
              className="w-full py-4 bg-primary text-white font-semibold rounded-xl flex items-center justify-center gap-2 transition-all disabled:opacity-60 disabled:cursor-not-allowed"
            >
              {loading ? (
                <><span className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" /> Sending...</>
              ) : (
                <><FiSend /> Send Message</>
              )}
            </motion.button>
          </motion.form>
        </div>
      </div>
    </section>
  )
}
''')

# Footer
write(f'{base}/frontend/src/components/Footer.jsx', '''import { motion } from "framer-motion"
import { FiGithub, FiLinkedin, FiTwitter, FiHeart } from "react-icons/fi"
import { Link } from "react-scroll"

const nav  = ["About","Skills","Projects","Experience","Contact"]
const socs = [
  { icon: <FiGithub />,   href: "https://github.com/alphaxcoder" },
  { icon: <FiLinkedin />, href: "https://linkedin.com/in/alphaxcoder" },
  { icon: <FiTwitter />,  href: "https://twitter.com/alphaxcoder" },
]

export default function Footer() {
  return (
    <footer className="border-t border-border py-12">
      <div className="max-w-6xl mx-auto px-6">
        <div className="flex flex-col md:flex-row items-center justify-between gap-6">
          <span className="text-xl font-bold gradient-text">&lt;Alphaxcoder /&gt;</span>
          <ul className="flex gap-6">
            {nav.map(l => (
              <li key={l}>
                <Link to={l.toLowerCase()} smooth duration={600} offset={-70}
                  className="text-sm text-gray-500 hover:text-white transition-colors cursor-pointer"
                >{l}</Link>
              </li>
            ))}
          </ul>
          <div className="flex gap-3">
            {socs.map((s, i) => (
              <motion.a key={i} href={s.href} target="_blank" rel="noreferrer"
                whileHover={{ scale: 1.2 }}
                className="w-9 h-9 glass rounded-full flex items-center justify-center text-gray-400 hover:text-primary transition-colors text-sm"
              >{s.icon}</motion.a>
            ))}
          </div>
        </div>
        <div className="mt-8 pt-8 border-t border-border text-center text-gray-500 text-sm">
          Made with <FiHeart className="inline text-red-400 mx-1" /> by Alphaxcoder &nbsp;·&nbsp; {new Date().getFullYear()}
        </div>
      </div>
    </footer>
  )
}
''')

# Vercel config for frontend
write(f'{base}/frontend/vercel.json', '''{
  "rewrites": [{"source": "/(.*)", "destination": "/index.html"}]
}
''')

# .env.example frontend
write(f'{base}/frontend/.env.example', '''VITE_API_URL=https://your-backend-url.onrender.com
''')

# ─── BACKEND ───────────────────────────────────────────────────────────────────

write(f'{base}/backend/package.json', '''{
  "name": "portfolio-backend",
  "version": "1.0.0",
  "description": "Portfolio contact form backend",
  "main": "src/index.js",
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "dotenv": "^16.4.1",
    "express": "^4.18.2",
    "express-rate-limit": "^7.2.0",
    "express-validator": "^7.0.1",
    "helmet": "^7.1.0",
    "morgan": "^1.10.0",
    "nodemailer": "^6.9.9"
  },
  "devDependencies": {
    "nodemon": "^3.0.3"
  },
  "engines": { "node": ">=18.0.0" }
}
''')

write(f'{base}/backend/src/index.js', '''require("dotenv").config()
const express  = require("express")
const cors     = require("cors")
const helmet   = require("helmet")
const morgan   = require("morgan")
const contactRouter = require("./routes/contact")

const app  = express()
const PORT = process.env.PORT || 5000

// ── Security & middleware ──
app.use(helmet())
app.use(morgan("combined"))
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS
    ? process.env.ALLOWED_ORIGINS.split(",")
    : ["http://localhost:3000"],
  methods: ["GET", "POST"],
  allowedHeaders: ["Content-Type"],
}))
app.use(express.json({ limit: "10kb" }))
app.use(express.urlencoded({ extended: true, limit: "10kb" }))

// ── Routes ──
app.get("/health", (_req, res) => res.json({ status: "ok", ts: Date.now() }))
app.use("/api/contact", contactRouter)

// ── 404 ──
app.use((_req, res) => res.status(404).json({ error: "Not found" }))

// ── Global error handler ──
app.use((err, _req, res, _next) => {
  console.error(err.stack)
  res.status(500).json({ error: "Internal server error" })
})

app.listen(PORT, () => console.log(`🚀 Backend running on port ${PORT}`))
''')

write(f'{base}/backend/src/routes/contact.js', '''const router = require("express").Router()
const rateLimit = require("express-rate-limit")
const { body, validationResult } = require("express-validator")
const { sendContactEmail } = require("../controllers/contact.controller")

// 5 requests per 15 min per IP
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  message: { error: "Too many requests — please try again in 15 minutes." },
  standardHeaders: true,
  legacyHeaders: false,
})

const validate = [
  body("name").trim().notEmpty().withMessage("Name is required").isLength({ max: 100 }),
  body("email").trim().isEmail().withMessage("Valid email is required").normalizeEmail(),
  body("subject").trim().optional().isLength({ max: 200 }),
  body("message").trim().notEmpty().withMessage("Message is required").isLength({ min: 10, max: 5000 }),
]

router.post("/", limiter, validate, async (req, res) => {
  const errors = validationResult(req)
  if (!errors.isEmpty())
    return res.status(422).json({ errors: errors.array() })
  await sendContactEmail(req, res)
})

module.exports = router
''')

write(f'{base}/backend/src/controllers/contact.controller.js', '''const nodemailer = require("nodemailer")

const createTransporter = () =>
  nodemailer.createTransport({
    service: "gmail",
    auth: {
      user: process.env.GMAIL_USER,
      pass: process.env.GMAIL_APP_PASSWORD,  // Gmail App Password (not your real password)
    },
  })

exports.sendContactEmail = async (req, res) => {
  const { name, email, subject, message } = req.body
  try {
    const transporter = createTransporter()

    // ── Email TO you ──
    await transporter.sendMail({
      from: `"Portfolio Contact" <${process.env.GMAIL_USER}>`,
      to:   process.env.CONTACT_EMAIL || process.env.GMAIL_USER,
      replyTo: email,
      subject: `[Portfolio] ${subject || `New message from ${name}`}`,
      html: `
        <div style="font-family:Inter,Arial,sans-serif;max-width:600px;margin:auto;background:#0d0d0d;color:#fff;border-radius:16px;overflow:hidden;">
          <div style="background:linear-gradient(135deg,#2783DE,#5E9FE8);padding:32px;">
            <h2 style="margin:0;font-size:24px;">New Contact Form Submission</h2>
          </div>
          <div style="padding:32px;">
            <table style="width:100%;border-collapse:collapse;">
              <tr><td style="padding:8px 0;color:#aaa;width:100px;">From</td>
                  <td style="padding:8px 0;font-weight:600;">${name}</td></tr>
              <tr><td style="padding:8px 0;color:#aaa;">Email</td>
                  <td style="padding:8px 0;"><a href="mailto:${email}" style="color:#2783DE;">${email}</a></td></tr>
              <tr><td style="padding:8px 0;color:#aaa;">Subject</td>
                  <td style="padding:8px 0;">${subject || "—"}</td></tr>
            </table>
            <hr style="border:none;border-top:1px solid #222;margin:24px 0;" />
            <p style="color:#aaa;font-size:13px;margin-bottom:8px;">MESSAGE</p>
            <p style="background:#1a1a1a;border-radius:8px;padding:20px;line-height:1.7;">${message.replace(/\n/g, "<br/>")}</p>
            <p style="color:#555;font-size:12px;margin-top:24px;">Sent at ${new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" })} IST</p>
          </div>
        </div>
      `,
    })

    // ── Auto-reply to sender ──
    await transporter.sendMail({
      from: `"Alphaxcoder" <${process.env.GMAIL_USER}>`,
      to:   email,
      subject: `Got your message, ${name}! 👋`,
      html: `
        <div style="font-family:Inter,Arial,sans-serif;max-width:600px;margin:auto;background:#0d0d0d;color:#fff;border-radius:16px;overflow:hidden;">
          <div style="background:linear-gradient(135deg,#2783DE,#5E9FE8);padding:32px;">
            <h2 style="margin:0;">Thanks for reaching out! 🚀</h2>
          </div>
          <div style="padding:32px;">
            <p style="line-height:1.8;">Hi <strong>${name}</strong>,</p>
            <p style="line-height:1.8;color:#aaa;">I\'ve received your message and will get back to you within 24 hours. In the meantime, feel free to connect with me on <a href="https://linkedin.com/in/alphaxcoder" style="color:#2783DE;">LinkedIn</a> or check out my <a href="https://github.com/alphaxcoder" style="color:#2783DE;">GitHub</a>.</p>
            <p style="color:#aaa;margin-top:24px;">— Alphaxcoder</p>
          </div>
        </div>
      `,
    })

    res.status(200).json({ success: true, message: "Email sent successfully!" })
  } catch (err) {
    console.error("Email error:", err)
    res.status(500).json({ error: "Failed to send email. Please try again." })
  }
}
''')

write(f'{base}/backend/.env.example', '''PORT=5000

# Your Gmail address
GMAIL_USER=your_email@gmail.com

# Gmail App Password (Settings > Security > 2FA > App Passwords)
GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx

# Where contact form emails land (usually same as GMAIL_USER)
CONTACT_EMAIL=your_email@gmail.com

# Comma-separated list of allowed frontend origins
ALLOWED_ORIGINS=https://your-portfolio.vercel.app,http://localhost:3000
''')

write(f'{base}/backend/.gitignore', '''.env
node_modules/
*.log
''')

# Render deploy config
write(f'{base}/backend/render.yaml', '''services:
  - type: web
    name: portfolio-backend
    runtime: node
    buildCommand: npm install
    startCommand: npm start
    envVars:
      - key: PORT
        value: 5000
      - key: GMAIL_USER
        sync: false
      - key: GMAIL_APP_PASSWORD
        sync: false
      - key: CONTACT_EMAIL
        sync: false
      - key: ALLOWED_ORIGINS
        sync: false
''')

# Root README
write(f'{base}/README.md', '''# 🚀 Alphaxcoder Portfolio

A production-ready, full-stack portfolio with a React frontend and Express backend contact form.

## 🗂️ Directory Structure

```
portfolio/
├── frontend/                 ← React + Vite + Tailwind
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx    ← Sticky nav with mobile menu
│   │   │   ├── Hero.jsx      ← Animated hero + type animation
│   │   │   ├── About.jsx     ← Stats + traits grid
│   │   │   ├── Skills.jsx    ← Animated progress bars
│   │   │   ├── Projects.jsx  ← Filterable project cards
│   │   │   ├── Experience.jsx← Timeline (work + education)
│   │   │   ├── Contact.jsx   ← Form → hits backend API
│   │   │   └── Footer.jsx
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css         ← Tailwind + custom utilities
│   ├── vercel.json           ← Vercel SPA routing fix
│   ├── .env.example          ← VITE_API_URL
│   ├── tailwind.config.js
│   ├── vite.config.js
│   └── package.json
│
├── backend/                  ← Node.js + Express
│   ├── src/
│   │   ├── routes/
│   │   │   └── contact.js    ← POST /api/contact (rate-limited + validated)
│   │   ├── controllers/
│   │   │   └── contact.controller.js ← Nodemailer (notify you + auto-reply)
│   │   └── index.js          ← Express app (CORS, Helmet, Morgan)
│   ├── render.yaml           ← One-click Render.com deploy
│   ├── .env.example
│   └── package.json
│
└── README.md
```

## ⚡ Quick Start (Local)

### Backend
```bash
cd backend
npm install
cp .env.example .env        # Fill in Gmail credentials
npm run dev                 # Runs on :5000
```

### Frontend
```bash
cd frontend
npm install
cp .env.example .env.local  # Set VITE_API_URL=http://localhost:5000
npm run dev                 # Runs on :3000
```

## 🌐 Deploy to Production

### 1. Deploy Backend → Render.com (Free)
1. Push to GitHub
2. Go to **render.com** → New Web Service → connect repo
3. Root Directory: `backend`
4. Set env vars from `.env.example`
5. Deploy — get your URL: `https://portfolio-backend.onrender.com`

### 2. Deploy Frontend → Vercel (Free)
1. Go to **vercel.com** → Import project
2. Root Directory: `frontend`
3. Add env var: `VITE_API_URL=https://portfolio-backend.onrender.com`
4. Deploy → live in ~60 seconds!

## 📧 Gmail Setup (for contact form)
1. Enable 2-Factor Authentication on your Google account
2. Go to **Google Account → Security → App Passwords**
3. Create an App Password for "Mail"
4. Paste it into `GMAIL_APP_PASSWORD` in your `.env`

## 🛡️ Security Features
- Rate limiting (5 req / 15 min per IP)
- Input validation & sanitization
- CORS whitelist
- Helmet HTTP headers
- Body size limits (10KB)

## 🎨 Customization
- Edit `frontend/src/components/` to update content
- Replace project data in `Projects.jsx`
- Update socials/links in `Navbar.jsx` and `Hero.jsx`
- Colors in `tailwind.config.js`
''')

# Root gitignore
write(f'{base}/.gitignore', '''node_modules/
dist/
.env
.env.local
*.log
.DS_Store
''')

print("\n✅ All files created successfully!")
