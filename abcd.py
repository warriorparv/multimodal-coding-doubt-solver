import requests
import base64

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def image_to_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")

IMAGE_PATH = "problem.png"
image_base64 = image_to_base64(IMAGE_PATH)

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "Coding Doubt Solver"
}

payload = {
    "model": "openai/gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": (
                "You are a coding doubt solver for students. "
                "Read the coding problem from the image, explain it clearly, "
                "then provide an optimized solution with code."
            )
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Solve this coding problem:"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image_base64}"
                    }
                }
            ]
        }
    ],
    "max_tokens": 1000
}

response = requests.post(API_URL, headers=headers, json=payload)
result = response.json()

# Print only the solution text
if "choices" in result:
    bot_reply = result["choices"][0]["message"]["content"]
    print("\n🤖 CODING DOUBT SOLVER RESPONSE:\n")
    print(bot_reply)
else:
    print("\n❌ ERROR FROM OPENROUTER:\n")
    print(result)