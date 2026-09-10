import { motion } from "framer-motion"
import { useInView } from "react-intersection-observer"
import { FiLayout, FiServer, FiDatabase, FiTool } from "react-icons/fi"

const categories = [
  {
    icon: <FiLayout />, title: "Frontend", color: "text-blue-400", bg: "bg-blue-400/10",
    skills: [
      { name: "React",       level: 75 },
      { name: "TypeScript",  level: 60 },
      { name: "Tailwind CSS",level: 75 },
      { name: "Next.js",     level: 65 }, 
      { name: "HTML/CSS",     level: 85 },
    ],
  },
  {
    icon: <FiServer />, title: "Backend", color: "text-green-400", bg: "bg-green-400/10",
    skills: [
      { name: "Node.js",    level: 80 },
      { name: "Express.js", level: 65 },
      { name: "REST APIs",  level: 70 },
      { name: "Python",     level: 75 }, 
      { name: "Java",     level: 75 },
    ],
  },
  {
    icon: <FiDatabase />, title: "Database", color: "text-yellow-400", bg: "bg-yellow-400/10",
    skills: [
      { name: "MongoDB",   level: 85 },
      { name: "PostgreSQL",level: 75 }, 
      { name: "Firebase",  level: 78 },
    ],
  },
  {
    icon: <FiTool />, title: "Tools & DevOps", color: "text-purple-400", bg: "bg-purple-400/10",
    skills: [
      { name: "Git / GitHub",  level: 75 },
      { name: "Docker",        level: 68 },
      { name: "Vercel / Netlify", level: 80 },
      { name: "Linux",         level: 65 },
      { name: "Postman",       level: 70 },
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
