import requests
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def generate_monster_image(prompt):

    full_prompt = f"""
    pixel art monster sprite,
    retro video game character,
    dark fantasy creature,
    pixel art style,
    simple background,
    {prompt}
    """

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": full_prompt}
    )

    # If model returns an error
    if "image" not in response.headers.get("content-type", ""):
        print("HuggingFace error:", response.text)
        return "https://via.placeholder.com/256"

    filename = f"{uuid.uuid4()}.png"
    filepath = f"images/{filename}"

    with open(filepath, "wb") as f:
        f.write(response.content)

    return f"http://127.0.0.1:8000/images/{filename}"