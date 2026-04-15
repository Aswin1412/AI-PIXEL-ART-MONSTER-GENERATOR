# AI Pixel Monster Generator

## Overview

AI Pixel Monster Generator is a full-stack web application that generates pixel-art monsters from user-defined prompts. The system integrates a text-to-image model to produce visuals and dynamically generates associated lore and attributes, simulating game-style content creation.

This project demonstrates the practical integration of AI models into a web application, along with backend API design and frontend interaction.

---

## Key Features

* Prompt-based pixel-art monster generation using Stable Diffusion
* Integration with HuggingFace Inference API
* Dynamic generation of monster lore and attributes
* REST API built with FastAPI
* Lightweight frontend using HTML, CSS, and JavaScript
* Local storage and serving of generated images
* Secure handling of API keys using environment variables

---

## Tech Stack

* Backend: Python, FastAPI
* AI Integration: HuggingFace Inference API (Stable Diffusion)
* Frontend: HTML, CSS, JavaScript
* Tools: Uvicorn, dotenv

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
├── images/
├── .env
├── .gitignore
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/yourusername/AI-Pixel-Monster-Generator.git
cd AI-Pixel-Monster-Generator
```

### 2. Install Dependencies

```
pip install fastapi uvicorn requests python-dotenv
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```
HF_TOKEN=your_huggingface_token
```

### 4. Run the Application

```
uvicorn Backend.main:app --reload
```

### 5. Access the Frontend

Open `Frontend/index.html` in your browser.

---

## Example Input

```
red eye demon
```

---

## Learning Outcomes

* Integrated AI models into a production-style application
* Built and exposed RESTful APIs using FastAPI
* Managed API authentication securely using environment variables
* Connected frontend UI with backend services using asynchronous requests
* Implemented dynamic content generation combining AI output and logic-based attributes

---

## Future Enhancements

* Add user authentication and saved monster profiles
* Implement a database for persistent storage
* Introduce rarity classification and scoring system
* Enable image download and sharing
* Improve UI/UX and responsiveness

---

## Author

Aswin

---

## License

This project is intended for educational and demonstration purposes.
