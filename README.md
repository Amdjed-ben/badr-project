# 0x01 // BADR_PROJECT_BACKEND
> **Status:** `PRODUCTION_READY` // **Service:** API Engine

This repository hosts the **Backend API Service** for Project Badr. A robust, scalable infrastructure engineered to manage security modules, project datasets, and client architecture with a focus on high-speed data delivery and secure endpoints.

---

### 0x02 // TECH_ARCHITECTURE
- **Core Engine:** `Django 5.x` (Python 3.12)
- **API Layer:** `Django REST Framework (DRF)`
- **Admin Interface:** `Jazzmin` (Customized Cyber-Dashboard)
- **Database Architecture:**
  - *Development:* `SQLite` (Lightweight)
  - *Production:* `PostgreSQL` (Deployed on Render)
- **Media Storage:** `Cloudinary` (Persistent CDN for project assets)

---

### 0x03 // CORE_FEATURES
- **RESTful API Design:** Clean endpoints for seamless React integration.
- **Secure Authentication:** Robust handling of security modules and client data.
- **Optimized Performance:** Engineered for low-latency response times.
- **Persistent Storage:** Integrated Cloudinary pipeline for media management.

---

### 0x04 // SYSTEM_SETUP
```bash
# 1. Clone the service
git clone [https://github.com/Amdjed-ben/Badr-Project-Backend](https://github.com/Amdjed-ben/Badr-Project-Backend)

# 2. Initialize Virtual Environment
python -m venv venv
source venv/scripts/activate  # Windows

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Apply Migrations & Launch
python manage.py migrate
python manage.py runserver
