import cohere
import os
from dotenv import load_dotenv


load_dotenv()
key = os.getenv("openai_api_key")

co = cohere.Client(key)


response = co.embed(
    texts=['hello', ' goodbye'],
    model='small',
)
print(response.embeddings)
