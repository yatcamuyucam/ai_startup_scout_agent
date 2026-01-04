import os
from crewai import Crew, Process
from agents import StartupAgents
from tasks import StartupTasks

def run(sector: str):
    # 1. Dosya adını sektöre özel ve güvenli bir formata çeviriyoruz
    # Örn: "Enterprise Software" -> report_enterprise_software.md
    clean_name = sector.lower().replace(' ', '_')
    file_name = f"report_{clean_name}.md"

    # 2. PERSISTENCE (KALICILIK) KONTROLÜ
    # Eğer bu sektörün raporu klasörde varsa, ajanları hiç yormadan dosyayı oku.
    if os.path.exists(file_name):
        print(f"\n♻️  {sector} sektörü için yerel kayıt bulundu. Veri '{file_name}' dosyasından okunuyor...")
        with open(file_name, "r", encoding="utf-8") as f:
            return f.read()

    # 3. Dosya yoksa Ajan ve Görev Fabrikalarını başlatalım
    print(f"\n🚀 {sector} sektörü için yerel kayıt bulunamadı. Ajanlar göreve çağrılıyor...")
    agents_factory = StartupAgents()
    tasks_factory = StartupTasks()

    discovery_agent = agents_factory.discovery_agent()
    classification_agent = agents_factory.classification_agent()
    insight_agent = agents_factory.insight_agent()
    reporting_agent = agents_factory.reporting_agent()

    # 5. Görevleri (Task) dinamik olarak oluşturalım 
    # Not: tasks.py'deki report_task fonksiyonunun da 'file_name' parametresini kullanması gerekir.
    discovery = tasks_factory.discover_task(discovery_agent, sector)
    classification = tasks_factory.classify_task(classification_agent)
    insight = tasks_factory.insight_task(insight_agent)
    reporting = tasks_factory.report_task(reporting_agent, sector)

    # 6. Crew'u (Ekibi) kuralım
    ai_startup_crew = Crew(
        agents=[
            discovery_agent,
            classification_agent,
            insight_agent,
            reporting_agent
        ],
        tasks=[
            discovery,
            classification,
            insight,
            reporting
        ],
        process=Process.sequential, # Sıralı mantıksal akış
        verbose=True,               # Reasoning sürecini terminalden izlemek için
        memory=True,                # Kısa süreli (context) hafıza
        cache=True                  # Tool-level cache (Aynı sorguları tekrar yapmaz)
    )

    # 7. Süreci başlatalım
    result = ai_startup_crew.kickoff()

    # 8. Sonucu döndürelim (Streamlit'e ham metin olarak gider)
    # CrewAI raporu zaten tasks.py'de belirttiğimiz file_name'e otomatik kaydedecek.
    return result.raw if hasattr(result, 'raw') else str(result)

if __name__ == "__main__":
    # Test çalıştırması
    sector_to_test = "Cybersecurity"
    output = run(sector_to_test)
    print("\n" + "="*30 + " FINAL REPORT " + "="*30 + "\n")
    print(output)