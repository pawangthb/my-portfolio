import { useState } from "react"
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
      toast.success("Message sent! I'll reply within 24 hours. 🚀")
      setForm({ name: "", email: "", subject: "", message: "" })
    } catch {
      toast.error("Something went wrong. Try emailing me directly.")
    } finally {
      setLoading(false)
    }
  }

  const info = [
    { icon: <FiMail />,   label: "Email",    val: "pg19062004@gmail.com" },
    { icon: <FiMapPin />, label: "Location",  val: "Noida, Uttar Pradesh, India" },
    { icon: <FiLinkedin />,label:"LinkedIn",  val: "pawan-gupta-739914264" },
    { icon: <FiGithub />, label: "GitHub",   val: "pawangthb" },
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
          <h2 className="text-4xl md:text-5xl font-bold mt-3">Let's Connect</h2>
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
              <input name="subject" value={form.subject} onChange={handle} className={inputClass} placeholder="What's this about?" />
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
