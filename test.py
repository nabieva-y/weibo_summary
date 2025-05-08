from weibo_fetcher import fetch_weibo_posts

if __name__ == "__main__":
    uid = "1671109627"  # 包容万物恒河水
    posts = fetch_weibo_posts(uid=uid, max_count=5)

    print("📌 抓取到的微博内容如下：\n")
    for i, post in enumerate(posts, 1):
        print(f"{i}. {post}\n")
