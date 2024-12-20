import os
import openai

class LetterWriter:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai_client = openai.OpenAI(api_key=self.openai_api_key)

    def generate_letter(self, job_description, resume):
        pass

