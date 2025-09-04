import gradio as gr
from groq import Groq
import os

# Get API key from environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Define system prompt
def initialize_messages():
    return [{
        "role": "system",
        "content": (
            "You are a professional Chef with years of experience and detailed knowledge "
            "regarding cultural foods and you work like ChatGPT."
        )
    }]

messages_prmt = initialize_messages()

# Chatbot function
def customLLMBot(user_input, history):
    global messages_prmt
    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama3-8b-8192",
    )

    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply

# Create Gradio Chat Interface with styled layout
with gr.Blocks(theme=gr.themes.Soft(primary_hue="red")) as iface:
    gr.Markdown(
        """
        # 👨‍🍳 **Professional Chef ChatBot**
        _Welcome to your personal cooking assistant!_

        Ask anything related to food, recipes, or culinary culture from around the world 🍲
        """
    )

    chat = gr.ChatInterface(
        fn=customLLMBot,
        chatbot=gr.Chatbot(height=350),
        textbox=gr.Textbox(placeholder="Ask me a question related to cooking..."),
        title=None,
        description=None,
        examples=["Hey", "What are your recommendations?", "How to boil an egg"],
        submit_btn="🍳 Ask",
    )

# Launch app
if __name__ == "__main__":
    iface.launch()
