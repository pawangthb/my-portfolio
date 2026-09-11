import { motion } from "framer-motion"
import { useInView } from "react-intersection-observer"
import { FiBriefcase, FiBook } from "react-icons/fi"

const work = [
  {
  role: "LLM Post AI Intern",
  org:  "Ethara AI",
  period: "Mar 2026 – May 2026",
  desc: [
    "Evaluated and validated AI-generated responses to improve LLM output quality, accuracy, and relevance.",
    "Reviewed prompts and model outputs, identifying inconsistencies, factual errors, and optimization opportunities.",
    "Gained hands-on experience in prompt engineering and AI model quality assurance workflows.",
  ],
},
 {
  role: "Software Development Intern ",
  org:  "Bluestock Fintech",
  period: "Aug 2025 – Sep 2025",
  desc: [
    "Developed 5+ user-facing features for a FinTech platform serving real-time stock data through integrated APIs.",
    "Integrated real-time stock market APIs for live price tracking and portfolio updates.",
    "Worked on a production-grade platform handling live financial data for real users.",
  ],
},
  {
  role: "Web Developer Intern",
  org:  "Bharat Intern",
  period: "Aug 2023",
  desc: [
    "Developed responsive landing pages using HTML5, CSS3, and JavaScript.",
    "Improved cross-browser compatibility and optimized frontend performance.",
    "Gained hands-on experience building real-world web projects in a remote environment.",
  ],
},
]

const edu = [
  {
    degree: "B.Tech — Computer Science & Engineering",
    org:    "NIET, Greater Noida",
    period: "2022 – 2026",
    desc:   ["CGPA: 7.15 / 10", "Core CS, DSA, OS, DBMS, Networks"],
  },
  {
    degree: "Higher Secondary (Class XII)",
    org:    "JDS International School, Gorakhpur, CBSE Board",
    period: "2022",
    desc:   ["PCM with Eng & IT — 70%"],
  },
  {
    degree: "Secondary School(Class X)",
    org:    "JDS International School, Gorakhpur, CBSE Board",
    period: "2020",
    desc:   ["Maths,Science, Social Study, IT — 80%"],
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
