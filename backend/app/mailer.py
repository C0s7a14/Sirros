import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")
SMTP_FROM = os.environ.get("SMTP_FROM", SMTP_USER)


def send_welcome_email(to_email: str, password: str) -> None:
    if not SMTP_USER or not SMTP_PASSWORD:
        print(f"[MAILER] SMTP not configured — skipping welcome email to {to_email}")
        return

    subject = "Bem-vindo ao Sirros — suas credenciais de acesso"
    html = f"""
    <div style="font-family: Raleway, Arial, sans-serif; max-width: 480px; margin: 0 auto; color: #333;">
      <div style="background: #091f33; padding: 32px 24px; border-radius: 12px 12px 0 0;">
        <h1 style="color: #fff; margin: 0; font-size: 24px; font-weight: 800;">Sirros</h1>
      </div>
      <div style="background: #fff; padding: 32px 24px; border-radius: 0 0 12px 12px;
                  box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <h2 style="color: #091f33; font-size: 18px; margin-top: 0;">Conta criada com sucesso!</h2>
        <p style="color: #797979; font-size: 14px; line-height: 1.6;">
          Use as credenciais abaixo para acessar a plataforma:
        </p>
        <div style="background: rgba(48,168,242,0.08); border: 1px solid #30a8f2;
                    border-radius: 12px; padding: 16px 20px; margin: 20px 0;">
          <p style="margin: 0 0 8px; font-size: 13px; color: #797979;">E-mail</p>
          <p style="margin: 0 0 16px; font-size: 15px; font-weight: 600; color: #091f33;">{to_email}</p>
          <p style="margin: 0 0 8px; font-size: 13px; color: #797979;">Senha</p>
          <p style="margin: 0; font-size: 15px; font-weight: 600; color: #091f33;">{password}</p>
        </div>
        <a href="https://sirros-frontend.vercel.app/login"
           style="display: block; background: #30a8f2; color: #fff; text-align: center;
                  padding: 12px; border-radius: 8px; text-decoration: none;
                  font-weight: 700; font-size: 14px;">
          Acessar plataforma
        </a>
        <p style="color: #797979; font-size: 12px; margin-top: 20px; margin-bottom: 0;">
          Por segurança, recomendamos alterar sua senha após o primeiro acesso.
        </p>
      </div>
    </div>
    """

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SMTP_FROM
    msg["To"] = to_email
    msg.attach(MIMEText(html, "html", "utf-8"))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_FROM, [to_email], msg.as_string())
        print(f"[MAILER] Welcome email sent to {to_email}")
    except Exception as exc:
        print(f"[MAILER] Failed to send email to {to_email}: {exc}")
