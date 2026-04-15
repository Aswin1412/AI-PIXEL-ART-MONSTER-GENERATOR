# AI-PIXEL-ART-MONSTER-GENERATOR
AI Pixel Monster Generator is a full-stack web app that generates pixel-art monsters from user prompts using Stable Diffusion via HuggingFace. Built with FastAPI and JavaScript, it creates images, lore, and stats dynamically, demonstrating AI integration and API-based content generation.

# AI Pixel Monster Generator

AI Pixel Monster Generator is a full-stack web application that generates unique pixel-art monsters from user prompts using AI. It creates a monster image, lore, and stats dynamically, simulating a game-style creature generator.

---

## Features

* AI-generated monster images using Stable Diffusion (HuggingFace)
* Prompt-based monster creation
* Dynamic monster lore generation
* Randomized stats (Intensity, Stealth, Rift Affinity)
* FastAPI backend with HTML/CSS/JavaScript frontend
* Local image storage and serving

---

## Project Structure

```
AI-Pixel-Monster-Generator
│
├── Backend
│   ├── main.py
│   ├── ai_image.py
│   └── ai_lore.py
│
├── Frontend
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── images
├── .env
├── .gitignore
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/yourusername/AI-Pixel-Monster-Generator.git
cd AI-Pixel-Monster-Generator
```

---

### 2. Install dependencies

```
pip install fastapi uvicorn requests python-dotenv
```

---

### 3. Create a `.env` file

```
HF_TOKEN=your_huggingface_token
```

Get your token from: https://huggingface.co/settings/tokens

---

### 4. Run the backend

```
uvicorn Backend.main:app --reload
```

---

### 5. Open the frontend

Open `Frontend/index.html` in your browser.

---

## Example Prompt

```
red eye demon
```

---

## Tech Stack

* Python
* FastAPI
* HuggingFace API
* Stable Diffusion
* HTML, CSS, JavaScript

---

## Security

API keys are stored in `.env` and excluded from version control using `.gitignore`.

---

## Future Improvements

* Monster rarity system (Common, Rare, Epic, Legendary)
* Download generated monsters
* Monster gallery
* Database integration
* Animated pixel monsters

---

## Author

Aswin Singh

---

## License

This project is for educational and personal use.
