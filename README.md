# 👨‍🍳 Professional Chef ChatBot

Your very own **AI-powered cooking assistant**, built using **Gradio** and **Groq’s llama3-8b-8192 LLM**.  
Ask it anything about food, recipes, cooking techniques, or culinary culture, and get instant, professional chef-style answers! 🍲

---

## ✨ Features

✅ **Chef Persona** – Always responds like a professional chef with years of culinary experience  
✅ **Interactive Chat UI** – Clean, user-friendly Gradio chat interface  
✅ **Groq LLM Powered** – Uses `llama3-8b-8192` for fast and detailed responses  
✅ **Memory Support** – Maintains conversation context across turns  
✅ **Styled UI** – Uses Gradio's **Soft theme** with a red primary hue for a warm, food-inspired look  

---

## 🛠 Tech Stack

- **Python 3.9+**
- [Gradio](https://gradio.app/) – For creating the chat interface
- [Groq API](https://groq.com/) – High-performance inference with `llama3-8b-8192`

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/bobbythomas985/Chef-ChatBot
cd Chef-ChatBot

```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Set Up Your API Key
Export your Groq API key as an environment variable:
**Linux / macOS**
```bash
export GROQ_API_KEY="your_api_key_here"
```
**Windows**
```powershell
setx GROQ_API_KEY "your_api_key_here"
```
Alternatively, replace the placeholder in **app.py**:
```python
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your-api-key")
```
### 4️⃣ Run the App
```bash
python app.py
```

---

## 🖥️ How It Works

1️⃣ **User Input**  
You type a question related to food, cooking, or culinary culture.

2️⃣ **Conversation Memory**  
The system stores your conversation in a `messages_prmt` list to maintain context.

3️⃣ **Groq API Call**  
Your question + conversation history is sent to `llama3-8b-8192` for generating a chef-style response.

4️⃣ **Response Display**  
The AI-generated reply is added to chat history and shown in the Gradio interface.


## 🔮 Future Improvements

- 🍽️ **Image Input** – Upload a picture of ingredients and get recipe suggestions  
- 📖 **Recipe Mode** – Step-by-step guided cooking instructions  
- 🌍 **Cuisine Explorer** – Learn about food culture from different regions  
- 🎤 **Voice Support** – Ask questions by speaking, get voice replies back  
- 📚 **Recipe Database Integration** – Pull from real cooking APIs for accurate measurements  

---

> *Your AI-powered kitchen companion — making cooking easier, smarter, and more fun!*
