import cohere
import os
import numpy as np
import math

# from dotenv import load_dotenv


# load_dotenv()
key = "3lg9AUNX9rtseLl78F6hPvS9fCyHwklG2WNcV4HQ"

co = cohere.Client(key)


file = open("/home/ml/Code/thinkAI/data.txt", "r")

texts = []
for line in file:
    texts.append(line.split(":")[1])
    
# print(texts)    
myRecipesFromData = texts

response = co.embed(
    texts=texts,
    model='small',
)
embeddings=response.embeddings
# for embedding in embeddings:
#     print(embedding)


""" let's test here first """
response = co.embed(
    texts=["ginger,Lentils, tomatoes, onions, parsley, cilantro, vermicelli noodles, ginger, saffron, black pepper"],
    model='small',
)
embeddingForRecipeTest=response.embeddings

cosine_similarity_list = []

for i in range(len(embeddings)):
    # Calculate the dot product of the two arrays
    dot_product = np.dot(embeddingForRecipeTest, embeddings[i])

    # Calculate the norm of the two arrays
    norm_embeddingForRecipeTest = np.linalg.norm(embeddingForRecipeTest)
    norm_embedding = np.linalg.norm(embeddings[i])

    # Calculate the cosine similarity
    cosine_similarity = dot_product / (norm_embeddingForRecipeTest * norm_embedding)

    cosine_similarity_list.append((i, cosine_similarity))


# Sort the list by the variable in descending order
cosine_similarity_list.sort(key=lambda x: x[1], reverse=True)

# Select the top 3 by ID
top_3 = [x for x in cosine_similarity_list[:3]]
print("Top 3 IDs:", top_3)

for recipe in top_3:
    print(recipe[1], myRecipesFromData[recipe[0]])


