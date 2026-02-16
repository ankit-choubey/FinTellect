# Fintellect AI: The Autonomous Financial Sentinel

[![Status](https://img.shields.io/badge/Status-Active%20Development-success.svg)]()
[![Backend](https://img.shields.io/badge/Django-REST%20Framework-red)]()
[![AI Engine](https://img.shields.io/badge/GenAI-Gemini%20Pro%20%2B%20RAG-purple)]()
[![Database](https://img.shields.io/badge/MongoDB-NoSQL-green)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)]()

> **"Stopping impulse spending before the transaction happens."**

> *Architected by [Ankit Choubey (Master AK)](https://github.com/ankit-choubey)*

---

## 📖 Executive Summary

**Fintellect AI** (formerly *FinGenius*) is a hyper-personalized financial intelligence system designed to solve the "impulse generation" problem. Unlike traditional fintech apps that act as passive "post-mortem" expense trackers, Fintellect operates as a **Real-Time Financial Firewall**.

By leveraging a **Hybrid NLP Pipeline** (Regex + NER + LLM) and **Retrieval-Augmented Generation (RAG)**, Fintellect intercepts transaction intents via SMS and browser overlays. It analyzes spending behavior against long-term wealth goals in milliseconds, actively intervening with a "Pre-Transaction Pause" to prevent fraud and impulse purchases.

---

## 🧠 Cognitive Architecture

Fintellect runs on an **Event-Driven Financial NLP Pipeline**, optimized for high-throughput and low-latency decision making.

### The Transaction Interception Workflow:
1.  **Ingestion Layer**: Android-level hooks capture raw transactional SMS/UPI strings in real-time.
2.  **Hybrid Parsing Engine**:
    * **L1 (Fast Path)**: Regex patterns instantly extract `Amount`, `Merchant`, and `Date` from standard bank formats (HDFC, SBI, ICICI).
    * **L2 (Deep Path)**: Complex or ambiguous strings are routed to **Google Gemini Pro** via LangChain for Zero-Shot Entity Extraction.
3.  **Contextual Retrieval (RAG)**: The system queries a **Vector Database (FAISS/ChromaDB)** to retrieve the user's historical spending vectors and current budget constraints.
4.  **Decision Logic**:
    * **Fraud Detection**: Anomaly detection algorithms (Isolation Forest) check for location/value variances.
    * **Budget Alignment**: The LLM compares the *intent* against the *goal* (e.g., "Buying these shoes delays your MacBook goal by 12 days").
5.  **Intervention**: If risk > threshold, the **"Pre-Transaction Pause"** API triggers a cognitive friction UI challenge.

---

## 🚀 Key Technical Features

* **⚡ Sub-Second Intent Analysis**: Hybrid architecture ensures 90% of transactions are parsed in <200ms via Regex, with LLM fallback only for edge cases.
* **🧠 "Pre-Transaction Pause" (USP)**: A psychological intervention mechanism that forces a 30-second "Need vs. Want" analysis before payment finalization.
* **🔍 Vector-Based Financial Context**: Uses embedding models to understand spending *patterns* (e.g., "You overspend on weekends") rather than just summing numbers.
* **🛡️ Autonomous Fraud Sentinel**: Parallel execution of anomaly detection models to flag suspicious UPI handles or geo-locations instantly.
* **🎮 Gamified Wealth Stack**: Real-time WebSocket (Django Channels) integration for live "Streak & Rank" leaderboards.

---

## 🛠️ Tech Stack & Dependencies

| Layer | Technology | Role |
| :--- | :--- | :--- |
| **Core Backend** | Python (Django REST Framework) | API Orchestration & Business Logic |
| **Async Queue** | Celery + Redis | Handling high-concurrency transaction streams |
| **Database** | MongoDB | Storing polymorphic transaction data (NoSQL) |
| **AI Engine** | Google Gemini Pro | Zero-Shot Classification & Financial Advice |
| **Orchestration** | LangChain | LLM Chain Management & Prompt Engineering |
| **Vector Store** | FAISS / ChromaDB | RAG Implementation for Financial Context |
| **Frontend** | React / Next.js | Reactive User Interface |

---

## ⚙️ Deployment & Configuration

### 1. Clone the Repository
```bash
git clone [https://github.com/ankit-choubey/fintellect-ai.git](https://github.com/ankit-choubey/fintellect-ai.git)
cd fintellect-ai

```

### 2. Environment Setup

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configuration (.env)

Create a `.env` file in the root directory:

```ini
DJANGO_SECRET_KEY=your_secret_key
LLM_API_KEY=your_gemini_api_key
MONGO_URI=mongodb://localhost:27017/fintellect
REDIS_URL=redis://localhost:6379/0

```

### 5. Database Migration & Server Start

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

---

## 📂 Repository Structure

```text
fintellect-ai/
├── core/
│   ├── nlp_engine/          # Regex & NER pipelines
│   ├── fraud_detection/     # Isolation Forest models
│   └── llm_agent/           # LangChain & Gemini integration
├── api/                     # DRF Views & Serializers
├── transactions/            # Models for SMS/UPI data
├── gamification/            # Streak & XP Logic
├── manage.py
├── requirements.txt
├── README.md
└── .env

```

---

## 🔮 Roadmap & Future Scope

* [ ] **Voice-Activated Finance**: "Hey Fintellect, can I afford this coffee?" (Whisper API integration).
* [ ] **Multi-Modal Receipt Scanning**: OCR for physical bills to automate cash tracking.
* [ ] **Predictive Cashflow**: LSTM models to forecast end-of-month balance based on current trajectory.
* [ ] **Bank API Aggregation**: Direct integration with Account Aggregator (AA) framework.

---

## 🤝 Contribution Guidelines

We invite fintech engineers and AI researchers to contribute:

1. Fork the repo (`git checkout -b feat/quantum-budgeting`).
2. Adhere to PEP-8 and Conventional Commits.
3. Submit PRs for review.

---

## 👨‍💻 Author & Visionary

**Ankit Choubey (Master AK)**
*Upcoming Billionaire | Full-Stack Architect | Tech Entrepreneur*

* **GitHub**: [ankit-choubey](https://www.google.com/url?sa=E&source=gmail&q=https://github.com/ankit-choubey)
* **Team**: CodeHashiras
* **Project**: Built for **Execute 4.0 Hackathon** & Beyond.

---

*"Building the customized financial brain for the next generation of wealth creators."*
```
