# NeuTech - A Django web application 🛍️

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project is an e-commerce web application developed using Django 4.x, Python 3.x, Bootstrap, and Tailwind CSS, with an SQLite3 database. The application allows users to browse products, add them to their cart, and proceed with the checkout process.

## Features

- User authentication (registration, login, logout)
- Product listing and detail pages
- Search and filter functionality
- Order placement and checkout process
- Secured Payment gateway integrated with Stripe
- Admin panel for managing products, categories, and orders

## Technologies Used

- **Backend**: Django 4.x, Python 3.x
- **Frontend**: Bootstrap, Tailwind CSS
- **Database**: SQLite3
- **Template Engine**: Django Template Language (DTL)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine
- Django 4.x installed (this can be done via pip)
- Node.js and npm installed (for managing frontend dependencies like Tailwind CSS)

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/e-commerce-django.git
   cd e-commerce-django
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Node.js dependencies**:
   ```bash
   npm install
   ```

5. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Admin Panel**: Access the admin panel at `http://127.0.0.1:8000/admin/` to manage products, categories, and orders.
- **User Interface**: Browse products,and for buying them proceed with the checkout process as a user.
- **Adding Product**: For adding the products as a seller go to, "http://127.0.0.1:8000/myapp/products/add".
- **Updating the products info**: For doing so visit, "http://127.0.0.1:8000/myapp/products/mylistings/" by loging into  your user account.

The Videographic representation of the web-app UI:

https://github.com/Tharunmoonwalker/neu_tech/assets/119483447/19890a3a-dd41-4de0-b6a3-99d51d470f74


## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

 

## Contact

If you have any questions or suggestions, feel free to contact me at karthicktharun11@gmail.com

---

Thank you for checking out this project! Happy coding!
