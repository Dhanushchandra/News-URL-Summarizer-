import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
from newspaper import Article
from PIL import Image, ImageTk
import requests
from io import BytesIO

def analyze_url():
    url = url_entry.get()

    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        # Fetch and display article data
        title_label.config(text="Title: " + article.title)
        publish_date_label.config(text="Publish Date: " + str(article.publish_date))
        authors_label.config(text="Authors: " + ", ".join(article.authors))
        keywords_label.config(text="Keywords: " + ", ".join(article.keywords))

        # Display image
        image_url = article.top_image
        response = requests.get(image_url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image = image.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

        summary = article.summary
        sentiment_score = TextBlob(summary).sentiment.polarity
        sentiment = get_sentiment(sentiment_score)

        # Update summary and sentiment labels
        summary_label.config(text="Summary:\n" + summary, fg="black", font=("Helvetica", 10, "italic"))
        sentiment_label.config(text="Sentiment Score: " + sentiment + " (" + str(sentiment_score) + ") ", fg=get_sentiment_color(sentiment_score), font=("Helvetica", 10, "bold"))
    except Exception as e:
        messagebox.showerror("Error", "An error occurred:\n" + str(e))

def get_sentiment(score):
    if score < -0.5:
        return "Very Negative"
    elif -0.5 <= score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    elif 0 < score <= 0.5:
        return "Positive"
    else:
        return "Very Positive"

def get_sentiment_color(score):
    if score < -0.5:
        return "red"
    elif -0.5 <= score < 0:
        return "darkorange"
    elif score == 0:
        return "gray"
    elif 0 < score <= 0.5:
        return "green"
    else:
        return "darkgreen"

def show_main_window():
    # Create the main window
    root = tk.Tk()
    root.title("URL Analyzer")
    root.geometry("500x500")

    global url_entry, title_label, publish_date_label, authors_label, keywords_label, image_label, summary_label, sentiment_label

    # URL entry
    url_label = tk.Label(root, text="Enter URL:", font=("Helvetica", 12))
    url_label.pack(pady=5)
    url_entry = tk.Entry(root, width=50, font=("Helvetica", 10))
    url_entry.pack(pady=5)

    # Analyze button
    analyze_button = tk.Button(root, text="Analyze URL", command=analyze_url, bg="lightblue", font=("Helvetica", 12, "bold"))
    analyze_button.pack(pady=5)

    # Labels to display article data
    title_label = tk.Label(root, font=("Helvetica", 10))
    title_label.pack(pady=5)
    publish_date_label = tk.Label(root, font=("Helvetica", 10))
    publish_date_label.pack(pady=5)
    authors_label = tk.Label(root, font=("Helvetica", 10))
    authors_label.pack(pady=5)
    keywords_label = tk.Label(root, font=("Helvetica", 10))
    keywords_label.pack(pady=5)

    # Image label
    image_label = tk.Label(root)
    image_label.pack(pady=5)

    # Summary label
    summary_label = tk.Label(root, wraplength=400, justify="left", font=("Helvetica", 10))
    summary_label.pack(pady=5)

    # Sentiment label
    sentiment_label = tk.Label(root, font=("Helvetica", 10))
    sentiment_label.pack(pady=5)

    root.mainloop()
