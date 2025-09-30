# IST105 - Assignment #4: Interactive Django Web Application

**Student Name:** Gustavo Iserte Bonfim  
**Student Number:** CT1010953  
**Course:** IST105 - Introduction to Programming  
**Assignment:** #4 – Building an Interactive Web Application with Conditional Logic, Version Control, and Deployment on AWS with Load Balancing  
**Date:** September 2025

---

## 🧾 Project Overview

This project is a Django-based interactive web application that collects user input, performs conditional logic and mathematical operations, and displays results dynamically. It is deployed on two AWS EC2 instances behind a Load Balancer using the Least Connection algorithm.

---

## 🚀 Features

- User input form for three float values: A, B, and C
- Conditional logic:
  - Validates numeric input
  - Handles edge cases (e.g., A < 1, B = 0, C < 0)
  - Computes C³ and applies further logic based on its value
- Displays all intermediate steps and final result in HTML
- Fully responsive and error-handled interface
- Deployed on AWS with load balancing
- Version-controlled using Git and GitHub with multiple branches

---

## 🛠️ Technologies Used

- Python 3
- Django
- HTML/CSS (via Django templates)
- AWS EC2 (Amazon Linux AMI)
- AWS Load Balancer (Least Connection algorithm)
- Git & GitHub

---

## 📦 Installation Instructions

### On EC2 Instances:
```bash
sudo yum update -y
sudo yum install -y python3 python3-pip
sudo pip3 install django
```
### Django Setup
```bash
django-admin startproject assignment4
cd assignment4
python3 manage.py startapp calculator
```

---

## 📬 Contact
For any questions or feedback, feel free to reach out via GitHub or Canvas.
