import google.generativeai as genai
from prompts import PLAN_PROMPT, DAILY_WORKOUT_PROMPT
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Load API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ ERROR: GEMINI_API_KEY not found in .env file!")

genai.configure(api_key=api_key)

# Use correct Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_plan(goal: str, level: str = "beginner"):
    prompt = PLAN_PROMPT.format(goal=goal, level=level)
    response = model.generate_content(prompt)
    return response.text


def generate_daily_workout(level: str):
    prompt = DAILY_WORKOUT_PROMPT.format(level=level)
    response = model.generate_content(prompt)
    return response.text
