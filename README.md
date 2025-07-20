# LLM-powered-Book-Recommendation-System

An intelligent book recommendation system powered by Large Language Models (LLMs) and Hugging Face sentence embeddings. Users can input a natural language query, select a genre and emotional tone, and get a personalized list of recommended books with thumbnails, titles, and descriptions.

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

## 📂 Project Structure

  ├── Dataset/  
  │ └── books_with_emotions.csv # Book metadata + emotion scores  
  ├── tagged_description.txt # Corpus of book descriptions  
  ├── gradio-dashboard.py # Main app file  
  ├── db_books/ # Persisted vector DB (Chroma)  
  ├── assets/  
  │ └── book-recommender-ui.png # UI screenshot (optional)  
  ├── .env # API keys or environment variables  
  └── README.md  

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
