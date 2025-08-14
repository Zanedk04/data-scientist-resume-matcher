import streamlit as st
import numpy as np
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# load job data
@st.cache_data
def load_data():
    df = pd.read_csv("scraped_dataset_indeed.csv")

    # Fill missing data in descriptions with empty strings
    df['description'] = df['description'].fillna('').str.lower()
    return df

df = load_data()

# Define skill list

skills = ["python", "sql", "excel", "pandas", "numpy", "matplotlib", "seaborn",
    "scikit-learn", "tensorflow", "keras", "pytorch", "machine learning",
    "power bi", "tableau", "aws", "azure", "git", "linux", "docker",
    "communication", "bachelor", "master", "phd"]

# Vectorization formual

def vectorize_text(text, skill_list):
    text = text.lower()
    return [1 if skill in text else 0 for skill in skill_list]


st.title("Resume Skill Matcher") # Header 
st.markdown("Paste your reseume text below") # Subtitle/ text

resume_input = st.text_area("Paste Resume Here", height=300)

# If resume is pasted, turn the resume into a binary skill vector
if resume_input:
    resume_vector = np.array(vectorize_text(resume_input, skills)).reshape(1, -1)

    # Loops through description coulumn and turns it into binary skill vector
    job_vectors = df['description'].apply(lambda x: vectorize_text(x, skills))

    # Creates new column that matches how well you match the job 
    df['matchScore'] = job_vectors.apply(lambda vec: cosine_similarity(resume_vector, [vec])[0][0])

    st.subheader("Top Matching Jobs")
    # Prints top 10 matching jobs
    top_matches = df.sort_values('matchScore', ascending=False).head(10)
    st.dataframe(top_matches[['positionName', 'company', 'location', 'matchScore' ]])

    # Finds matched skills with skill_list
    matched_skills = [skill for skill in skills if skill in resume_input.lower()]

    # Finds which skills you're missing with skill_list
    missing_skills = [skill for skill in skills if skill not in resume_input.lower()]

    # Shows matched skills with skill_list
    st.subheader("Skills Found in Resume")
    st.write(", ".join(matched_skills) if matched_skills else "None")
    
    # Shows which skills you're missing with skill_list
    st.subheader("Skills Missing (In Demand)")
    st.write(", ".join(missing_skills) if missing_skills else "You're doing great!")

skills_df = pd.read_csv('skill_frequency.csv')  # Make sure this file exists

# Sidebar Title
st.sidebar.title("📊 Most In-Demand Skills")

# Show the top 20 skills and their counts
st.sidebar.write("Top 20 skills from scraped job postings:")

for _, row in skills_df.head(20).iterrows():
    skill = row['Skill']
    count = row['Count']
    st.sidebar.markdown(f"- **{skill}** ({count} mentions)")


