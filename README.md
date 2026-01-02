# 🚀 AI Document Vision Platform

A production-ready, cloud-native AI document processing system built using **FastAPI, Streamlit, Docker, GitHub Actions, and Azure**.


🔗 **Live Demo:** 

---

## 📌 Project Overview

This project demonstrates an end-to-end **AI-powered document processing platform** with:

- Backend API for document processing
- Frontend UI for user interaction
- Full CI/CD pipeline
- Containerized deployment on Azure

The system is designed following **industry-grade DevOps practices**.

---

## 🧠 Key Features

- 📄 Upload and process documents+Scanned Images
- 🤖 AI-based document understanding
- 🐳 Dockerized backend and frontend
- 🔁 Automated CI/CD using GitHub Actions
- ☁️ Azure Container Registry integration
- ⚙️ Cloud-ready deployment architecture

---

## 🏗️ Architecture Overview
<img width="2693" height="2863" alt="Project architecture" src="https://github.com/user-attachments/assets/e03fc7dc-836b-420e-b95c-5cf1cc82cfbf" />

---

## 🧩 Tech Stack

| Layer | Technology |
|------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Registry | Azure Container Registry |
| Cloud Platform | Microsoft Azure |

---

## 📂 Project Structure
```
ai-document-vision/
├── backend/
│ ├── main.py
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── .github/
│ └── workflows/
│ └── docker-build.yml
└── README.md
```


---

## ⚙️ CI/CD Pipeline

The CI/CD pipeline is implemented using **GitHub Actions**.

### Pipeline Flow:
1. Code push to `main`
2. Docker images built for backend and frontend
3. Images pushed to Azure Container Registry
4. Ready for deployment to Azure services

---

## 🐳 Dockerized Deployment

Both frontend and backend are packaged as Docker images.

Example build command:
```bash
docker build -t ai-backend ./backend
docker build -t ai-frontend ./frontend
```
## CICD Workflow
```
Code Push
↓
GitHub Actions
↓
Build Docker Images
↓
Push to Azure Container Registry
```
---

### CI/CD Responsibilities

- Builds backend and frontend Docker images  
- Pushes images to Azure Container Registry  
- Produces deployment-ready artifacts  

---

## 🐳 Containerized Deployment

Both frontend and backend are deployed as Docker containers.

### Backend
- FastAPI-based REST API  
- Handles document processing logic  

### Frontend
- Streamlit-based UI  
- Communicates with backend via HTTP  

---

## 🚀 Running Locally

### Backend
```bash
cd backend
uvicorn main:app --reload
```
### Frontend
```bash
cd frontend
streamlit run app.py
```
---
## ☁️ Cloud Deployment

- Docker images are stored in Azure Container Registry  
- Deployed using Azure App Services or Azure Container Apps  
- Environment variables control runtime behavior  

---

## 🔐 Security & Best Practices

- Secrets are never committed to source code  
- Environment variables are used for sensitive configuration  
- Containers are isolated and reproducible  

---

## 📊 Project Status

- ✔ Containerized  
- ✔ CI/CD Enabled  
- ✔ Cloud Ready
---

## 👤 Author

**Ashutosh Rane**  
Azure AI

- LinkedIn: https://www.linkedin.com/in/your-profile  
- Email: ashutosh.21122001@gmail.com







