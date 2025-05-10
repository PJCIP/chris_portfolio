import streamlit as st
from PIL import Image

# --- Basic Information ---
name = "Christopher"
title = "Senior Executive"
introduction = """
Driven data analyst with 3 years of experience transforming raw data into actionable insights. 
Proficient in developing and deploying machine learning models to solve business challenges. 
I've also created frameworks and accelerators to streamline business pipelines and improve efficiency. 
Explore my projects below to see how I can contribute to your team.
"""
profile_image = Image.open("./images/profile.jpeg") # Replace with your image path

# --- Projects Data (for the sidebar) ---
projects = {
    "Bank Churn Prediction": "https://bankchurndemyst.streamlit.app/", # Replace with actual links or section anchors
    "Mail_Automation": "https://github.com/PJCIP/Mail-Automation",
    "Air_Quality_analysis": "https://github.com/PJCIP/-PJCIP-Air-quality-detecting-IOT-device-analysis",
    
}

# --- Experience Data (for the lower half) ---
experience_companies = [
    {"name": "EXL","year": "2022 - Present" ,"logo": Image.open("./images/logos/EXL_Service_logo.png")}, # Replace with your image paths
    {"name": "Cognitica AI", "year": "2020","logo": Image.open("./images/logos/cognitica_ai.png")},
    {"name": "Guvi", "year": "2019", "logo": Image.open("./images/logos/guvi.png")},
    {"name": "No Food Waste", "year": "2019", "logo": Image.open("./images/logos/no_food_waste.png")}
]

# --- Main Page Layout ---

# Sidebar for Projects
with st.sidebar:
    st.header("Projects")
    for project_name, link in projects.items():
        markdown = f"""
        <div style="margin-bottom: 10px;">
            <a href="{link}" target="_blank">
                <button style="background-color: transparent;
                    border: 2px solid red;
                    color: red;
                    padding: 10px 20px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    cursor: pointer;
                    border-radius: 20px;">
                    {project_name}
                </button>
            </a>
        </div>
        """
        st.markdown(markdown, unsafe_allow_html=True)

# print(st.session_state.selected_project)
# Main Area
col1, col2 = st.columns([3, 1])

with col1:
    st.title(name)
    st.subheader(title)
    st.write(introduction)

with col2:
    st.image(profile_image, width=200) # Adjust width as needed

st.markdown("<hr>", unsafe_allow_html=True) # Separator

st.header("Experience")
cols = st.columns(4)


projects_desc =    {"Cognitica AI": "- **PATIENT SENTIMENT INSIGHTS** - Assembled a sentiment analysis pipeline that predicts the sentiment with an precision of around **70%.** "
    ,"EXL": """- **FRAUD SENTINEL** - Assembled a classification pipeline that predicts a fraudulent activity in Emergency Visits in US Hospitals. With 85% of F1 score ,were able to **increase** revenue of $500 Grand every month. \n 
    - **MARKET MAVEN** - Assembled a classification pipeline that captures pattern of the Market. With 45% precision and 70% recall were able to **increase** revenue of $ 4 M every month."""
    ,"Guvi":" - **GUVI MAIL BOX** - **Turned down** about **75%** of **mailing time** where automation takes an edge off the manual mailing process."
    ,"No Food Waste":"- **AIR QUALITY FORENSICS** - Suggested a strategy to **minimize** the cost of the IoT product by **16%.**"}


for i, company in enumerate(experience_companies):
    img,desc =  st.columns(2)
    img.image(company["logo"], caption=company["year"],use_container_width=True)
    desc.markdown(projects_desc[company["name"]])

st.markdown("<hr>", unsafe_allow_html=True) # Separator

# for i, company in enumerate(experience_companies):
#     with cols[i]:
#         st.markdown(
#             f"""
#             <div style="display: flex; flex-direction: column; align-items: center;">
#                 <img src="{company['logo']}" alt="{company['name']}" style="width: 80%; max-width: 100px;">
#                 <p style="text-align: center; margin-top: 5px;">{company['name']}</p>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

# st.markdown("<hr>", unsafe_allow_html=True) # Separator
# # --- Project Details Section (will appear on the main page) ---
# st.header("Project Details")
# if "selected_project" in st.session_state:
#     st.subheader(st.session_state.selected_project)
#     # Add details about the selected project here
#     st.write(f"Details for {st.session_state.selected_project} will go here.")
# else:
#     st.info("Click on a project in the sidebar to view its details.")

# You can add more sections like Skills, Contact, etc. below.