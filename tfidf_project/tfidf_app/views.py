import re
import math
from collections import Counter
from django.shortcuts import render

def clean_and_tokenize(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.split()

def tfidf_view(request):
    table = None
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]
        text = file.read().decode("utf-8")

        words = clean_and_tokenize(text)
        total_words = len(words)
        word_counts = Counter(words)

        result = []
        for word, count in word_counts.items():
            tf = count / total_words
            idf = math.log(1 / tf)
            result.append({"word": word, "tf": round(tf, 5), "idf": round(idf, 5)})


        table = sorted(result, key=lambda x: x["idf"], reverse=True)[:50]

    return render(request, "index.html", {"table": table})
