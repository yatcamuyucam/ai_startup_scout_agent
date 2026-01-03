from crewai import Task

class StartupTasks:

    def discover_task(self, agent, sector):
        return Task(
            description=(
                f"Search the web to identify up to 3 emerging AI-first startups in the {sector} industry. "
                "Focus on companies that are genuinely disrupting the sector, not just using AI for marketing. "
                "Verify their existence through multiple sources (news, official site, LinkedIn). "
                "Critically evaluate if they are 'AI-native' or just 'AI-wrappers'."
            ),
            expected_output="A list of 3 verified AI startups with their names, websites, and a brief description of their AI core.",
            agent=agent
        )

    def classify_task(self, agent):
        return Task(
            description=(
                "Review the startups identified. Categorize them by their primary industry and "
                "the specific AI technology they leverage (e.g., Generative AI, Computer Vision, Predictive Analytics). "
                "Ensure the taxonomy is consistent and structured."
            ),
            expected_output="A structured list mapping startups to industry categories and specific tech stacks.",
            agent=agent
        )

    def insight_task(self, agent):
        return Task(
            description=(
                "Perform a deep-dive analysis on the classified startups. "
                "1. Identify their unique value proposition. "
                "2. Assess their competitive advantage (moat). "
                "3. Assign a 'Disruption Score' (0-100) based on their potential to replace legacy systems. "
                "4. Assign a 'Confidence Score' (0.0-1.0) based on the clarity and reliability of available data."
            ),
            expected_output=(
                "Detailed analysis for each startup including: "
                "Value Proposition, Competitive Advantage, Disruption Score (0-100), and Confidence Score."
            ),
            agent=agent
        )

    # tasks.py içindeki report_task metodu
    def report_task(self, agent, sector):
        clean_name = sector.lower().replace(" ", "_")
        file_name = f"report_{clean_name}.md" 

        return Task(
            description=(
                f"Generate a specialized executive report ONLY for the {sector} sector. " # Sadece bu sektör!
                f"Examine the startups identified specifically for {sector} and ignore any "
                "previous data from other industries. Highlight high-potential startups "
                f"within {sector} and identify trends specific to this industry only."
            ),
            expected_output=f"A professional Markdown report focused exclusively on the {sector} sector.",
            agent=agent,
            output_file=file_name
        )