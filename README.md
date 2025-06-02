# 🛍️ Shop.co – Full-Stack Django E-commerce Platform

**Shop.co** is a modern, full-stack e-commerce platform built using Django. The project includes user authentication, dynamic product listings, cart and wishlist functionality, order management, and a full admin backend. Designed with scalability and clarity, this project reflects practical application of Django and Bootstrap to simulate a real-world online shopping experience.

---

## 📌 Features

- 🔐 User authentication: signup, login, logout
- 🛒 Shopping cart: add/remove items, update quantities
- ❤️ Wishlist feature
- 📦 Product listing with categories and search
- 📬 Order placement and tracking
- 🧑‍💼 Admin dashboard for managing users, products, orders
- 🎨 Responsive UI using Bootstrap and Font Awesome

---

## ⚙️ Tech Stack

| Layer         | Technology                        |
|---------------|------------------------------------|
| Backend       | Django (Python)                    |
| Frontend      | HTML5, CSS3, Bootstrap             |
| Icons         | Font Awesome                       |
| Database      | SQLite (development)               |
| Deployment    | (Pluggable: Heroku, Render, etc.)  |

---

## 📁 Project Structure

```bash
shop-co/
├── base/              # Base templates and views
├── cart/              # Shopping cart logic
├── home/              # Landing and home views
├── media/             # Uploaded product images
├── orders/            # Order management and checkout
├── product/           # Product model, views, forms
├── shop_co/           # Django settings and root config
├── static/            # Static files (CSS, JS, images)
├── staticfiles/       # Collected static files for production
├── templates/         # Global templates
├── users/             # Custom user auth logic
├── wishlist/          # Wishlist functionality
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Clone & Setup

```bash
git clone https://github.com/noorfathima0/shop-co.git
cd shop-co
python -m venv env
source env/bin/activate   # On Windows use: env\Scripts\activate
pip install -r requirements.txt
```

### Run Migrations & Start Server

```bash
python manage.py migrate
python manage.py runserver
```

Visit: `http://127.0.0.1:8000`

---

## 🧑‍💼 Admin Panel

Access via: `/admin/`

Create superuser:

```bash
python manage.py createsuperuser
```

---

## 🛠️ Future Enhancements

- ✅ Stripe/PayPal payment integration
- 🧾 Invoice & email notification system
- 📊 Admin analytics dashboard
- 🌍 Multilingual support (i18n)
- 🧪 Test coverage for models and views

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE)

---

## 👩‍💻 Developed by

**Noor Fathima**  
📫 [Portfolio](https://noorfathima0.github.io/My-Portfolio)  
🐙 [GitHub](https://github.com/noorfathima0)
