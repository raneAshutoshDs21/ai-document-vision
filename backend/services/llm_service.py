from openai import AzureOpenAI
from config import settings

class LLMService:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=settings.AZURE_OPENAI_API_KEY,
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_version="2024-02-01"
        )

    def summarize(self, text: str):
        response = self.client.chat.completions.create(
            model=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": "Summarize the following document."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
