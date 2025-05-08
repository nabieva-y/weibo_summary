# import os
# import json
# import openai
# import yagmail
# from datetime import datetime
# from weibo_crawler import WeiboCrawler

# # 设置 OpenAI API 密钥
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # 设置邮箱信息
# EMAIL_USER = os.getenv("EMAIL_USER")
# EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
# EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# # 微博用户 UID
# WEIBO_UID = "1671109627"

# def fetch_weibo_posts(uid):
#     crawler = WeiboCrawler(uid=uid)
#     posts = crawler.get_latest_posts(count=10)
#     return posts

# def summarize_posts(posts):
#     content = "\n\n".join([post['text'] for post in posts])
#     prompt = f"请总结以下微博内容的要点：\n\n{content}"
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     summary = response.choices[0].message.content.strip()
#     return summary 

# def send_email(subject, content):
#     yag = yagmail.SMTP(user=EMAIL_USER, password=EMAIL_PASSWORD)
#     yag.send(to=EMAIL_RECEIVER, subject=subject, contents=content)

# def main():
#     posts = fetch_weibo_posts(WEIBO_UID)
#     summary = summarize_posts(posts)
#     today = datetime.now().strftime("%Y-%m-%d")
#     subject = f"包容万物恒河水 微博摘要 - {today}"
#     send_email(subject, summary)

# if __name__ == "__main__":
#     main()

# weibo_summary_mailer.py
import os

def fake_fetch_weibo():
    return [
        "人生就是一场修行。",
        "万物皆可包容，心若自在天地宽。",
        "恒河水在流，智慧常更新。"
    ]

def summarize(posts):
    return "包容万物恒河水本周发布了 {} 条微博，内容涵盖：修行、包容、哲理等主题。".format(len(posts))

def send_email(summary):
    import yagmail
    user = os.getenv("EMAIL_USER")
    pwd = os.getenv("EMAIL_PASSWORD")
    to = os.getenv("EMAIL_RECEIVER")
    print(f"使用邮箱账户: {user}")
    print(f"目标收件人: {to}")

    yag = yagmail.SMTP(user=user, password=pwd)
    yag.send(to=to, subject="微博周报：包容万物恒河水", contents=summary)
    print("📬 邮件已发送成功")

if __name__ == "__main__":
    posts = fake_fetch_weibo()
    summary = summarize(posts)
    print("📝 生成总结：", summary)
    send_email(summary)

