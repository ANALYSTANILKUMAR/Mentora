# 🎓 Mentora Institute – Data Analytics Training Website

This is the official **Streamlit web app** for **Mentora Institute**, an online learning platform offering professional training in **Data Analytics**, **Python**, **SQL**, **Excel**, **Power BI**, and **Machine Learning**.

---

## 🌐 Live Demo
👉 [https://mentora-institute.streamlit.app](https://mentora-institute.streamlit.app) *(after deployment)*

---

## 🧩 Features
- Home page with institute overview & courses offered  
- “Join Now” – Registration form for new students  
- “Enquiry” – Contact form for quick questions  
- Automatic **email notifications** to admin and users  
- Beautiful gradient background & responsive layout  

---

## ⚙️ Installation (Run Locally)

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/mentora-institute.git
cd mentora-institute
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run mentora_institute_app.py
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push this repository to GitHub.  
2. Visit [https://share.streamlit.io](https://share.streamlit.io).  
3. Click **“New App”** → Select your repo → Choose `mentora_institute_app.py`.  
4. Add your **email credentials** securely under:  
   `App Settings → Secrets → Edit Secrets`

---

## 🔐 Secrets Configuration

In **Streamlit Cloud**, go to  
**Settings → Secrets → Add the following:**

```toml
email = "anilkumar22.analyst@gmail.com"
password = "YOUR_APP_PASSWORD"
```

*(Use your Gmail App Password, not your main password!)*

---

## 🧰 Tech Stack
- **Streamlit** – Web app framework  
- **Python (smtplib)** – Email automation  
- **HTML + CSS (inline)** – Custom design & layout  
- **Gmail SMTP** – Secure email delivery  

---

## 📞 Contact
📧 Email: contact@mentora.institute  
🌐 Website: [www.mentora.institute](https://mentora.institute)  
👨‍💻 Developer: *Anil Kumar – Data Analyst & Educator*  
