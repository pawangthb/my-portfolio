const router = require("express").Router()
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
