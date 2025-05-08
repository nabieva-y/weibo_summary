import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_weibo_posts(posts):
    if not posts:
        return "本周无新微博内容。"

    prompt = "请你将以下微博内容总结为一段中文周报风格的简短摘要：\n\n"
    prompt += "\n\n".join(posts)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=300
    )

    return response["choices"][0]["message"]["content"]
