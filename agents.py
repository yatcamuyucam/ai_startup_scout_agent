from crewai import Agent
from crewai_tools import TavilySearchTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Model seçimi demo için kafi
llm = ChatOpenAI(
    model="gpt-4o-mini", 
    temperature=0.2 # Yaratıcılıktan ziyade tutarlı analiz için yeter 
)

# Tavily, AI odaklı aramalarda standart Google'dan daha iyi
search_tool = TavilySearchTool()

class StartupAgents:

    def discovery_agent(self):
        return Agent(
            role="Data Discovery Agent",
            goal="Identify and verify early-stage AI-first startups in the {sector} sector.",
            backstory=(
                "You are a sophisticated tech scout. Your job is not just finding keywords, "
                "but performing 'Reasoning' to distinguish between 'AI-wrappers' and 'Core AI' companies. "
                "You use multi-source verification to ensure the data is fresh and publicly valid."
            ),
            tools=[search_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False,
            memory=True # Dokümanındaki 'Shared Memory' 
        )

    def classification_agent(self):
        return Agent(
            role="Startup Classification Agent",
            goal="Categorize startups based on their underlying AI technology (LLM, CV, NLP, etc.) and industry niche.",
            backstory=(
                "You are an expert in technology taxonomies. You take raw data and structure it. "
                "You ensure that a startup's tech stack matches its industry application."
            ),
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def insight_agent(self):
        return Agent(
            role="Investment Insight Analyst",
            goal="Evaluate startups and calculate a 'Disruption Score' (1-10) based on market impact and tech depth.",
            backstory=(
                "You act as a Venture Capitalist analyst. You look for competitive advantages (moats). "
                "Your primary output is the 'Disruption Score', which considers: "
                "1. Scalability, 2. AI Innovation, 3. Sector Displacement potential."
            ),
            llm=llm,
            verbose=True,
            allow_delegation=False,
            memory=True
        )

    def reporting_agent(self):
        return Agent(
            role="Executive Reporting Agent",
            goal="Synthesize all findings into a professional, decision-oriented Markdown report.",
            backstory=(
                "You are a master of business communication. You turn complex technical scores "
                "into actionable insights for stakeholders. You focus on trends, risks, and opportunities."
            ),
            llm=llm,
            verbose=True,
            allow_delegation=False
        )