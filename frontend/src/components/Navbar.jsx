import { useState, useEffect } from "react"
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
          &lt;Pawan.dev /&gt;
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
