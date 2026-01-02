flowchart TD

    User[👤 User / Browser]

    subgraph Frontend
        FE[Frontend App<br/>(Streamlit)]
    end

    subgraph Backend
        API[Backend API<br/>(FastAPI)]
    end

    subgraph Azure
        ACR[Azure Container Registry]
        LOGS[Azure Log Analytics]
    end

    User --> FE
    FE --> API
    API -->|Reads/Writes| ACR
    API --> LOGS

    CI[GitHub Actions CI/CD] --> ACR
