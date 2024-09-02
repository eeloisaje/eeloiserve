import requests
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.graph_objects as go

# --------- PAGE TITLE -------------------
st.set_page_config(page_title=" Hello, I'm Eloisa ", page_icon="🦖")

# --------- PAGE LAYOUT -------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Jersey+10&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap');

    body {
        background-color: #fafaf0;
    }
    .center-chart {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
    }
    .main .block-container {
        max-width: 1200px; /* Change this value to your desired width */
        padding-left: 50px; /* Optional: adjust padding to suit your layout */
        padding-right: 50px;
        padding-top:80px; /* Optional: adjust padding to suit your layout */
    }

    .custom-subheader {
        font-family: 'Jersey 10', sans-serif;
        font-size: 35px;
        text-align: left;
        margin-bottom: 20px;
    }
    .custom-header {
        font-family: 'Jersey 10', sans-serif;
        font-size: 30px;
        margin-bottom: 15px;
    }
    .custom-title {
        font-family: 'Jersey 10', sans-serif;
        font-size: 40px;
        margin-bottom: 50px;
        text-align: left;
    }
    .custom-write {
        font-size: 16px;
        font-family: 'Roboto Mono', sans-serif;
        text-align: justify;
        margin: 0 auto;
        max-width: 100%;
        line-height: 1.6;
    }
    .center-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        height: 100%;
        width: 100%;
        text-align: left;
    }
    .side-by-side {
        display: flex;
        align-items: center;
    }
    .side-by-side img {
        margin-right: 15px; /* Space between image and text */
    }
    /* Hide the full-screen button */
    button[title="View fullscreen"] {
        display: none;
    }
    input[type=message], input[type=email], input[type=text], textarea {
        width: 100%; /* Full width */
        padding: 12px; /* Some padding */ 
        border: 1px solid #ccc; /* Gray border */
        border-radius: 4px; /* Rounded borders */
        box-sizing: border-box; /* Make sure that padding and width stays in place */
        margin-top: 6px; /* Add a top margin */
        margin-bottom: 16px; /* Bottom margin */
        resize: vertical; /* Allow the user to vertically resize the textarea (not horizontally) */
    }

    /* Style the submit button with a specific background color etc */
    button[type=submit] {
        background-color: #04AA6D;
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }

    /* When moving the mouse over the submit button, add a darker green color */
    button[type=submit]:hover {
        background-color: #45a049;
    }

    /* Modal styles */
    .modal {
        display: none;
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.4);
    }

    .modal-content {
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 80%;
    }

    .close {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
    }

    .close:hover,
    .close:focus {
        color: black;
        text-decoration: none;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ------ ASSETS --------------
lottie_coding = load_lottieurl("https://lottie.host/ae5d202f-3ead-4bd2-b973-3fea837fe683/uRkbHDxQ0n.json")

# --------- TAB LAYOUT -------------------
tab1, tab2 = st.tabs(["🏠 HOME", "🚀 LEARN MORE"])

# --------- HOME TAB CONTENT -------------------
with tab1:
    # --------- HEADER SECTION -----------
    with st.container():
        left_column, right_column = st.columns([2, 4])
        with left_column:
            st.image("assets/loloi.png", width=400)
        with right_column:
            st.markdown(
                """
                <div class="center-content">
                    <p class="custom-subheader">Hi there, I am <span style="color: #FF6700;">Eloisa J. Españo 🚀</span></p>
                    <p class="custom-title">Aspiring Cloud Engineer and Tech Innovator</p>
                    <p class="custom-write">
                       I was born on June 28, 2001, in Manila, Philippines, and currently residing in Cansojong, Talisay City, Cebu. I graduated with High Honors from Badian National High School, specializing in the TVL Programming Strand. Now a 4th-year BSIT student, I am passionate about cloud engineering and technology innovation. My academic journey has provided me with a strong foundation in IT, and I am eager to apply my knowledge to real-world challenges, with the goal of contributing to the field of cloud technologies and driving digital transformation.
                    </p>
                </div>
                """, unsafe_allow_html=True
            )

    # --------- WHAT I DO SECTION -----------
    with st.container():
        st.write("---")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<p class="custom-header">🛠️ WHAT I DO</p>', unsafe_allow_html=True)
            activities = [
                {"image": "assets/check.png", "description": "I develop software solutions, with a focus on programming languages like Java, Python, and React.js."},
                {"image": "assets/check.png", "description": "I continuously explore new technologies and frameworks, enhancing my technical proficiency."},
                {"image": "assets/check.png", "description": "I am passionate about cloud computing and its potential to revolutionize data management and digital services."},
                {"image": "assets/check.png", "description": "I engage in creative pursuits such as drawing and painting, which help me maintain a balanced perspective."},
                {"image": "assets/check.png", "description": "I am committed to personal growth through reading and spiritual practices, which enrich my professional and personal life."}
            ]
            for activity in activities:
                left_column, right_column = st.columns([1, 4])
                with left_column:
                    st.image(activity["image"], width=50)
                with right_column:
                    st.markdown(f'<p class="custom-write">{activity["description"]}</p>', unsafe_allow_html=True)

        with col2:
            st.markdown('<p class="custom-header">💻 MY HARD SKILLS</p>', unsafe_allow_html=True)

            # Radar Chart - Hard Skills
            fig = go.Figure(data=go.Scatterpolar(
                r=[4, 4, 4, 3, 5, 4, 3],
                theta=['Python', 'Java', 'C', 'Visual Basic', 'HTML', 'CSS', 'React.js'],
                fill='toself',
                fillcolor='rgba(135, 206, 250, 0.6)',
                line=dict(color='white', width=2),
                marker=dict(size=9, color='white')
            ))

            fig.update_layout(
                polar=dict(
                    bgcolor='black',
                    radialaxis=dict(
                        visible=True,
                        range=[0, 5],
                        tickvals=[1, 2, 3, 4, 5],
                        gridcolor='gray',
                        gridwidth=1
                    ),
                    angularaxis=dict(
                        gridcolor='#B5B3C3',
                        gridwidth=1
                    )
                ),
                showlegend=False,
                width=600,
                height=400,
            )
            st.markdown('<div class="center-chart">', unsafe_allow_html=True)
            st.plotly_chart(fig)
            st.markdown('</div>', unsafe_allow_html=True)

    # --------- SOFT SKILLS SECTION -----------
    with st.container():
        st.write("---")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<p class="custom-header">💻 MY SOFT SKILLS</p>', unsafe_allow_html=True)
            # Radar Chart - Soft Skills
            fig = go.Figure(data=go.Scatterpolar(
                r=[4, 4, 5, 4, 5, 4, 5, 5],
                theta=['Communication', 'Problem-Solving', 'Adaptability', 'Teamwork', 'Time Management', 'Customer Service', 'Attention to Detail', 'Creativity'],
                fill='toself',
                fillcolor='rgba(163, 197, 133, 0.6)',
                line=dict(color='white', width=2),
                marker=dict(size=9, color='white')
            ))

            fig.update_layout(
                polar=dict(
                    bgcolor='black',
                    radialaxis=dict(
                        visible=True,
                        range=[0, 5],
                        tickvals=[1, 2, 3, 4, 5],
                        gridcolor='gray',
                        gridwidth=1
                    ),
                    angularaxis=dict(
                        gridcolor='#A3C585',
                        gridwidth=1
                    )
                ),
                showlegend=False,
                width=600,
                height=400,
            )
            st.markdown('<div class="center-chart">', unsafe_allow_html=True)
            st.plotly_chart(fig)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<p class="custom-header"> 🛠️ WORK EXPERIENCE</p>', unsafe_allow_html=True)
            activities = [
                {"image": "assets/check.png", "description": "I was a Non-Academic Scholar at CIT-U and worked in the Human Resource Department for five months."},
                {"image": "assets/check.png", "description": "My tasks primarily involved filing and checking employee requirements, as well as assisting in creating PowerPoint presentations for events like the Sinag Awards and Year-End Party."},
            ]
            for activity in activities:
                left_column, right_column = st.columns([1, 4])
                with left_column:
                    st.image(activity["image"], width=50)
                with right_column:
                    st.markdown(f'<p class="custom-write">{activity["description"]}</p>', unsafe_allow_html=True)

with st.container():
    st.write("---")


# --------- LEARN MORE TAB CONTENT -------------------
with tab2:
     st.markdown('<p class="custom-header">Get In Touch With Me! 🚀</p>', unsafe_allow_html=True)
     with st.container():
        st.write("##")
        contact_form = """
        <form id="contactForm" action="https://formsubmit.co/espanoeloisa@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>

        <div id="successModal" class="modal">
            <div class="modal-content">
                <span class="close" onclick="document.getElementById('successModal').style.display='none'">&times;</span>
                <p>Thank you! Your message has been sent successfully.</p>
            </div>
        </div>

        <script>
        document.getElementById("contactForm").addEventListener("submit", function(event) {
            event.preventDefault();
            const form = event.target;
            fetch(form.action, {
                method: "POST",
                body: new FormData(form)
            })
            .then(response => {
                if (response.ok) {
                    document.getElementById("successModal").style.display = "block";
                    form.reset();
                } else {
                    alert("There was a problem with the submission.");
                }
            })
            .catch(() => {
                alert("There was a problem with the submission.");
            });
        });
        </script>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")


