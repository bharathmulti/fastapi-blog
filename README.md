<img width="378" height="186" alt="image" src="https://github.com/user-attachments/assets/5fd4704c-a0f0-4e83-bb16-ab65e9e856c6" />\# 🚀 FastAPI Blog API



A fully functional \*\*Blog API\*\* built using \*\*FastAPI\*\*, following clean architecture with routers, repository pattern, and authentication.



\---



\## 🔥 Features



\* ✅ User Registration \& Login

\* ✅ Password Hashing using Bcrypt

\* ✅ JWT Authentication

\* ✅ CRUD Operations for Blogs

\* ✅ SQLAlchemy ORM Integration

\* ✅ Clean Folder Structure (Router + Repository)

\* ✅ Error Handling with HTTPException



\---



\## 🛠️ Tech Stack



\* \*\*Backend:\*\* FastAPI

\* \*\*Database:\*\* SQLite (can be extended to PostgreSQL)

\* \*\*ORM:\*\* SQLAlchemy

\* \*\*Authentication:\*\* JWT Tokens

\* \*\*Password Hashing:\*\* Bcrypt



\---



\## 📁 Project Structure



```

fastapi\\\_learning/

│

├── routers/

│   ├── blog.py

│   ├── user.py

│   └── repository/

│       ├── blog.py

│       └── user.py

│

├── models.py

├── schemas.py

├── database.py

├── hashing.py

├── jwt\\\_token.py

├── oauth2.py

├── main.py

└── blog.db

```



\---



\## ⚙️ Installation \& Setup



```bash

\\# Clone the repository

git clone https://github.com/your-username/your-repo.git
\\# Navigate into project

cd your-repo
\\# Create virtual environment

python -m venv venv
\\# Activate environment

venv\\\\Scripts\\\\activate   # Windows
\\# Install dependencies

pip install -r requirements.txt
\\# Run the server

uvicorn main:app --reload

```
\---

\## 📌 API Endpoints

\### 👤 User

\* `POST /user` → Create User

\* `GET /user/{id}` → Get User

\### 📝 Blog

\* `GET /blog` → Get all blogs

\* `POST /blog` → Create blog

\* `GET /blog/{id}` → Get single blog

\* `DELETE /blog/{id}` → Delete blog
\---
\## 🔐 Authentication
\* Uses JWT tokens

\* Secure password hashing with Bcrypt
\---
\## 🚀 Future Improvements

\* 🔹 Add PostgreSQL support

\* 🔹 Deploy on cloud (Render / AWS)

\* 🔹 Add pagination \& filtering

\* 🔹 Add unit testing

\## 👨‍💻 Author
\*\ T. Bharath Reddy \*\*
\* GitHub: https://github.com/bharathmulti

\* LinkedIn: https://www.linkedin.com/in/tammaneni-bharath-reddy-837a04359/

⭐ If you like this project, give it a star!

