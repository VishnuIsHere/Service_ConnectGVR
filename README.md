# **Service Connect GVR**

A Python Django-based service marketplace where users can register, book services, manage bookings, and leave reviews. This project follows a RESTful API approach using Django Rest Framework (DRF).

---

## 🚀 **Features**
- User authentication (Registration, Login, OTP verification)
- Service listing with subcategories
- Service registry for employees
- Service request management
- Booking system
- User reviews (only authenticated users can post reviews)

---

## 🛠 **Tech Stack**
- **Backend**: Django Rest Framework (DRF)
- **Database**: SQLite
- **Authentication**: JWT Authentication
- **Version Control**: Git & GitHub

---

## 🔧 **Installation Guide**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/VishnuIsHere/Service_ConnectGVR.git
cd Service_ConnectGVR,ecommerce
```

### **2️⃣ Create & Activate Virtual Environment**
```sh
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on Mac/Linux
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations**
```sh
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Create Superuser (Admin)**
```sh
python manage.py createsuperuser
```

### **6️⃣ Run the Server**
```sh
python manage.py runserver
```
Visit **`http://127.0.0.1:8000/`** in your browser.

---

## 📌 **API Endpoints**

### **Authentication & User Management**
| Method | Endpoint | Description |
|--------|---------|------------|
| POST | `/register/` | Register a new user |
| POST | `/login/` | Login & get access token |
| POST | `/verify-otp/` | Verify OTP for authentication |
| POST | `/token/` | Obtain JWT access & refresh tokens |
| POST | `/token/refresh/` | Refresh access token |
| GET/POST/PUT/PATCH/DELETE | `/profile/` | View or update user profile |
| POST | `/logout/` | Logout user |

### **Service Management**
| Method | Endpoint | Description |
|--------|---------|------------|
| GET | `/services/` | List all services |
| GET/POST | `/service-registry/` | Register a new service or view existing services |

### **Service Requests & Booking**
| Method | Endpoint | Description |
|--------|---------|------------|
| GET/POST | `/service-requests/` | Create or view service requests |
| GET/PUT/DELETE | `/service-requests/<int:pk>/` | View, update, or delete a specific request |
| GET | `/bookings/` | View all bookings |

---

## 👨‍💻 **Contributing**
Feel free to fork the repo, create a branch, and submit a PR.

1. **Fork the repository**  
2. **Create a feature branch** (`git checkout -b feature-name`)  
3. **Commit your changes** (`git commit -m "Add feature X"`)  
4. **Push to GitHub** (`git push origin feature-name`)  
5. **Submit a Pull Request**

---

## 📜 **License**
This project is licensed under the **MIT License**.

---

## ✨ **Contact**
If you have any issues or feature requests, open an **issue** or reach out to me at **itsvishnupadmanabhan@gmail.com.com**.

---

## 🏆 **Show Your Support**
Give this repo a ⭐ if you find it useful! 😊

