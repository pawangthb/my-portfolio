require("dotenv").config()
const express  = require("express")
const visitorRoute = require('./routes/visitor');
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
app.use('/api/visitor', visitorRoute);

// ── 404 ──
app.use((_req, res) => res.status(404).json({ error: "Not found" }))

// ── Global error handler ──
app.use((err, _req, res, _next) => {
  console.error(err.stack)
  res.status(500).json({ error: "Internal server error" })
})

app.listen(PORT, () => console.log(`🚀 Backend running on port ${PORT}`))
