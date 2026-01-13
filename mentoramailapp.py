import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- PAGE CONFIG ---
st.set_page_config(page_title="Mentora Institute", layout="wide")

# --- EMAIL SETTINGS ---
SENDER_EMAIL = "anilkumar22.analyst@gmail.com"
APP_PASSWORD = "YOUR_APP_PASSWORD"  # ⚠️ Replace with your Gmail App Password


# --- FUNCTION TO SEND EMAIL ---
def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Email sending failed: {e}")
        return False


# --- CUSTOM STYLING (Light Blue Theme) ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #cce5ff, #e6f2ff);
            background-attachment: fixed;
            background-size: cover;
            color: #000000;
        }
        .main-title {
            text-align: center;
            font-size: 52px;
            color: #0047AB;
            font-weight: 900;
        }
        .sub-title {
            text-align: center;
            font-size: 22px;
            color: #007BFF;
            margin-bottom: 30px;
        }
        .section-header {
            font-size: 26px;
            color: #0047AB;
            margin-top: 40px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #007BFF, #66B2FF);
            color: white;
            font-weight: bold;
            border-radius: 12px;
            padding: 10px 25px;
            font-size: 16px;
            border: none;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #0047AB;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)


# --- SESSION INITIALIZATION ---
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Mentora Institute 🏫")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Join Now", "Enquiry", "About Us"],
    index=["Home", "Join Now", "Enquiry", "About Us"].index(st.session_state.page)
)


# --- HOME PAGE ---
if page == "Home":
    st.markdown("<h1 class='main-title'>Mentora Institute</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Empowering Future-Ready Professionals in Data Analytics</p>", unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>🎓 Courses Offered</h3>", unsafe_allow_html=True)
    st.write("""
    - **Data Analytics & Business Intelligence**
    - **Python Programming for Data Analysis**
    - **SQL for Data Management**
    - **Excel for Business Insights**
    - **Power BI Dashboard Mastery**
    - **Machine Learning Basics for Business**
    """)

    st.markdown("<h2 class='section-header'>💡 Why Choose Us?</h2>", unsafe_allow_html=True)
    st.write("""
    - Real-world business and industrial data training  
    - Hands-on projects and dashboards  
    - Expert mentors with industry experience  
    - Live + Recorded classes  
    - Job-ready skills and interview preparation  
    """)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📝 Join Now"):
            st.session_state.page = "Join Now"
            st.rerun()
    with col2:
        if st.button("📞 Enquiry"):
            st.session_state.page = "Enquiry"
            st.rerun()

    st.markdown("<div class='footer'>© 2026 Mentora Institute | contact@mentora.institute | +91-9876543210</div>", unsafe_allow_html=True)


# --- JOIN NOW PAGE ---
elif page == "Join Now":
    st.markdown("<h1 class='main-title'>Join Mentora Institute</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Fill in your details to enroll in our upcoming batch.</p>", unsafe_allow_html=True)

    with st.form("join_form"):
        name = st.text_input("Full Name")
        dob = st.date_input("Date of Birth")
        email = st.text_input("Email Address")
        phone = st.text_input("Mobile Number")
        qualification = st.text_input("Qualification")
        course = st.selectbox("Select Course", [
            "Data Analytics & Business Intelligence",
            "Python Programming",
            "SQL for Data Analysis",
            "Excel for Business",
            "Power BI Dashboard",
            "Machine Learning Basics"
        ])
        experience = st.text_input("Experience (if any)")
        submit = st.form_submit_button("Submit")

    if submit:
        admin_subject = f"New Admission Form: {name}"
        admin_body = f"""
        New student registration details:

        Name: {name}
        DOB: {dob}
        Email: {email}
        Phone: {phone}
        Qualification: {qualification}
        Course: {course}
        Experience: {experience}
        """
        user_subject = "✅ Thank You for Registering with Mentora Institute"
        user_body = f"Dear {name},\n\nThank you for registering with Mentora Institute!\nOur team will contact you soon.\n\nBest regards,\nMentora Institute Team"

        send_email("anilkumar22.analyst@gmail.com", admin_subject, admin_body)
        send_email(email, user_subject, user_body)
        st.success(f"✅ Thank you, {name}! Your enrollment form has been submitted successfully.")
        st.balloons()

    if st.button("🏠 Back to Home"):
        st.session_state.page = "Home"
        st.rerun()


# --- ENQUIRY PAGE ---
elif page == "Enquiry":
    st.markdown("<h1 class='main-title'>Enquiry Form</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Ask your questions and we’ll respond soon.</p>", unsafe_allow_html=True)

    with st.form("enquiry_form"):
        enq_name = st.text_input("Full Name")
        enq_dob = st.date_input("Date of Birth")
        enq_mobile = st.text_input("Mobile Number")
        enq_email = st.text_input("Email Address")
        query = st.text_area("Your Query / Question")
        enq_submit = st.form_submit_button("Submit Enquiry")

    if enq_submit:
        admin_subject = f"New Enquiry from {enq_name}"
        admin_body = f"""
        Name: {enq_name}
        DOB: {enq_dob}
        Mobile: {enq_mobile}
        Email: {enq_email}
        Query: {query}
        """
        user_subject = "📩 Thank You for Contacting Mentora Institute"
        user_body = f"Dear {enq_name},\n\nThank you for reaching out to Mentora Institute.\nWe’ve received your enquiry and will get back to you soon.\n\nBest regards,\nMentora Institute Team"

        send_email("anilkumar22.analyst@gmail.com", admin_subject, admin_body)
        send_email(enq_email, user_subject, user_body)
        st.success(f"📩 Thank you, {enq_name}! Your enquiry has been sent successfully.")
        st.balloons()

    if st.button("🏠 Back to Home"):
        st.session_state.page = "Home"
        st.rerun()


# --- ABOUT US PAGE ---
elif page == "About Us":
    st.markdown("<h1 class='main-title'>About Mentora Institute</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Guiding students to become job-ready in the digital world.</p>", unsafe_allow_html=True)

    st.write("""
    **Mentora Institute** is a leading online training platform focused on transforming learners into skilled professionals.
    We provide project-based education in **Data Analytics**, **Programming**, and **Business Intelligence**.

    ### 💫 Our Mission
    - Empower learners with practical, job-oriented skills  
    - Bridge the gap between education and employment  
    - Deliver quality learning with industry expert mentors  

    ### 🌟 Our Vision
    To become a trusted institute producing the next generation of data-driven professionals ready for global challenges.

    ### 📞 Contact Us
    - 📧 Email: contact@mentora.institute  
    - 📱 Phone: +91-9876543210  
    - 🌐 Website: www.mentora.institute  
    """)

    if st.button("🏠 Back to Home"):
        st.session_state.page = "Home"
        st.rerun()
