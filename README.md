
# 🚀 AI Startup Scout

AI Startup Scout is an **autonomous multi-agent market intelligence system** that discovers, classifies, and evaluates AI-first startups across different industry sectors.  
The project is designed to simulate how an investment analyst or venture scout would research emerging AI companies — but fully automated.

---

## ✨ Key Features

- 🧠 **Multi-Agent Architecture (CrewAI)**
  - Discovery Agent: Web research & startup discovery
  - Classification Agent: Industry & AI capability categorization
  - Insight Agent: Disruption scoring & competitive moat analysis
  - Reporting Agent: Executive-level report generation

- 🌐 **Real-Time Web Search**
  - Powered by Tavily Search Tool
  - Avoids hallucinations by grounding analysis in live data

- ⚡ **Smart Caching Strategy**
  - Application-level persistence for completed reports
  - CrewAI internal caching to reduce repeated API calls
  - Ultra-fast responses for previously analyzed sectors

- 🖥️ **Interactive Streamlit UI**
  - Sector-based analysis selection
  - Real-time agent status updates
  - Executive report preview & download

- 📄 **Executive-Ready Output**
  - Clean Markdown reports
  - Disruption scores, confidence levels, and strategic insights

---

## 🏗️ System Architecture

```
User (Streamlit UI)
        ↓
Persistence Layer (.md check)
        ↓
CrewAI Orchestration
 ├─ Discovery Agent (Web Search)
 ├─ Classification Agent
 ├─ Insight Agent
 └─ Reporting Agent
        ↓
Markdown Executive Report
```

---

## 🧠 Why Two Caching Layers?

| Layer | Purpose |
|-----|--------|
| **Persistence Layer** | Bypasses the entire AI workflow if a report already exists |
| **CrewAI Cache** | Prevents redundant tool & search calls during agent execution |

This design dramatically reduces **latency**, **API cost**, and **compute overhead**.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-startup-scout.git
cd ai-startup-scout
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables
Create a `.env` file:
```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 5️⃣ Run the Application
```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
.
├── app.py              # Streamlit UI
├── main.py             # Crew orchestration
├── agents.py           # Agent definitions
├── tasks.py            # Task definitions
├── reports/            # Generated sector reports (.md)
├── requirements.txt
└── README.md
```

---

## 🧪 Example Sectors

- Healthtech
- Fintech
- Sports
- B2B SaaS
- Cybersecurity
- Logistic / Supply Chain
- Sustainability

Each sector generates a **unique executive analysis report**.

---

## 🎯 Use Cases

- Venture capital & startup scouting
- Market research & competitive analysis
- AI ecosystem mapping
- Strategy & innovation teams

---

## ⚠️ Disclaimer

This project is for **research and educational purposes**.  
Insights are generated using publicly available information and AI-based reasoning.

---

## 👨‍💻 Author

**Yusuf Ataş**  
Software Engineer  
Specialized in AI Agents, Multi-Agent Systems, and AI-driven Product Design

---

## ⭐ Future Improvements

- Streaming agent outputs in real-time
- Vector database integration (long-term memory)
- Report comparison across sectors
- Deployment-ready API mode

---

If you find this project useful, feel free to ⭐ star the repository!
