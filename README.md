# 🔐 DES Encryption Web App (Flask)

A simple web application built with **Python** and **Flask** that enables users to perform text encryption using the **Data Encryption Standard (DES)** algorithm. The app provides a user-friendly interface to input plaintext and an 8-character key, and displays the encrypted result in hexadecimal format.

---

## 🚀 Features

- Encrypt text using the DES algorithm (ECB mode)
- User-friendly web interface built with HTML and Flask
- Key validation to ensure exactly 8 characters
- Displays encrypted output in hexadecimal format

---

## 🛠 Technologies Used

- Python 3.10
- Flask
- PyCryptodome (for cryptographic operations)

---

## 📦 Project Structure

```

des\_flask\_app/
│
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
└── static/
    └── style.css        # Style for HTML
└── templates/
    └── index.html       # HTML template for UI

````

---

## 🧪 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/gbennnn/data-encryption-standard.git
cd data-encryption-standard
````

### 2. Create & Activate a Virtual Environment (Optional)

```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/macOS
.venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Example

* **Plaintext**: `Learning Cryptography`
* **Key**: `mykey123`
* **Encrypted Output**: `b0a0986d2dfa5c708b7a77d37d21a48b61016932a91fc1c6`

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it for educational or personal use.

---

## 🤝 Contributing

Contributions, feedback, and ideas are welcome! Fork this repo and submit a pull request if you'd like to improve it or add new features.

---
## Preview

![image](https://github.com/user-attachments/assets/9feeb4cd-0d97-4629-ba0f-50c3475ec501)


