# weibo_fetcher.py

import requests

def fetch_weibo_posts(uid="1671109627", max_count=10):
    """
    使用 m.weibo.cn 接口获取指定 UID 的最新微博内容（JSON 返回结构，稳定不易封）
    """
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": f"https://m.weibo.cn/u/{uid}"
    }

    url = f"https://m.weibo.cn/api/container/getIndex?type=uid&value={uid}"
    
    # 获取 containerid
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception("获取 containerid 失败")
    
    data = resp.json()
    container_id = None
    for tab in data["data"]["tabsInfo"]["tabs"]:
        if tab["tab_type"] == "weibo":
            container_id = tab["containerid"]
            break

    if not container_id:
        raise Exception("未找到微博 containerid")


    # 抓取微博内容
    weibo_api = f"https://m.weibo.cn/api/container/getIndex?type=uid&value={uid}&containerid={container_id}"
    # #test
    # print("📦 container_id:", container_id)
    # print("🔗 weibo_api:", weibo_api)
    # #
    resp = requests.get(weibo_api, headers=headers)
    if resp.status_code != 200:
        raise Exception("获取微博内容失败")

    cards = resp.json()["data"]["cards"]
#  #test
#     print(f"🧾 共抓到 {len(cards)} 条 card")
#     for i, card in enumerate(cards):
#         print(f"{i+1}. card_type = {card.get('card_type')}")
# #
    # ✅ 抓取 page=2，跳过置顶微博
    page = 2
    posts = []
    while len(posts) < max_count:
        weibo_api = f"https://m.weibo.cn/api/container/getIndex?type=uid&value={uid}&containerid={container_id}&page={page}"
        resp = requests.get(weibo_api, headers=headers)
        cards = resp.json().get("data", {}).get("cards", [])

        for card in cards:
            if card.get("card_type") == 9:
                mblog = card.get("mblog", {})
                text = mblog.get("text", "")
                clean_text = strip_html_tags(text)
                posts.append(clean_text)

            if len(posts) >= max_count:
                break

        page += 1
        if not cards:
            break  # 没内容就停止

    return posts



def strip_html_tags(text):
    """快速去除微博返回 HTML 内容中的标签"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text).replace("&nbsp;", " ").replace("&amp;", "&")

