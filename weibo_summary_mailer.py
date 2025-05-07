import os
import json
import openai
import yagmail
from datetime import datetime
from weibo_crawler import WeiboCrawler

# 设置 OpenAI API 密钥
openai.api_key = os.getenv("OPENAI_API_KEY")

# 设置邮箱信息
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# 微博用户 UID
WEIBO_UID = "1671109627"

def fetch_weibo_posts(uid):
    crawler = WeiboCrawler(uid=uid)
    posts = crawler.get_latest_posts(count=10)
    return posts

def summarize_posts(posts):
    content = "\n\n".join([post['text'] for post in posts])
    prompt = f"请总结以下微博内容的要点：\n\n{content}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    summary = response.choices[0].message.content.strip()
    return summary

def send_email(subject, content):
    yag = yagmail.SMTP(user=EMAIL_USER, password=EMAIL_PASSWORD)
    yag.send(to=EMAIL_RECEIVER, subject=subject, contents=content)

def main():
    posts = fetch_weibo_posts(WEIBO_UID)
    summary = summarize_posts(posts)
    today = datetime.now().strftime("%Y-%m-%d")
    subject = f"包容万物恒河水 微博摘要 - {today}"
    send_email(subject, summary)

if __name__ == "__main__":
    main()
