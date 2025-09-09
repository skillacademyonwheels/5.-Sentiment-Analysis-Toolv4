import requests
from config import API_KEY, API_KEY_2

# API URL and headers

# api_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased"
# api_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
# api_url = "https://api-inference.huggingface.co/models/BAAI/bge-reranker-v2-m3"
api_url = "https://api-inference.huggingface.co/models/siebert/sentiment-roberta-large-english"

headers = {"Authorization": f"Bearer {API_KEY_2}"}


# User input

text_input = input("Enter text for sentiment analysis: ")


# Send POST request to Hugging Face API

response = requests.post(api_url, headers=headers, json={"inputs": text_input})


# Check if the request was successful

if response.status_code == 200:

    result = response.json()

    print(result)
    # print(f"Sentiment: {result[0]['label']} with confidence score: {result[0]['score']}")

else:

    print(f"Error: {response.status_code}")

