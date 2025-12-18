import tiktoken

# Load encoding
enc = tiktoken.encoding_for_model("gpt-4o")

# Text to tokenize
text = "HeyThere! My name is Adnan Qaisar"

# Encode text
tokens = enc.encode(text)

# Output
print("Tokens:", tokens)
print("Token count:", len(tokens))

decoded = enc.decode([25216, 5632, 0, 3673, 1308, 382, 2686, 24114, 1486, 1873, 277])
print("Decode", decoded)
