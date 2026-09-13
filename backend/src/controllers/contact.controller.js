const { Resend } = require("resend")

const resend = new Resend(process.env.RESEND_API_KEY)

exports.sendContactEmail = async (req, res) => {
  const { name, email, subject, message } = req.body
  try {

    // ── Email TO you ──
    await resend.emails.send({
      from: "Portfolio Contact <onboarding@resend.dev>",
      to: process.env.CONTACT_EMAIL,
      replyTo: email,
      subject: `[Portfolio] ${subject || `New message from ${name}`}`,
      html: `
        <div style="font-family:Inter,Arial,sans-serif;max-width:600px;margin:auto;background:#0d0d0d;color:#fff;border-radius:16px;overflow:hidden;">
          <div style="background:linear-gradient(135deg,#2783DE,#5E9FE8);padding:32px;">
            <h2 style="margin:0;font-size:24px;">New Contact Form Submission</h2>
          </div>
          <div style="padding:32px;">
            <table style="width:100%;border-collapse:collapse;">
              <tr><td style="padding:8px 0;color:#aaa;width:100px;">From</td>
                  <td style="padding:8px 0;font-weight:600;">${name}</td></tr>
              <tr><td style="padding:8px 0;color:#aaa;">Email</td>
                  <td style="padding:8px 0;"><a href="mailto:${email}" style="color:#2783DE;">${email}</a></td></tr>
              <tr><td style="padding:8px 0;color:#aaa;">Subject</td>
                  <td style="padding:8px 0;">${subject || "—"}</td></tr>
            </table>
            <hr style="border:none;border-top:1px solid #222;margin:24px 0;" />
            <p style="color:#aaa;font-size:13px;margin-bottom:8px;">MESSAGE</p>
            <p style="background:#1a1a1a;border-radius:8px;padding:20px;line-height:1.7;">${message.replace(/\n/g, '<br>')}</p>
            <p style="color:#555;font-size:12px;margin-top:24px;">Sent at ${new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" })} IST</p>
          </div>
        </div>
      `,
    })

    // ── Auto-reply to sender ──
    await resend.emails.send({
      from: "Pawan Gupta <onboarding@resend.dev>",
      to: email,
      subject: `Got your message, ${name}! 👋`,
      html: `
        <div style="font-family:Inter,Arial,sans-serif;max-width:600px;margin:auto;background:#0d0d0d;color:#fff;border-radius:16px;overflow:hidden;">
          <div style="background:linear-gradient(135deg,#2783DE,#5E9FE8);padding:32px;">
            <h2 style="margin:0;">Thanks for reaching out! 🚀</h2>
          </div>
          <div style="padding:32px;">
            <p style="line-height:1.8;">Hi <strong>${name}</strong>,</p>
            <p style="line-height:1.8;color:#aaa;">I've received your message and will get back to you within 24 hours. In the meantime, feel free to connect with me on <a href="https://www.linkedin.com/in/pawan-gupta-739914264" style="color:#2783DE;">LinkedIn</a> or check out my <a href="https://github.com/pawangthb" style="color:#2783DE;">GitHub</a>.</p>
            <p style="color:#aaa;margin-top:24px;">— Pawan Gupta</p>
          </div>
        </div>
      `,
    })

    res.status(200).json({ success: true, message: "Email sent successfully!" })
  } catch (err) {
    console.error("Email error:", err)
    res.status(500).json({ error: "Failed to send email. Please try again." })
  }
}