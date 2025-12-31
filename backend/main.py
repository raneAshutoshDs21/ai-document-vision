from fastapi import FastAPI, UploadFile, File, HTTPException, status
from services.storage import BlobStorageService
from services.document_ai import DocumentAIService
from services.llm_service import LLMService

app = FastAPI(title="AI Document Vision API")

# Initialize services once
blob_service = BlobStorageService()
doc_ai = DocumentAIService()
llm = LLMService()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/analyze")
async def analyze_document(file: UploadFile = File(...)):
    # 1️⃣ Validate file
    if not file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No file uploaded"
        )

    try:
        # 2️⃣ Read file content
        file_bytes = await file.read()

        if not file_bytes:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Uploaded file is empty"
            )

        # 3️⃣ Upload to Azure Blob Storage
        blob_url = blob_service.upload_file(
            file_bytes=file_bytes,
            filename=file.filename
        )

        # 4️⃣ Extract text using Document Intelligence
        extracted = doc_ai.analyze_document(file_bytes)

        if not extracted or "text" not in extracted:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to extract text from document"
            )

        # 5️⃣ Generate summary using LLM
        summary = llm.summarize(extracted["text"])

        # 6️⃣ Final response
        return {
            "status": "success",
            "filename": file.filename,
            "blob_url": blob_url,
            "summary": summary
        }

    except HTTPException:
        raise  # rethrow expected errors

    except Exception as e:
        # Catch-all safety net
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
