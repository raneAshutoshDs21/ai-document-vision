from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from config import settings

class VisionService:
    def __init__(self):
        self.client = ImageAnalysisClient(
            endpoint=settings.VISION_ENDPOINT,
            credential=AzureKeyCredential(settings.VISION_KEY)
        )

    def analyze_image(self, image_url: str):
        result = self.client.analyze(
            image_url=image_url,
            visual_features=["Read", "Objects"]
        )
        return result
