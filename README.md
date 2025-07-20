#  Hybrid Rasa + OpenAI GPT Customer Support Chatbot

An AI-powered chatbot that integrates **Rasa's conversation management** with **OpenAI's GPT models**, ensuring both structured dialogue control and natural language understanding.  

## 📌 Project Information

- **Version:** 1.1.0  
- **Author:** Faisal Hakimi  
- **Email:** [email](faisalh5556@gmail.com)  
- **Website:** [Portfolio]([https://yourportfolio.com](https://hakimi-portfolio-0.vercel.app/))  
- **Repository:** [GitHub Repo](https://github.com/Faisalhakimi22/Automated-Customer-Support-Chatbot/tree/main)  
- **License:** MIT License  
- **Last Updated:** 2024-08-03  

---

## 🌟 Features

✔️ 🚀 **Hybrid AI chatbot (Rasa + GPT-4)**  
✔️ 📲 **Multi-platform support (Web, Telegram, WhatsApp, Discord)**  
✔️ 🔍 **Context-aware conversation flow**  
✔️ 📈 **Logging & analytics for performance tracking**  
✔️ ⚙️ **Customizable intent recognition & responses**  
✔️ 🛠️ **Scalable API & cloud deployment support**  

---

## 🏗️ Project Structure

```
customer-support-chatbot/
├─ data/             # Rasa training data (FAQs, customer queries)
├─ models/           # Trained chatbot models
├─ backend/          # API and chatbot logic
├─ frontend/         # UI integrations (Telegram, Web, etc.)
├─ logs/             # Logs interactions for analysis
├─ requirements.txt  # Dependencies
├─ config.yml        # Rasa chatbot configuration
└─ README.md         # Documentation
```

---

## ⚙️ Technologies Used

| **Backend**       | **Frontend**       | **NLP Tools**   | **Deployment**         |
| ----------------- | ------------------ | --------------- | ---------------------- |
| Python 🐍         | React ⚛️ / Next.js | NLTK / Spacy    | Docker 🐳              |
| Flask / FastAPI   | Streamlit          | Hugging Face 🤗 | AWS / Firebase ☁️      |
| OpenAI GPT / Rasa |                    | Transformers    | CI/CD (GitHub Actions) |

---

## 🚀 Installation Guide

### 🔧 Prerequisites

- Python 3.8+  
- pip  
- Rasa CLI  
- Git  

### 🛠️ Steps

1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-username/customer-support-chatbot.git
cd customer-support-chatbot
```

2️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

3️⃣ **Set Up API Keys**  
Create a `.env` file and add:
```sh
OPENAI_API_KEY="your_api_key_here"
```

4️⃣ **Train the Rasa Model**
```sh
rasa train
```

5️⃣ **Run the Chatbot**
- **GPT-based**:
  ```sh
  python backend/chatbot.py
  ```
- **Rasa**:
  ```sh
  rasa run --enable-api
  ```
- **Hybrid (Rasa + GPT)**:
  ```sh
  python backend/hybrid_chatbot.py
  ```

6️⃣ **Deploy using Docker (Optional)**
```sh
docker build -t chatbot .
docker run -p 8000:8000 chatbot
```

---

## ✅ Testing & Debugging

| Test Type              | Command         |
| ---------------------- | --------------- |
| 🧪 **Unit Testing**    | `pytest tests/` |
| 🔄 **Rasa Model Test** | `rasa test`     |
| 🌐 **API Testing**     | Postman         |

---

## 🔥 Future Enhancements

🚀 **Multilingual Support**  
🎤 **Voice-based interaction (Speech-to-Text)**  
🔍 **Advanced intent recognition with embeddings**  
📊 **Admin Dashboard for Analytics**  

---

## 🤝 Contribution Guidelines

- **Fork** the repository  
- **Create a feature branch**  
- **Commit changes & submit a PR**  
- Open issues for suggestions 🚀  

📩 **For support, contact:** [email](mailto:faisalh5556@gmail.com)  

---

## 📜 License

📚 **MIT License** – Open-source and free to modify.  
© 2024 **Faisal Hakimi**
