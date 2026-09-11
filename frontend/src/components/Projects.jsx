import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { useInView } from "react-intersection-observer"
import { FiGithub, FiExternalLink } from "react-icons/fi"

const projects = [
  {
    title: "Portfolio | High-Performance Real-Time Communication",
    desc: "Built a responsive messaging application with instant communication, secure authentication, and real-time updates, delivering a seamless user experience with reliable and scalable performance.",
    tech: ["React", "Node.js", "Vite", "MySQL"],
    github: "https://github.com/pawangthb/my-portfolio", live: "#",
    color: "from-blue-500/20 to-primary/10",
    tag: "Full Stack",
  },
  {
    title: "Student Attendance & Analytics Dashboard",
    desc: "A smart attendance management platform featuring role-based access, real-time attendance tracking, insightful analytics, automated records, and an intuitive React dashboard for efficient academic management.",
    tech: ["React", "Express", "MongoDb", "Bootstrap"],
    github: "https://github.com/pawangthb/Student-Attendance-System", live: "#",
    color: "from-green-500/20 to-emerald-500/10",
    tag: "Full Stack",
  },
  {
    title: "Responsive Landing Page",
    desc: "Developed a responsive and visually engaging landing page with modern UI design, optimized layouts, intuitive navigation, and cross-device compatibility to enhance user experience.",
    tech: ["Next.js", "TypeScript", "GitHub API", "Tailwind", "Chart.js"],
    github: "https://github.com/pawangthb/Landing_Page-Codsoft", live: "#",
    color: "from-purple-500/20 to-pink-500/10",
    tag: "Frontend",
  },
  
  {
    title: "Netflix-Inspired Streaming Platform",
    desc: "Developed a responsive streaming platform featuring movie browsing, categorized content, search functionality, interactive UI, user authentication, and seamless navigation across devices",
    tech: ["React", "Express", "JWT", "Bootstrap", "PostgreSQL", "OAuth2"],
    github: "https://github.com/pawangthb/Netflix_homepage/tree/main/TAsk%203%20NF", live: "#",
    color: "from-orange-500/20 to-yellow-500/10",
    tag: "Frontend",
  },
   
  {
    title: "TempX – Smart Temperature Converter ⭐",
    desc: "Built an interactive temperature converter using HTML, CSS, and JavaScript, supporting Celsius, Fahrenheit, and Kelvin conversions with responsive design.",
    tech: ["HTML", "CSS", "JavaScript"],
    github: "https://github.com/pawangthb/Temperature-Conv/tree/main/Task%202%20TC", live: "#",
    color: "from-red-500/20 to-pink-500/10",
    tag: "Frontend",
  },
  {
    title: "HireBuddy – Smart Hiring & Task Platform",
    desc: "Developed a platform connecting users with skilled professionals for real-world tasks, featuring service discovery, task posting, secure authentication, and streamlined hiring workflows.",
    tech: ["React", "Express", "SQLite", "Bootstrap", "JWT"],
    github: "https://github.com/pawangthb/HireBuddy", live: "#",
    color: "from-red-500/20 to-pink-500/10",
    tag: "Backend",
  },
  
]

const tags = ["All", "Full Stack", "Frontend", "Backend"]

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
