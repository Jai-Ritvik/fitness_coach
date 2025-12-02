from flask import Flask, render_template, request
import markdown
from agents import generate_plan
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    goal = request.form.get("goal")
    result = generate_plan(goal)

    # Ensure result is a dictionary
    if isinstance(result, str):
        try:
            # Try parsing as JSON
            result = json.loads(result)
        except json.JSONDecodeError:
            # If it's not JSON, treat the whole string as the plan
            result = {"plan": result}

    # Convert Markdown → HTML
    formatted_output = markdown.markdown(result.get("plan", ""))

    return render_template("result.html", output=formatted_output)

if __name__ == "__main__":
    app.run(debug=True)
