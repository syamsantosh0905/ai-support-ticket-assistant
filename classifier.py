
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


DATA_PATH = Path(__file__).parent / "Data" / "tickets.csv"


def train_classifier(target_column):
    """Train a text classifier for the requested target column."""

    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    data = pd.read_csv(DATA_PATH)

    required_columns = {"ticket_text", "category", "priority"}
    if not required_columns.issubset(data.columns):
        raise ValueError("CSV must contain ticket_text, category and priority.")

    data = data.dropna(subset=["ticket_text", target_column])
    data["ticket_text"] = data["ticket_text"].astype(str).str.strip()
    data = data[data["ticket_text"] != ""]

    if len(data) < 4 or data[target_column].nunique() < 2:
        raise ValueError("Add more labelled examples before training.")

    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("classifier", LogisticRegression(max_iter=1000))
    ])

    model.fit(data["ticket_text"], data[target_column])
    return model


def predict_ticket(ticket_text):
    """Predict a ticket's category and priority."""

    text = ticket_text.strip()
    if not text:
        raise ValueError("Ticket text cannot be empty.")

    category_model = train_classifier("category")
    priority_model = train_classifier("priority")

    category = category_model.predict([text])[0]
    priority = priority_model.predict([text])[0]

    return category, priority
