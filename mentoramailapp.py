import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Gmail Configuration ---
SENDER_EMAIL = "anilkumar22.analyst@gmail.com"
APP_PASSWORD = "utkq ugcw lpke qdxs"  # 🔒 Use your Gmail App Password here

# --- Function to send email ---
def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Email sending failed: {e}")
        return False


# --- Page Config ---
st.set_page_config(page_title="Mentora Institute", layout="wide")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #007BFF, #00B4D8);
            color: white;
        }
        .main-title {
            text-align: center;
            color: white;
            font-size: 50px;
            font-weight: 800;
            margin-bottom: 20px;
        }
        .sub-title {
            text-align: center;
            font-size: 22px;
            margin-bottom: 30px;
        }
        .stButton>button {
            background-color: #FFD60A;
            color: black;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 25px;
        }
    </style>
""", unsafe_allow_html=True)


# --- Navigation ---
st.sidebar.title("Mentora Institute 🏫")
page = st.sidebar.radio("Go to", ["Home", "Join Now", "Enquiry", "About Us"])


# --- HOME PAGE ---
if page == "Home":
    st.markdown("""
        <div style='text-align:center; padding:0; margin:0;'>
            <h1 style='color:white; font-size:50px; font-weight:800; margin-bottom:0;'>Mentora Institute</h1>
            <h3 style='color:#FFD60A; font-size:24px; font-weight:500; margin-top:5px;'>Empowering Future-Ready Professionals in Data Analytics</h3>
        </div>
    """, unsafe_allow_html=True)

    st.header("🎓 Courses Offered")
    st.write("""
    - **Data Analytics & Business Intelligence**
    - **Python Programming for Data Analysis**
    - **SQL for Data Management**
    - **Excel for Business Insights**
    - **Power BI Dashboard Mastery**
    - **Machine Learning Basics for Business**
    """)

    st.header("💡 Why Choose Us?")
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
    with col2:
        if st.button("📞 Enquiry"):
            st.session_state.page = "Enquiry"

    st.markdown("<br><hr><center>© 2026 Mentora Institute | Empowering Data Careers</center>", unsafe_allow_html=True)
    st.markdown("<br><hr><center> Email: contact@mentora.institute | Phone: +91-9876543210</center>", unsafe_allow_html=True)


# --- JOIN NOW PAGE ---
elif page == "Join Now":
    st.markdown("<h1 class='main-title'>Join Mentora Institute</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Fill in your bio-data to enroll in our upcoming Data Analytics batch.</p>", unsafe_allow_html=True)

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
        # Send email to admin
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
        user_body = f"Dear {name},\n\nThank you for registering with Mentora Institute!\nOur team will contact you soon with next steps.\n\nBest regards,\nMentora Institute Team"

        send_email("anilkumar22.analyst@gmail.com", admin_subject, admin_body)
        send_email(email, user_subject, user_body)

        st.success(f"✅ Thank you, {name}! Your enrollment form has been submitted successfully. A confirmation email has been sent.")
        st.balloons()

    if st.button("🏠 Back to Home"):
        st.session_state.page = "Home"


# --- ENQUIRY PAGE ---
elif page == "Enquiry":
    st.markdown("<h1 class='main-title'>Enquiry Form</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Ask your questions and we’ll get back to you shortly.</p>", unsafe_allow_html=True)

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
        user_body = f"Dear {enq_name},\n\nThank you for reaching out to Mentora Institute. We’ve received your enquiry and will get back to you soon.\n\nBest regards,\nMentora Institute Team"

        send_email("anilkumar22.analyst@gmail.com", admin_subject, admin_body)
        send_email(enq_email, user_subject, user_body)

        st.success(f"📩 Thank you, {enq_name}! Your enquiry has been sent. A confirmation email has been delivered to your inbox.")
        st.balloons()

    if st.button("🏠 Back to Home"):
        st.session_state.page = "Home"


# --- ABOUT US PAGE ---
elif page == "About Us":
    st.markdown("<h1 class='main-title'>About Mentora Institute</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Guiding students to become job-ready in the digital world.</p>", unsafe_allow_html=True)

    st.write("""
    **Mentora Institute** is a leading online training platform focused on transforming learners into skilled professionals.  
    Our mission is to deliver **industry-relevant, project-based education** in Data Analytics, Programming, and Business Intelligence.

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
