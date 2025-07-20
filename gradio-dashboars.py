import pandas as pd
import numpy as np
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma

import gradio as gr

load_dotenv()

# Load book data
books = pd.read_csv("./Dataset/books_with_emotions.csv")
books['large_thumbnail'] = books['thumbnail'] + '&fife=w800'
books['large_thumbnail'] = np.where(
    books['large_thumbnail'].isna(),
    'cover-not-found.png',
    books['large_thumbnail']
)

# Load and embed book descriptions
raw_documents = TextLoader('tagged_description.txt').load()
text_splitter = CharacterTextSplitter(separator='\n', chunk_size=512, chunk_overlap=50)
documents = text_splitter.split_documents(raw_documents)

db_books = Chroma.from_documents(
    documents,
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
    persist_directory='db_books'
)

def retrieve_semantic_recommendations(query: str, category: str = None, tone: str = None,
                                      initial_top_k: int = 50, final_top_k: int = 10) -> pd.DataFrame:
    results = db_books.similarity_search(query, k=initial_top_k)
    book_list = [rec.page_content.strip('"').split()[0] for rec in results]
    book_recs = books[books['isbn13'].astype(str).isin(book_list)].head(final_top_k)

    if category != "All":
        book_recs = book_recs[book_recs['simple_categories'] == category].head(final_top_k)

    if tone == 'joy':
        book_recs = book_recs.copy()
        book_recs.sort_values(by='joy', ascending=False, inplace=True)
    elif tone == 'surprise':
        book_recs = book_recs.copy()
        book_recs.sort_values(by='surprise', ascending=False, inplace=True)
    elif tone == 'sadness':
        book_recs = book_recs.copy()
        book_recs.sort_values(by='sadness', ascending=False, inplace=True)
    elif tone == 'anger':
        book_recs = book_recs.copy()
        book_recs.sort_values(by='anger', ascending=False, inplace=True)
    elif tone == 'fear':
        book_recs = book_recs.copy()
        book_recs.sort_values(by='fear', ascending=False, inplace=True)
    elif tone == 'disgust':
        book_recs = book_recs.copy()
        book_recs.sort_values(by='disgust', ascending=False, inplace=True)

    return book_recs

def get_recommendations(query, category, tone):
    recommendations = retrieve_semantic_recommendations(query, category, tone)
    results = []

    for _, row in recommendations.iterrows():
        description = row.get('description', '')
        truncated_description = " ".join(description.split()[:30]) + "..."

        authors = row.get('authors', '')
        authors_split = authors.split(";")
        if len(authors_split) == 2:
            authors_str = f"{authors_split[0]} and {authors_split[1]}"
        elif len(authors_split) > 2:
            authors_str = f"{', '.join(authors_split[:-1])}, and {authors_split[-1]}"
        else:
            authors_str = authors

        caption = f"{row['title']} by {authors_str}: {truncated_description}"
        results.append((row['large_thumbnail'], caption))

    return results

# UI options
categories = ["All"] + sorted(books['simple_categories'].unique())
tones = ['All', 'joy', 'surprise', 'sadness', 'anger', 'fear', 'disgust', 'neutral']

# Gradio UI
with gr.Blocks(theme=gr.themes.Glass()) as dashboard:
    gr.Markdown("# 📚 Book Recommendation System")

    with gr.Row():
        user_query = gr.Textbox(label="Please enter a description of a book:",
                                placeholder="e.g., A story about courage and friendship")
        category_dropdown = gr.Dropdown(choices=categories, label="Select a category:", value="All")
        tone_dropdown = gr.Dropdown(choices=tones, label="Select an emotional tone:", value="All")
        submit_button = gr.Button("Find recommendations")

    gr.Markdown("## 📖 Recommendations")
    output = gr.Gallery(label="Recommended books", columns=4, rows=2)

    submit_button.click(fn=get_recommendations,
                        inputs=[user_query, category_dropdown, tone_dropdown],
                        outputs=output)

if __name__ == "__main__":
    dashboard.launch(inbrowser=True)