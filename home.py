import streamlit as st
from pathlib import Path
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "125157032_K_Harini.pdf"
profile_pic = current_dir / "photo_resume.jpg"
css_file = current_dir / "styles.css"

PAGE_TITLE="DIGITAL CV || HARINI"
PAGE_ICON=":wave:"
NAME = "K Harini"
DESCRIPTION = """
Passionate and technically adept, I thrive in roles that bridge technology and customer satisfaction. With hands-on experience in data analysis, machine learning, and web technologies, I bring a strategic mindset and strong communication skills to ensure customers derive maximum value from innovative solutions. My goal is to enhance customer experiences by delivering tailored, data-driven insights.
"""
EMAIL = "harini.kesavarapu@gmail.com"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

bg="""
<style>
    [data-testid=stAppViewContainer]{
    background-image:url("https://www.shutterstock.com/image-photo/blue-sky-background-260nw-277059062.jpg");
    background-size:cover;
    }
    [data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(bg,unsafe_allow_html=True)


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFByte=pdf_file.read()
profile_pic=Image.open(profile_pic)


col1,col2=st.columns(2,gap="small") 
with col1:
    st.image(profile_pic,width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(label="📄 Download Resume",
    data=PDFByte,
    file_name=resume_file.name,
    mime="application/octed-stream" ,  
    )

col1,col2,col3=st.columns(3)
with col1:
    st.markdown('<div class="centered-text">' + EMAIL + '</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="centered-text">9094313324</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="centered-text">Chennai</div>', unsafe_allow_html=True)


st.subheader("EDUCATION")

education = """
<div class="education-section">
    <div class="education-item">
        <div class="degree">
            <strong>B.Tech Computer Science and Engineering (Specialization in Cyber Security and Blockchain Technology)</strong>
            <span class="date">2021 – Present</span>
        </div>
        <div class="institution">
            <em>SASTRA Deemed to be University, Thanjavur</em>
        </div>
        <div class="details">
            CGPA (as of 6th semester): 8.0146
        </div>
    </div>
    <div class="education-item">
        <div class="degree">
            <strong>Higher Secondary Schooling</strong>
            <span class="date">2021</span>
        </div>
        <div class="institution">
            <em>Narayana Olympiad School, Chennai</em>
        </div>
        <div class="details">
            Higher Secondary Examination: 94.8%
        </div>
    </div>
    <div class="education-item">
        <div class="degree">
            <strong>Secondary Schooling</strong>
            <span class="date">2019</span>
        </div>
        <div class="institution">
            <em>Narayana e-Techno School, Chennai</em>
        </div>
        <div class="details">
            Secondary Examination: 94.4%
        </div>
    </div>
</div>
"""


st.write(education,unsafe_allow_html=True)

st.subheader("Professional Experience")

experience="""
<div class="Experience">
    <div class="company">
        <div class="degree">
            <strong>Data Science Intern</strong>
            <span class="date"> October 2023-December 2023</span>
        </div>
        <div class="institution">
            <em>PathFinder Global FZCO</em>
        </div>
        <div class=details-list>
            <ul>
                <li><p>Conducted in-depth analysis on historical stock data sourced from the National Stock Exchange of India (NSE), ensuring meticulous examination of trends and patterns.</p></li>
                <li><p>Applied advanced data cleaning techniques, addressing null and missing values, and categorized stocks into distinct groups. Extended the analysis over a 10-day period, consolidating daily data into a single CSV file for comprehensive and streamlined analysis.</p></li>
                <li><p>Developed a sophisticated Streamlit application showcasing technical expertise in data visualization for diverse stocks across multiple categories.</p></li>
            </ul>
        </div>
    </div>
    <div class="company">
        <div class="degree">
            <strong>Data Science Intern</strong>
            <span class="date"> June 2023-June 2023</span>
        </div>
        <div class="institution">
            <em>Onward Technologies</em>
        </div>
        <div class=details-list>
            <ul>
                <li><p> Conducted thorough data cleaning and utilized machine learning techniques, including RFM analysis and clustering, to create customer segmentation models, enhancing data-driven decision-making.</p></li>
                <li><p>Demonstrated commitment to continuous learning and fostering a data-driven culture within the organization.</p></li>
            </ul>
        </div>
    </div>
</div>

