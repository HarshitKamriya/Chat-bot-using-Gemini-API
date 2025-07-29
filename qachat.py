import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini with your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini 2.0 Flash model (same as gemini-1.5-flash-latest)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

# Create chat session
chat = model.start_chat(history=[])

def main():
    print("🤖 Gemini 2.0 Flash Chatbot: Type 'exit' to end the conversation.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break
        try:
            response = chat.send_message(user_input)
            print("🤖:", response.text)
        except Exception as e:
            print("⚠️ Error:", e)

if __name__ == "__main__":
    main()