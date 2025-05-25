# ☕ EmptyCup - Assignment Project

A simple full-stack app that combines a Python backend and a static HTML/CSS frontend. This project is designed to demonstrate a foundational understanding of web architecture, basic routing, and containerization with Docker.

---

## 📁 Project Structure

```
EmptyCup-Assignment/
│
├── backend/           # Python backend (Flask)
│   ├── app.py
│   └── requirements.txt
│
├── frontend/          # Static frontend
│   ├── index.html
│   ├── style.css
│   └── Images/
│
├── Dockerfile         # Docker configuration for backend
├── docker-compose.yml # Compose file to run the full app
└── README.md          # You are here!
```

---

## 🚀 Features

* 🎨 Responsive frontend using HTML & CSS
* 🧠 Python-based backend using Flask
* 🐳 Fully Dockerized for easy deployment
* 🔗 Integrated with Docker Compose

---

## 🛠️ Installation & Usage

### ✅ Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop)
* [Git](https://git-scm.com/)

---

### 📦 Run with Docker Compose

```bash
# Clone the repo
git clone https://github.com/Khushi-2409/EmptyCup-Assignment.git
cd EmptyCup-Assignment

# Build and start the containers
docker-compose up --build
```

The app will be available at:
👉 **[http://localhost:5000](http://localhost:5000)**

---

## 🧪 Project Goals

* Demonstrate backend + frontend integration
* Practice Docker & container orchestration
* Build clean, modular file structure for future scaling
