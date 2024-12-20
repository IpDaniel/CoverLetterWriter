import os
import openai

class LetterWriter:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai_client = openai.OpenAI(api_key=self.openai_api_key)

    def generate_letter(self, job_description, resume):
        response = self.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful cover letter writing assistant."},
                {"role": "user", "content": self.create_prompt(job_description, resume)},
            ],
        )
        return response.choices[0].message.content

    def create_prompt(self, job_description, resume):
        return f"Please write a cover letter for the following job description and resume. Job Description: \n{job_description}\n\nResume: {resume}"