"""
st.write(experience,unsafe_allow_html=True)

st.subheader("Skills")
skills = """
<div class="skills-section">
    <div class="skills-item">
         <!-- &bull; is a bullet point -->
        <strong>C++</strong> &bull; 
        <strong>Python</strong> &mdash; Numpy, Pandas, Scikit, Matplotlib, Seaborn, Plotly &bull; <!-- &mdash; is an em dash -->
        <strong>SQL</strong> &bull; 
        <strong>Data Structures and Algorithms</strong> &bull; 
        <strong>Machine Learning Algorithms</strong> &bull; 
        <strong>Fundamentals of Cryptography</strong>
    </div>
</div>
"""
st.write(skills,unsafe_allow_html=True)

st.subheader("Projects")

projects="""
<div class=projects>
    <div class=proj>
        <div class="degree">
            <strong>  Interactive Resume Chatbot Using HTML, CSS, and JavaScript</strong>
        </div>
        <div class=details>
            <p> This project involves creating an interactive chatbot for a personal portfolio website.By leveraging HTML, CSS, 
and JavaScript, this chatbot provides a simple yet effective way to engage visitors and provide them with relevant 
information from the resume.</p>
        </div>
    </div>
    <div class=proj>
        <div class="degree">
            <strong> Automated Product Data Extraction and Analysis(Data Engineering)</strong>
        </div>
        <div class=details>
            <p> This project automates the extraction of product details from Amazon.in using Selenium. It logs in, searches for products, collects data on names, prices, reviews, and ratings, handles missing values, and exports the information to a CSV file for further analysis</p>
        </div>
    </div>
    <div class=proj>
        <div class="degree">
            <strong>  Classification of malicious URLS from legitimate URLS</strong>
        </div>
        <div class=details>
            <p>  This project is about classification of malicious urls from legitimate ones.This project includes extraction of features such as domain name ,ipaddress, http/https etc.Upon extraction, the features are converted into dataset for classification. Various classification algorithms used are SVM, Random Forest, Decision Tree and MLP</p>
        </div>
    </div>
    <div class=proj>
        <div class="degree">
            <strong>  Bitcoin Address Analysis</strong>
        </div>
        <div class=details>
            <p>  This project classifies bitcoin transactions into 13 different types based on the address of the bitcoin and the features extracted from it. The ML models used to train the dataset are KNN, Random Forest, Decision Tree,MLP ,XGBoost. After model training all the features are analyzed and the top 10 features are extracted using the selectkbest algorithm</p>
        </div>
    </div>
</div>

"""
st.write(projects,unsafe_allow_html=True)
st.subheader("Chatbot")
chatbot_html = """
<div id="chatbot">
    <div id="chat-log" style="border: 1px solid #ddd; padding: 10px; height: 300px; overflow-y: auto;"></div>
    <input type="text" id="chat-input" placeholder="Type a message..." style="width: calc(100% - 22px); padding: 10px; margin-top: 10px;">
</div>
<script>
    const chatInput = document.getElementById('chat-input');
    const chatLog = document.getElementById('chat-log');

    chatInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            const userInput = chatInput.value;
            chatLog.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
            const botResponse = getBotResponse(userInput);
            chatLog.innerHTML += `<p><strong>Bot:</strong> ${botResponse}</p>`;
            chatInput.value = '';
        }
    });

    function getBotResponse(input) {
        const responses = {
            'hello': 'Hello! How can I assist you?',
            'skills': 'My skills include programming languages like C,C++,Java,Python and Database language like SQL.I have also had the oppurtunity to learn machine learning algorithms and cryptography as a part of my curriculum',
            'experience': 'I had the opportunity to intern under 2 companies.At Onward Technologies, I worked as a data science intern where I learnt basic Machine Learning concepts such as clustering and RFM Analysis.At PathFinder Global FZCO, I had the opportunity to learn more statistical concepts as well as learn more about data analysis and data visualization. I also got to know about the streamlit tool where I developed a application to analyse the  prices of various stocks based on various factors.',
            'education': 'I am currently pursueing my computer science degree at SASTRA University',
            'projects':'Some of my projects are:Data extraction and analysis from websites , Classification of malicious URLS from legitimate URLS, Interactive Resume Chatbot Using HTML, CSS, and JavaScript,Bitcoin Address Analysis ',
        };

        const keywords = ['hello', 'skills', 'experience', 'education','projects'];

        const lowerCaseInput = input.toLowerCase();

        for (let keyword of keywords) {
            if (lowerCaseInput.includes(keyword)) {
                return responses[keyword];
            }
        }

        return 'I am not sure how to respond to that.';
    }
</script>
"""
st.components.v1.html(chatbot_html, height=500, scrolling=True)
