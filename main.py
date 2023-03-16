import openai

openai.api_key = "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"
questions = input()

res = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role":"user",
            'content': questions
        }
    ]
)    
print(res["choices"][0]["message"]["content"]) # レスポンス（res）の中から返答のみを指定して出力する