import openai
import requests
import json

# Set up OpenAI API credentials
openai.api_key = "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"

# Prompt for image generation
prompt = "Imagine a marrocan women scrooling in an application named KOZINTAI in the kitchen"

# Generate image using OpenAI API
response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="1024x1024",
    response_format="url"
)

# Get image URL from response
image_url = json.loads(json.dumps(response))["data"][0]["url"]

# Save image locally
with open("generated_image.png", "wb") as f:
    f.write(requests.get(image_url).content)
