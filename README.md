# **Inventory Management API**

An **Inventory Management API** built with **Django** and **Django REST Framework (DRF)**. This API allows users to manage inventory items by adding, updating, deleting, and viewing current inventory levels, with features like user authentication, inventory tracking, filtering, sorting, and pagination.

---

## **Features**

- **Inventory Item Management (CRUD)**
  - Manage items with attributes: Name, Description, Quantity, Price, Category.
  - Validate required fields: Name, Quantity, Price.

- **User Management (CRUD)**
  - Register and manage users.
  - Authentication to restrict inventory management to authorized users.

- **View Inventory Levels**
  - View current inventory with optional filters and sorting.
  
- **Track Inventory Changes**
  - Log changes to inventory quantities.
  - View change history for each item.

- **Technical Features**
  - Django ORM for database interactions.
  - Pagination and sorting for efficient data handling.
  - Deployed on platforms like Heroku or PythonAnywhere.

---

## **Getting Started**

### **Prerequisites**

- **Python 3.6+**
- **pip** package installer
- **Virtual Environment** tool (recommended)

### **Installation**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/inventory-management-api.git
   cd inventory-management-api
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv env
   env\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the Server**

   ```bash
   python manage.py runserver
   ```

---

## **Usage**

### **API Endpoints**

- **Register User:** `POST /api/register/`
- **User Detail:** `GET /api/users/{id}/`
- **List Items:** `GET /api/items/`
- **Create Item:** `POST /api/items/` *(Authentication Required)*
- **Item Detail:** `GET /api/items/{id}/`
- **Update Item:** `PUT/PATCH /api/items/{id}/` *(Authentication Required)*
- **Delete Item:** `DELETE /api/items/{id}/` *(Authentication Required)*
- **View Change Logs:** `GET /api/change_logs/` *(Authentication Required)*

### **Authentication**

- Uses **Basic Authentication**.
- Include your username and password in the request headers.





