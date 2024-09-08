MediQ: Hospital Management System
MediQ is a comprehensive hospital management web application developed for the Smart India Hackathon (SIH) 2024. This application aims to streamline hospital operations by offering solutions for various aspects of hospital management, including patient queuing, bed availability, admissions, and inventory management.

Key Features
Patient Queuing System: Efficiently manage patient queues in Outpatient Departments (OPDs) to reduce wait times and improve service delivery.
Bed Availability Tracking: Real-time updates on bed availability across different wards and departments within the hospital.
Patient Admissions: Simplified process for patient admissions, including data entry and tracking.
Inventory Management: Monitor and manage hospital inventory to ensure adequate supplies and prevent shortages.
Hospital Login: Secure login feature for hospital staff to update bed availability and view inventory details.
Technologies Used
Backend: Django, a high-level Python web framework.
Database: PostgreSQL, hosted on Railway for remote access.
Deployment: Vercel for deploying the Django application.
Static File Management: WhiteNoise for serving static files in production.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/mediQ.git
Navigate to the project directory:

bash
Copy code
cd mediQ
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Configure your environment variables. Make sure to include:

SECRET_KEY
PGDATABASE
PGUSER
PGPASSWORD
HOST
PORT
Apply migrations:

bash
Copy code
python manage.py migrate
Collect static files:

bash
Copy code
python manage.py collectstatic
Run the server:

bash
Copy code
python manage.py runserver
Usage
Access the application via Vercel URL.
Log in as hospital staff to manage bed availability and inventory.
Contributing
Feel free to fork the repository and submit pull requests. For any issues or feature requests, please open an issue on the GitHub repository.
