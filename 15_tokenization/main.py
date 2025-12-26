import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "hY There! My name is Md Adnan Qaisar"
tokens = enc.encode(text)

print("Tokens", tokens)

