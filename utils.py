import openai
import base64
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def image_to_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

async def analyze_hand(image_path: str) -> str:
    base64_img = image_to_base64(image_path)
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "system", "content": "Ти досвідчений хіромант. Проаналізуй фото долоні людини і дай глибоку відповідь про її характер, долю, здоров’я, стосунки та кар’єру."},
            {"role": "user", "content": [
                {"type": "text", "text": "Проаналізуй цю долоню."},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_img}"}}
            ]}
        ],
        max_tokens=1000
    )
    return response.choices[0].message["content"]