from flask import Flask, send_file, render_template_string
from models import Base, Cardholder, Transaction, Statement
from pdf_generator import StatementPDFGenerator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configure SQLite database with error handling
try:
    database_url = os.environ.get('DATABASE_URL', 'sqlite:///credit_card.db')
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
except Exception as e:
    logger.error(f"Database initialization error: {str(e)}")
    raise

@app.route('/')
def home():
    try:
        return """
        <h1>HSBC Credit Card Statement Generator</h1>
        <a href="/generate-statement">Generate Statement</a>
        """
    except Exception as e:
        logger.error(f"Error in home route: {str(e)}")
        return "Internal Server Error", 500

@app.route('/generate-statement')
def generate_statement():
    session = Session()
    
    try:
        # Create sample data
        cardholder = Cardholder(
            name="Mr Arjun Mehta",
            card_number="4678",
            billing_address="D-45, Green Park,\nNew Delhi-110016, India",
            email="arjun.mehta@email.com",
            phone="+919876543210"
        )
        session.add(cardholder)
        session.flush()

        transactions = [
            Transaction(
                cardholder_id=cardholder.id,
                date=datetime.date(2025, 3, 2),
                description="Amazon India - Electronics",
                amount=3499.00
            ),
            Transaction(
                cardholder_id=cardholder.id,
                date=datetime.date(2025, 3, 2),
                description="Uber Ride - New Delhi",
                amount=285.50
            )
        ]
        session.add_all(transactions)

        statement = Statement(
            cardholder_id=cardholder.id,
            statement_date=datetime.date(2025, 3, 31),
            previous_balance=13840.00,
            payments_received=175.50,
            purchases_charges=640.00,
            finance_charges=45.00,
            new_balance=13935.50,
            credit_limit=175.00,
            available_credit=1230.00,
            payment_due_date=datetime.date(2025, 4, 20),
            reward_points=175
        )
        session.add(statement)
        session.commit()

        # Generate PDF
        pdf_path = 'credit_card_statement.pdf'
        pdf_generator = StatementPDFGenerator(statement, cardholder, transactions)
        pdf_generator.generate_pdf(pdf_path)

        # Send PDF file
        return send_file(pdf_path, as_attachment=True)

    except Exception as e:
        return f"Error: {str(e)}", 500
    
    finally:
        session.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))