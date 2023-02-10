import openai
import os


class ChatgptResponse:
    def __init__(self):
        openai.api_key = os.environ["CHATGPT_KEY"]

    def get(self, prompt: str, max_tokens: int = 1000):
        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
        )
        return completion.choices[0]["text"]
