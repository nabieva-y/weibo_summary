import yagmail
import os

def send_email(contents, subject="微博周报"):
    yag = yagmail.SMTP(
        user=os.getenv("EMAIL_USER"),
        password=os.getenv("EMAIL_PASSWORD"),
        host="smtp.qq.com",  # 如果你用 QQ 邮箱
        port=465,
        smtp_ssl=True
    )
    to = os.getenv("EMAIL_RECEIVER")
    to2 = os.getenv("EMAIL_RECEIVER2")
    yag.send(to=to, subject=subject, contents=contents)
    yag.send(to=to2, subject=subject, contents=contents)
