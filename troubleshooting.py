
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Create the Gemini client only when an API key is available.
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


def get_fallback_steps(category):
    troubleshooting_guide = {
        "Login": [
            "Verify that your username and password are correct.",
            "Try resetting your password if you cannot sign in.",
            "Check whether your account is locked after multiple failed attempts.",
            "Contact the support team if the issue persists."
        ],
        "Application Error": [
            "Close and reopen the application.",
            "Check whether the application has any pending updates.",
            "Note the exact error message and when it occurs.",
            "Contact technical support if the application continues to crash."
        ],
        "Database": [
            "Check whether the database service is available.",
            "Verify the database connection settings.",
            "Review the error message and relevant database logs.",
            "Escalate persistent connection or performance issues to the database team."
        ],
        "API": [
            "Verify the API endpoint and HTTP method.",
            "Check the authentication token and required permissions.",
            "Review the response status code and server logs.",
            "Check rate limits and retry only when appropriate."
        ]
    }

    return troubleshooting_guide.get(
        category,
        [
            "Review the issue details and any error messages.",
            "Try to reproduce the issue.",
            "Contact technical support if the issue persists."
        ]
    )


def get_troubleshooting_steps(category, description=""):
    # Keep the existing steps available if Gemini cannot be used.
    fallback_steps = get_fallback_steps(category)

    if client is None:
        return fallback_steps

    prompt = f"""
You are a careful technical support assistant.

Analyze this support ticket and suggest 4 to 6 practical troubleshooting
steps tailored to the actual issue.

Predicted category: {category}
Ticket description:
{description}

Rules:
- Number the steps from 1 to 4-6 in your response.
- Give clear, specific, beginner-friendly actions.
- Never ask the user to reveal passwords, API keys, or access tokens.
- Do not claim you have accessed systems, logs, or accounts.
- Do not recommend destructive changes or exposing sensitive data.
- If the issue needs administrator access, mention that clearly.
- Keep the advice relevant to the described issue.
- Return only the troubleshooting steps.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        if response.text and response.text.strip():
            return [
                line.strip()
                for line in response.text.splitlines()
                if line.strip()
            ]

    except Exception as error:
        print(f"Gemini API Error: {error}")

    return fallback_steps