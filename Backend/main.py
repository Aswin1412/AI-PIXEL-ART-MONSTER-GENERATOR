from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from Backend.ai_image import generate_monster_image
from Backend.ai_lore import generate_monster_lore

app = FastAPI()

# Serve generated images
app.mount("/images", StaticFiles(directory="images"), name="images")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    text: str


@app.post("/generate-monster")
def generate_monster(prompt: Prompt):

    image_url = generate_monster_image(prompt.text)

    name, lore, rarity, stats = generate_monster_lore(prompt.text)

    return {
        "title": name,
        "lore": lore,
        "rarity": rarity,
        "stats": stats,
        "image": image_url
    }