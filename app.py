import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY")

# Initialize Claude client
client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)

# Streamlit UI
st.title("📄 Claude Resume Tailoring Assistant")
st.markdown("Paste the job description below to get a tailored resume in JSON format for Google Docs script.")

# Text input
job_description = st.text_area("💼 Job Description", height=400)

if st.button("✏️ Generate Tailored Resume"):
    if not job_description.strip():
        st.warning("Please paste a job description before generating.")
    else:
        with st.spinner("Generating with Claude..."):

            # Prompt with job description injected directly
            prompt = f"""
You are an AI assistant tasked with tailoring a resume to match a specific job description. Your goal is to create a customized resume that highlights the most relevant skills, experiences, and achievements for the given job opportunity. Follow these instructions carefully to complete the task.

First, review the job description:
<job_description>
{{job_description}}
</job_description>

Now, review the original resume content:
Original Resume Content
Work Experience:
Helm (Jan 2025 - Mar 2025) - Data Analyst Intern

Designed SQL-based data models for 5+ Power BI dashboards, reducing ad-hoc queries by 30% and improving reporting efficiency
Engineered churn and performance prediction models using Scikit-learn and XGBoost, boosting dealer targeting precision across campaigns
Developed Power BI dashboards to track financial and behavioral KPIs, delivering real-time insights for strategic decision-making
Optimized revenue forecasting by 25% using Python-based regression models, enhancing monthly financial planning accuracy
Accelerated projected dealer acquisition by 42.86% through data-driven lead scoring and targeted outreach modeling

Wyant College of Optical Sciences (Sep 2023 - Dec 2024) - Full Stack Developer

Built ML models using Python to analyze student engagement, leading to a 25% increase in overall platform adoption within 3 months
Developed real-time backend systems with SQL and Firebase to support seamless data flow for 1000+ active users
Designed dashboards in Power BI and React, improving monthly student retention by 18% through actionable insights

Brainerd Solutions LLC (Dec 2022 - Jun 2023) - Software Developer

Built serverless ETL pipelines using AWS Lambda, Glue, and DynamoDB, cutting latency by 40%
Implemented real-time activity logging with AWS Kinesis and Step Functions, improving monitoring efficiency
Improved platform reliability by optimizing validation for 10K+ daily events

Bosch Global Software Technologies (Apr 2022 - Oct 2022) - Web Developer – Project Trainee

Created internal data visualization tools with React.js and Material UI, improving data access for the team
Enhanced data analysis by integrating Neo4j, enabling advanced graph insights and optimized node-level filtering
Deployed Grafana dashboards to monitor system metrics, reducing issue resolution time by 45%

Projects:

Real-time Data Streaming Pipeline – https://github.com/gss-18/Realtime-Data-Streaming
Credit Card Fraud Detection – https://github.com/gss-18/Fraud-Detection
Life Expectancy Prediction – https://github.com/gss-18/Life-Expectancy
Supply Chain Dashboard – https://github.com/gss-18/Business-Intelligence-Project
Telco Churn – https://github.com/gss-18/Telco_Project
Cricket Score Predictor – https://github.com/gss-18/Cricket_Score_Predictor
Home Price Prediction – https://github.com/gss-18/Cricket_Score_Predictor
Disease Prediction – https://github.com/gss-18/Final_Project
AI-Powered Resume Tailoring System

Your task is to analyze the job description and tailor the resume content to create a customized resume that matches the job requirements. Follow these steps:

1. Analyze the job description:
   - Identify required skills and tools
   - Extract key responsibilities
   - Note desired experience levels
   - Recognize industry-specific terminology

2. Tailor the resume content:
   - Create a concise summary (1-2 sentences) that highlights your most relevant qualifications for the position
   - Modify work experience bullets for each position to emphasize relevant skills and achievements
   - Select and tailor relevant project descriptions
   - Group and categorize skills based on the job requirements

3. Format the tailored content:
   - Ensure all bullet points are concise and fit on a single line (approximately 100-120 characters)
   - Include an action verb, tool/technology used, and quantified result in every bullet point
   - Match terminology to the job description
   - Focus only on relevant experience and skills

Output Format:
<output_format>
function updateResumeForProjectmates() {{
  const body = DocumentApp.getActiveDocument().getBody();
  const replacements = {{
     "summary": "concise professional summary tailored to job description",
  "work.helm1": "tailored bullet point 1 for Helm",
  "work.helm2": "tailored bullet point 2 for Helm",
  "work.helm3": "tailored bullet point 3 for Helm",
  "work.helm4": "tailored bullet point 4 for Helm",
  "work.helm5": "tailored bullet point 5 for Helm",
  "work.wyant1": "tailored bullet point 1 for Wyant",
  "work.wyant2": "tailored bullet point 2 for Wyant",
  "work.wyant3": "tailored bullet point 3 for Wyant",
  "work.wyant4": "tailored bullet point 4 for Wyant",
  "work.brainerd1": "tailored bullet point 1 for Brainerd",
  "work.brainerd2": "tailored bullet point 2 for Brainerd",
  "work.brainerd3": "tailored bullet point 3 for Brainerd",
  "work.bosch1": "tailored bullet point 1 for Bosch",
  "work.bosch2": "tailored bullet point 2 for Bosch",
  "work.bosch3": "tailored bullet point 3 for Bosch",
  "project.ptitle1": "selected project 1 title",
  "project.plink1": "selected project 1 link",
  "project.plinkD1": "tailored description for project 1",
  "project.ptitle2": "selected project 2 title",
  "project.plink2": "selected project 2 link",
  "project.plinkD2": "tailored description for project 2",
  "skills.skills.header.1": "skill category 1",
  "skills.skills.values.1": "relevant skills for category 1",
  "skills.skills.header.2": "skill category 2",
  "skills.skills.values.2": "relevant skills for category 2",
  "skills.skills.header.3": "skill category 3",
  "skills.skills.values.3": "relevant skills for category 3",
  "skills.skills.header.4": "skill category 4",
  "skills.skills.values.4": "relevant skills for category 4",
  "skills.skills.header.5": "skill category 5",
  "skills.skills.values.5": "relevant skills for category 5"
  }};
  for (const key in replacements) {{
    body.replaceText(`{{{{${{key}}}}}}`, replacements[key]);
  }}
}}
</output_format>

Important:
- make sure not to add ```javascript in the output
- Ensure all bullet points are concise and fit on a single line
- Each bullet should highlight an achievement with a specific tool/skill mentioned in the job description
- Every bullet follows this strict format: Action verb + Tool/Tech + Quantified Outcome
- Focus only on the most relevant experiences and skills for the position

Provide your tailored resume content in the specified format, ensuring that all fields are filled with appropriate, tailored content based on the job description and original resume and make sure to add all the  keywords to obtain high ATS score
"""

            try:
                response = client.messages.create(
                    model="claude-3-7-sonnet-20250219",
                    max_tokens=20000,
                    temperature=1,
                    messages=[{
                        "role": "user",
                        "content": [{"type": "text", "text": prompt}]
                    }]
                )

                output = response.content[0].text
                st.success("✅ Tailored resume JSON generated!")
                st.code(output, language="json")

            except Exception as e:
                st.error(f"❌ Error: {e}")
