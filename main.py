import streamlit as st
st.set_page_config(page_title="Md. Samiul Islam's Resume", layout="wide")

# Dark mode CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600&family=Roboto+Mono&display=swap');
    
    * {
        font-family: 'JetBrains Mono', monospace;
        color: #e0e0e0;
    }
    
    body {
        background-color: #0a0a0a !important;
    }
    
    .stApp {
        background: linear-gradient(45deg, #000000, #1a1a1a);
    }
    
    .section-title {
        color: #00ff9d !important;
        border-left: 3px solid #00ff9d;
        padding-left: 1rem;
        text-shadow: 0 0 8px rgba(0, 255, 157, 0.3);
        margin: 2rem 0;
    }
    
    .card {
        background: #1a1a1a !important;
        border: 1px solid #2d2d2d;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s;
    }
    
    .card:hover {
        border-color: #00ff9d;
        box-shadow: 0 0 15px rgba(0, 255, 157, 0.1);
        transform: translateY(-3px);
    }
    
    .skill-badge {
        display: inline-block;
        background: #2d2d2d !important;
        color: #00ff9d !important;
        padding: 0.2rem 0.8rem;
        border-radius: 4px;
        margin: 0.6rem;
        border: 1px solid #00ff9d;
        font-size: 0.9em;
    }
    
    .cyber-border {
        position: relative;
        padding: 1rem;
        margin: 1rem 0;
        background: #000000;
        border: 1px solid #00ff9d;
    }
    
    .cyber-border::before {
        content: "";
        position: absolute;
        top: -3px;
        left: -3px;
        right: -3px;
        bottom: -3px;
        z-index: -1;
        background: linear-gradient(45deg, #00ff9d, transparent 50%);
    }
    
    .glow-text {
        text-shadow: 0 0 10px rgba(0, 255, 157, 0.5);
    }
</style>
""", unsafe_allow_html=True)



# Header Section
# st.markdown('<div class="header">', unsafe_allow_html=True)
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("<h1 style='color: #00ff9d'>MD. SAMIUL ISLAM</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #e0e0e0'>▷ FULL STACK DEVELOPER | ML ENGINEER</h3>", unsafe_allow_html=True)
    st.markdown("◼ GREEN UNIVERSITY OF BANGLADESH")
    st.markdown("◼ B.SC IN COMPUTER SCIENCE & ENGINEERING")

with col2: 
    st.markdown("<h1 class='glow-text' style='color: #00ff9d'>Contact</h1>" , unsafe_allow_html=True)
    st.markdown("<div>", unsafe_allow_html=True)
    st.markdown("```+8801683754038```")
    st.markdown("```mdsamiulislam2172@gmail.com```")
    st.markdown("[⌨ GITHUB](https://github.com/MDSAMIULSAMI)")
    st.markdown("[⚡ LEETCODE](https://leetcode.com/u/mdsamiulislam2172/)")
    st.markdown("</div>", unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)

# About Section
st.markdown("<h2 class='section-title glow-text'>_ABOUT PROFILE</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
    <span style="color: #00ff9d">>></span> I'm Md. Samiul Islam, a curious problem-solver and tech enthusiast with a background in Computer Science. 
    I have a solid understanding of Python, Django, Next.js, Nuxt.js and Machine Learning. My passion lies in 
    exploring web development, backend engineering and the potential of machine learning to solve real-world 
    problems. For me, every project is an opportunity to learn, grow and create something meaningful.
</div>
""", unsafe_allow_html=True)

# Education & Experience
col3, col4 = st.columns(2)
with col3:
    st.markdown("<h2 class='section-title glow-text'>_EDUCATION</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3 style="color: #00ff9d">B.SC COMPUTER SCIENCE</h3>
        <p>◼ GREEN UNIVERSITY OF BANGLADESH</p>
        <p>◼ 2020-2024 | CGPA: 3.30/4.00</p>
        <div style="border-top: 1px solid #2d2d2d; margin: 1rem 0"></div>
        <h3 style="color: #00ff9d">CERTIFICATIONS</h3>
        <p>◼ AI FOR EVERYONE <a style="text-decoration: None" href='https://coursera.org/share/6ecabbbf6c791eac234c47930bf3ed84'>(Verify Link)</a></p>
        <p>◼ BUSINESS IMPLICATIONS OF AI: A NANO-COURSE <a style="text-decoration: None" href='https://coursera.org/share/a9f5b01fc014113f4ba094aac1c9230a'>(Verify Link)</a></p>
        <p>◼ DATA SCIENCE EXPERT WITH PYTHON DJANGO <a style="text-decoration: None" href='https://simpli-web.app.link/e/42zpWLxPuNb'>(Verify Link)</a></p>
        <p>◼ PROGRAMMING FOR EVERYBODY (GETTING STARTED WITH PYTHON) <a style="text-decoration: None" href='https://coursera.org/share/07f76ab8872b96ecba8ff17cee273ef4'>(Verify Link)</a></p>
    </div>
    """, unsafe_allow_html=True) 
with col4:
    st.markdown("<h2 class='section-title glow-text'>_EXPERIENCE</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3 style="color: #00ff9d">JUNIOR SOFTWARE ENGINEER</h3>
        <p>◼ CODER ORBIT | 2024-PRESENT</p>
        <ul>
            <li>> Vue/NuxtJS • NextJS • Laravel</li>
            <li>> API Development • Testing</li>
            <li>> Technical Documentation</li>
        </ul>
        <div style="border-top: 1px solid #2d2d2d; margin: 1rem 0"></div>
        <div>
            <h3 style="color: #00ff9d">FRONTEND DEVELOPER INTERN</h3>
            <p>◼ UNICORN SOFTWARE SOLUTIONS LTD | 2023</p>
            <ul>
                <li>> VueJS • Primevue • Jira</li>
                <li>> Education Management System</li>
            </ul>
        </div>
    </div>
    
    
    """, unsafe_allow_html=True)

# Projects Section
st.markdown("<h2 class='section-title glow-text'>_PROJECTS</h2>", unsafe_allow_html=True)
projects = [
    {"title": "ROBERTA-SAN FOR TEXT CLASSIFICATION (A NOVEL HYBRID MODEL)", "tech": "[PYTHON • TRANSFORMERS • KAGGLE]", "url": "https://github.com/MDSAMIULSAMI/RoBERTa-SAN-For-Text-Classification"},
    {"title": "LOCAL IMAGE SEARCH ENGINE", "tech": "[CLIP • COMPUTER VISION]", "url": "https://github.com/MDSAMIULSAMI/Image-Search-by-Text-Prompt-using-CLIP"},
    {"title": "REALTIME CHAT SYSTEM", "tech": "[SOCKET.IO • JAVASCRIPT]", "url": "https://github.com/MDSAMIULSAMI/Simple-Real-Time-Chat-Room"},
    {"title": "ONI MART USING BASH PROGRAMMING WITH GUI", "tech": "[BASH • WHIPTAIL]", "url": "https://github.com/MDSAMIULSAMI/Bash"},
]

for project in projects:
    st.markdown(f"""
    <div class="card">
        <h3 style="color: #00ff9d">▷ {project['title']}</h3>
        <p style="color: #666">{project['tech']}</p>
        <a style="text-decoration: None" href={project['url']}>Github Link</a>
    </div>
    """, unsafe_allow_html=True)

# Skills Section
st.markdown("<h2 class='section-title glow-text'>_TECHNICAL STACK</h2>", unsafe_allow_html=True)
skills = {
    "LANGUAGES": ["PYTHON", "JAVASCRIPT(ES6, BASIC)", "BASH", "HTML5/CSS3" ],
    "FRAMEWORKS": ["DJANGO", "VUE/NUXT", "REACT/NEXT", "LARAVEL", "TAILWIND/BOOTSTRAP"],
    "TOOLS": ["VS CODE", "KAGGLE", "GOOGLE COLAB", "FIGMA", "GITHUB"],
}

skill_cols = st.columns(3)
for idx, (category, items) in enumerate(skills.items()):
    with skill_cols[idx]:
        st.markdown(f"""
        <div class="card">
            <h3 style="color: #00ff9d">◼ {category}</h3>
            {" ".join([f'<span class="skill-badge">{item}</span>' for item in items])}
        </div>
        """, unsafe_allow_html=True)

# Achievements
st.markdown("<h2 class='section-title glow-text'>_ACHIEVEMENTS</h2>", unsafe_allow_html=True)
st.markdown("""
<div class="card">
    <div style="columns: 2; gap: 2rem;">
        <div style="margin-bottom: 2rem;">
            <h3 style="color: #00ff9d">◼ PUBLICATIONS</h3>
            <p>> PUBLISHED A PAPER ON BANGLA SENTIMENT ANALYSIS (NATURAL LANGUAGE PROCESSING) IN THE JOURNAL OF BUSINESS & IT (<a style="text-decoration: None" href="https://www.researchgate.net/publication/387043086_Depressive_and_Suicidal_Text-Based_Sentiment_Analysis_in_Bangla_Using_Deep_Learning_Models">Link</a>)</p>
        </div>
        <div style="margin-bottom: 2rem;">
            <h3 style="color: #00ff9d">◼ AWARDS</h3>
            <p>> DEAN'S AWARD 2020 (GPA 3.80)</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin: 3rem 0; color: #2d2d2d padding-bottom: 0rem;">
    <span style="color: #00ff9d">⚡</span> Md. Samiul Islam • 2025 <span style="color: #00ff9d">⚡</span>
</div>
""", unsafe_allow_html=True)