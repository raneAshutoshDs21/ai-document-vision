from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from config import settings

class DocumentAIService:
    def __init__(self):
        self.client = DocumentAnalysisClient(
            endpoint=settings.DOC_INTELLIGENCE_ENDPOINT,
            credential=AzureKeyCredential(settings.DOC_INTELLIGENCE_KEY)
        )

    def analyze_document(self, file_bytes: bytes):
        poller = self.client.begin_analyze_document(
            "prebuilt-layout",
            file_bytes
        )
        result = poller.result()

        extracted_text = []
        for page in result.pages:
            for line in page.lines:
                extracted_text.append(line.content)

        return {
            "text": "\n".join(extracted_text),
            "pages": len(result.pages)
        }
