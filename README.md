#  HNG Stage 0 – Backend Task (Python/Django)

## Project Overview

This is a simple **Django REST API** created for the HNG Stage 0 Backend task.
The API exposes a single endpoint `/me` that returns:

* Your name, email, and backend stack
* The current UTC timestamp (ISO 8601 format)
* A random cat fact fetched from the **Cat Facts API**

---

## Technologies Used

* **Python 3**
* **Django 5**
* **Django REST Framework**
* **Requests**
* **python-dotenv**

---

## Folder Structure

```
hng_stage0_backend/
│
├── core/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── profile_api/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

##  Setup Instructions

### 1 Clone the Repository

```bash
git clone https://github.com/ASZagam/hng-stage0-backend-profile.git
cd hng_stage0_backend
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Linux/Mac
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory with the following:

```
USER_EMAIL=abdulmaliksz02@gmail.com
USER_NAME=Abdulmalik Sani Zagam
USER_STACK=Backend/Python/Django
```

### 5️⃣ Run the Server

```bash
python manage.py runserver
```

### 6️⃣ Visit the Endpoint

Open your browser and go to:

```
http://127.0.0.1:8000/me
```

---

## 🧠 Example Response

```json
{
    "status": "success",
    "user": {
        "email": "abdulmaliksz02@gmail.com",
        "name": "Abdulmalik Sani Zagam",
        "stack": "Python/Django"
    },
    "timestamp": "2025-10-17T20:41:25.553568+00:00",
    "fact": "The Maine Coone is the only native American long haired breed."
}
```

---

## 🧩 Environment Variables

| Variable     | Description                 |
| ------------ | --------------------------- |
| `USER_EMAIL` | Your personal email address |
| `USER_NAME`  | Your full name              |
| `USER_STACK` | Your backend stack          |

---

## 🐾 API Reference

### **GET** `/me`

**Description:** Returns user details, current UTC time, and a random cat fact.

**Response Codes:**

* `200 OK` – Success
* `500 Internal Server Error` – If Cat Fact API fails

---

## ⚡ Notes

* Every request to `/me` fetches a **new cat fact** from `https://catfact.ninja/fact`
* Timestamp updates dynamically with each request
* `.env` file is excluded from Git via `.gitignore`
* Uses `python-dotenv` for environment configuration

---

## ✍️ Author

**Name:** Abdulmalik Sani Zagam
**Email:** [abdulmaliksz02@gmail.com](mailto:abdulmaliksz02@gmail.com)
**Stack:** Backend/Python/Django
**Matric Number:** U18CO1005
**Institution:** Ahmadu Bello University, Zaria, Nigeria

---

## 🧾 License

This project is open source and available under the [MIT License](LICENSE).
