import { motion } from "framer-motion"
import { useInView } from "react-intersection-observer"
import { FiCode, FiCoffee, FiHeart, FiTarget } from "react-icons/fi"

const stats = [
  { label: "Projects Built", value: "7+" },
  { label: "Years Coding",   value: "1+" },
  { label: "Technologies",   value: "8+" },
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
              I'm a <span className="text-white font-semibold">Full Stack Developer</span> from Noida,having recently graduated in engineering from NIET. I love crafting products that are not just
              functional but genuinely delightful to use.
            </p>
            <p className="text-gray-400 text-lg leading-relaxed mb-6">
              When I'm not coding, I'm exploring new technologies, contributing to open source,
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
