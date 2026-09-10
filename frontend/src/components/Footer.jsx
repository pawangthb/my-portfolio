import { motion } from "framer-motion"
import { FiGithub, FiLinkedin, FiTwitter, FiHeart } from "react-icons/fi"
import { Link } from "react-scroll"

const nav  = ["About","Skills","Projects","Experience","Contact"]
const socs = [
  { icon: <FiGithub />,   href: "https://github.com/pawangthb" },
  { icon: <FiLinkedin />, href: "https://www.linkedin.com/in/pawan-gupta-739914264" },
  { icon: <FiTwitter />,  href: "#" },
]

export default function Footer() {
  return (
    <footer className="border-t border-border py-12">
      <div className="max-w-6xl mx-auto px-6">
        <div className="flex flex-col md:flex-row items-center justify-between gap-6">
          <span className="text-xl font-bold gradient-text">&lt;Pawan.Dev /&gt;</span>
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
          Made <FiHeart className="inline text-red-400 mx-1" /> by Pawan &nbsp;·&nbsp; {new Date().getFullYear()}
        </div>
      </div>
    </footer>
  )
}
