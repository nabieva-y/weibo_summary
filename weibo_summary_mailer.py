from weibo_fetcher import fetch_weibo_posts
from summarizer import summarize_weibo_posts
from mailer import send_email



# if __name__ == "__main__":
#     uid = "1671109627"  # 包容万物恒河水
#     posts = fetch_weibo_posts(uid=uid, max_count=10)
    
#     print(f"📝 抓取微博 {len(posts)} 条")
    
#     summary = summarize_weibo_posts(posts)
#     print("📦 总结内容：", summary)

#     send_email(summary)
#     print("📬 邮件发送成功")

accounts = {
    "包容万物恒河水": "1671109627",
    "沈逸": "1157864602"
}

all_posts = []

for name, uid in accounts.items():
    posts = fetch_weibo_posts(uid)
    if posts:
        all_posts.extend([f"[{name}] {p}" for p in posts])

summary = summarize_weibo_posts(all_posts)
send_email(summary)