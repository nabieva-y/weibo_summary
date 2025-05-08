import openai
import os

# 建议使用默认客户端初始化方法（新写法）
#client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    organization="org-VkZyew7Umepy4xud9hHOwMVk"  # ← 用你上一步复制的那个替换这里
)

def summarize_weibo_posts(posts):
    if not posts:
        return "本周无新微博内容。"

    prompt = "请你将以下微博内容总结为一段中文周报风格的简短摘要：\n\n"
    prompt += "\n\n".join(posts)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=300,
    )

    return response.choices[0].message.content
