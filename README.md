# 📚 Semantic Book Recommender

This project is a **learning-based implementation** aimed at exploring the integration of **Large Language Models (LLMs)**, **semantic similarity search**, and **emotion-aware filtering**. It uses modern AI tools such as **LangChain**, **Hugging Face Sentence Transformers**, and **Gradio** to build an intelligent book recommendation system.

Users can enter a natural language query describing the kind of book they are interested in, and the system recommends titles based on semantic relevance, genre, and emotional tone. The goal of this project was to **gain hands-on experience** with vector databases, embeddings, and interactive user interfaces — key components in building real-world AI-powered applications.

---

## 📸 Demo Screenshot

<img width="1920" height="966" alt="image" src="https://github.com/user-attachments/assets/faacc417-ec2c-4f4d-b43b-90e06a5de4d1" />

---

## 🚀 Features

- 🔍 **Semantic Search**: Retrieve books based on meaning, not just keywords.
- 🧠 **LLM Intelligence**: Leverages LLMs (or embeddings) to understand user intent.
- 😄 **Emotion Filtering**: Filter recommendations by tone (e.g., Joy, Fear, Surprise).
- 🎨 **Beautiful UI**: Built using [Gradio](https://www.gradio.app/) for seamless interactivity.
- 📊 **Genre Selection**: Choose specific book categories like Fiction, Biography, etc.
- 🖼️ **Cover Previews**: Includes large thumbnail previews of each recommended book.

---

## 🛠️ Installation & Running the App

Follow these steps to set up and run the Semantic Book Recommender:

---

### 🧪 Step 1: Set up a virtual environment

- Run `python -m venv .venv` to create a virtual environment.
- Activate the environment:
  - On macOS/Linux: `source .venv/bin/activate`
  - On Windows: `.venv\Scripts\activate`

---

### 📥 Step 2: Install dependencies

- Make sure your environment is activated.
- Run `pip install -r requirements.txt` to install all necessary packages.

---

### ▶️ Step 3: Run the Gradio app

- Execute the script by running: `python gradio-dashboard.py`
- The app will launch at `http://127.0.0.1:7860/`

To make it publicly shareable, modify the launch line in `gradio-dashboard.py` like this:

```python
dashboard.launch(share=True)
