import openai
import time
import json

# Set up the OpenAI API key
openai.api_key = "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"

# Define the prompt to send to Chat GPT
prompt = "Hello, how are you?"

# Send the prompt to Chat GPT and receive the response
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
# Print the response from Chat GPT
response_json = json.loads(json.dumps(response))
print(response_json["choices"][0]["text"])

