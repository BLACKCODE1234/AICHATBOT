# po = "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"

# from google import genai
# client = genai.Client("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")
# response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents="Explain how AI works in a few words"

# )
# print(response.txt)


new_api = "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"

import google.generativeai as genai

# Configure your API key
genai.configure(api_key=new_api)

# Create a model instance (gemini-1.5-pro or gemini-1.5-flash)
model = genai.GenerativeModel("gemini-2.5-flash")

# Generate content
response = model.generate_content("Explain how AI works in a few words")

# Print the response
print(response.text)
