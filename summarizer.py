import requests
import os

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

def summarize_weibo_posts(posts):
    if not posts:
        return "本周暂无新微博。"

    # 构造 prompt
    content = "\n\n".join(f"{i+1}. {post}" for i, post in enumerate(posts))
    system_prompt = (
        "你是一名内容编辑，请对下列微博内容进行归纳总结，语言自然流畅，指出它们主要关注的主题、表达的思想或观点，不要逐条重复内容。"
    )

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": content}
        ],
        "temperature": 0.7,
        "max_tokens": 800
    }

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()
    else:
        return f"❌ 摘要生成失败，状态码 {response.status_code}，错误信息：{response.text}"
