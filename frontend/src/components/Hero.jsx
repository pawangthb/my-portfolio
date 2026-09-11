import { motion } from "framer-motion"
import { TypeAnimation } from "react-type-animation"
import { Link } from "react-scroll"
import { FiGithub, FiLinkedin, FiArrowDown, FiDownload } from "react-icons/fi"
import { SiLeetcode } from "react-icons/si"

const socials = [
  { icon: <FiGithub />,   href: "https://github.com/pawangthb" },
  { icon: <FiLinkedin />, href: "https://www.linkedin.com/in/pawan-gupta-739914264" },
  { icon: <SiLeetcode  />,  href: "https://leetcode.com/u/pg19062004/" },
]

export default function Hero() {
  return (
    <section id="hero" className="relative min-h-screen flex items-center justify-center overflow-hidden">
       
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-[500px] h-[500px] bg-primary/10 rounded-full blur-[120px] animate-pulse-slow" />
        <div className="absolute bottom-1/4 right-1/4 w-[400px] h-[400px] bg-purple-500/10 rounded-full blur-[100px] animate-pulse-slow" style={{animationDelay:"2s"}} />
        <div className="absolute top-1/2 left-1/2 w-[300px] h-[300px] bg-accent/5 rounded-full blur-[80px] animate-float" />
      </div>
 
      <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,.02)_1px,transparent_1px)] bg-[size:60px_60px] [mask-image:radial-gradient(ellipse_80%_80%_at_50%_50%,#000_40%,transparent_100%)]" />

      <div className="relative z-10 max-w-6xl mx-auto px-6">
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
        > 
          <div className="flex justify-center mb-8">
            <motion.div
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ duration: 0.5 }}
              className="inline-flex items-center gap-2 px-4 py-2 glass rounded-full text-sm text-primary"
            >
              <span className="w-2 h-2 rounded-full bg-green-400 animate-pulse" />
              Available for opportunities
            </motion.div>
          </div>
 
          <div className="flex flex-col-reverse md:flex-row items-center justify-between gap-12">
 
            <div className="flex-1 text-center md:text-left">
              <h1 className="text-5xl md:text-7xl lg:text-8xl font-extrabold leading-tight mb-6">
                Hi, I'm
                <span className="block gradient-text">Pawan Gupta</span>
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

              <p className="max-w-2xl text-gray-400 text-lg leading-relaxed mb-12">
                I build scalable, performant web applications with clean code and intuitive UX.
                Passionate about turning complex problems into elegant solutions.
              </p>
 
              <div className="flex flex-wrap items-center justify-center md:justify-start gap-4 mb-10">
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
                <a href="/Pawan_Resume.pdf" download="Pawan_Gupta_Resume.pdf">
                  <motion.button
                    whileHover={{ scale: 1.05, boxShadow: "0 0 30px rgba(39,131,222,0.2)" }}
                    whileTap={{ scale: 0.97 }}
                    className="px-8 py-4 glass text-white font-semibold rounded-full text-base hover:border-primary/50 transition-all flex items-center gap-2"
                  >
                    <FiDownload className="text-primary" />
                    Download CV
                  </motion.button>
                </a>
              </div>
 
              <div className="flex items-center justify-center md:justify-start gap-4">
                {socials.map((s, i) => (
                  <motion.a key={i} href={s.href} target="_blank" rel="noreferrer"
                    whileHover={{ scale: 1.2, y: -4 }} whileTap={{ scale: 0.9 }}
                    className="w-11 h-11 glass rounded-full flex items-center justify-center text-gray-400 hover:text-primary hover:border-primary/50 transition-all"
                  >
                    {s.icon}
                  </motion.a>
                ))}
              </div>
            </div>
 
            <motion.div
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.8, delay: 0.4 }}
              className="flex-shrink-0"
            >
              <div className="relative w-64 h-64 md:w-80 md:h-80 lg:w-96 lg:h-96">
                 
                <div className="absolute inset-0 rounded-full bg-gradient-to-br from-primary/40 to-purple-500/40 blur-2xl animate-pulse-slow" />
                 
                <div className="absolute inset-0 rounded-full border-2 border-primary/30 animate-spin" style={{ animationDuration: "8s" }} />
                 
               <div className="relative w-full h-full rounded-full overflow-hidden border-2 border-primary/20 glass bg-dark">
                 <img
                    src="/For_Pf.jpeg"
                    alt="Pawan Gupta"
                    className="w-full h-full object-cover object-top"
                    onError={(e) => {
                      e.target.style.display = 'none';
                      e.target.parentNode.innerHTML = `
                        <div class="w-full h-full flex items-center justify-center text-6xl font-bold gradient-text">
                          PG
                        </div>
                      `;
                    }}
                  />
                </div>
              </div>
            </motion.div>

          </div>
        </motion.div>
 
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