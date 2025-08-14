# Data Scientist Resume Matcher

## Overview
This project matches candidate resumes with job listings for data science roles. Job postings were scraped from multiple sites using **Apify**, then processed to extract the most in-demand skills. The app takes a resume and a job description, compares the skills in both, and gives a similarity score so you can quickly see how well they align.

## Features
- Pulls job listing data scraped with Apify.
- Extracts skills from both resumes and job postings.
- Compares them using cosine similarity to generate a match score.
- Sidebar shows the most in-demand skills based on the scraped dataset.
- Simple web app built with Streamlit for easy uploading and viewing.

## Tech Stack
- **Python 3**
- Pandas
- scikit-learn
- Streamlit
- NLTK / spaCy for text processing

## How It’s Structured
.
├── matcher.py            # Streamlit app for running the matcher
├── skills.csv            # CSV of top skills scraped from job listings (Skill, Count)
├── resumes/              # Sample resumes for testing
├── job_descriptions/     # Sample scraped job postings
├── requirements.txt      # Python package dependencies
└── README.md             # Project documentation

  
## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/data-scientist-resume-matcher.git
   cd data-scientist-resume-matcher
   pip install -r requirements.txt
   streamlit run matcher.py
