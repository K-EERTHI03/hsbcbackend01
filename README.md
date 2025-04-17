
# 💳 HSBC Credit Card Statement Generator (Backend)

This backend system generates monthly credit card statements in PDF format using customer and transaction data stored in a database. It's built using Python, Flask, SQLAlchemy, and ReportLab.

---

## 📁 Project Structure

```
hsbcbackend01-main/
├── app.py                    # Main Flask app with web routes
├── main.py                   # Inserts sample users and transactions into the database
├── models.py                 # SQLAlchemy ORM models for database schema
├── pdf_generator.py          # PDF builder that formats statements for download
├── gunicorn.conf.py          # Gunicorn server configuration for deployment
├── requirements.txt          # Lists all Python dependencies
├── credit_card.db            # SQLite database file with sample data
├── credit_card_statement.pdf # Sample generated PDF
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/hsbcbackend01-main.git
cd hsbcbackend01-main
```

### 2. Set Up Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Insert Sample Data

Before generating statements, populate the database with test users and transactions:
```bash
python main.py
```

---

## 🧾 Generate a PDF Statement

Run the app:
```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) and click **"Generate Statement"** to create and download a sample statement.

---

## ⚙️ Run in Production with Gunicorn

```bash
gunicorn -c gunicorn.conf.py app:app
```

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask** – Web framework
- **SQLAlchemy** – ORM for managing the database
- **SQLite** – Lightweight relational database
- **ReportLab** – PDF generation engine
- **Gunicorn** – WSGI server for production

---

## 📬 API Endpoint

| Route | Method | Description |
|-------|--------|-------------|
| `/` | `GET` | Homepage with a link to generate a statement |
| `/generate-statement` | `GET` | Triggers the generation and download of a PDF statement |

---

## 🧠 How It Works

1. `main.py` populates the database with mock data.
2. `app.py` exposes routes to interact with the system.
3. When the user visits `/generate-statement`, it fetches data from the database.
4. `pdf_generator.py` takes that data and formats it into a clean, professional statement.
5. The user receives a downloadable `credit_card_statement.pdf`.

---

## 📎 Sample Output

Check the included `credit_card_statement.pdf` file to see what the final output looks like.
