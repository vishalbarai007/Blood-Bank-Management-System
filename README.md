# Blood-Bank-Management-System

A Blood Bank Management System is software that manages donor registration, tracks blood stock, and streamlines issuing and receiving blood. It enables quick donor searches, ensures accurate inventory management, reduces errors, and improves efficiency, with options for database integration and automation.

BloodBankManagementSystem/
│
├── django_project/                     # Django project directory
│   ├── bloodbank/                      # Django app for blood bank features
│   │   ├── migrations/                 # Database migration files
│   │   ├── static/                     # Static files (CSS, JS, images)
│   │   ├── templates/                  # HTML templates
│   │   │   ├── base.html               # Base template
│   │   │   ├── donor_form.html         # Donor registration form
│   │   │   └── search_results.html     # Search results page
│   │   ├── __init__.py
│   │   ├── admin.py                    # Admin panel configuration
│   │   ├── apps.py                     # App configuration
│   │   ├── models.py                   # Database models
│   │   ├── tests.py                    # Automated tests
│   │   ├── urls.py                     # App-specific URLs
│   │   └── views.py                    # Request handling and logic
│   ├── django_project/                 # Django project core settings
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py                 # Project-wide settings
│   │   ├── urls.py                     # Project-wide URL routing
│   │   └── wsgi.py
│   ├── db.sqlite3                      # SQLite database file
│   └── manage.py                       # Django management commands
│
├── tkinter_app/                        # Tkinter-based GUI application
│   ├── assets/                         # Assets for the GUI (icons, images)
│   ├── __init__.py
│   ├── database.py                     # SQLite database connection and queries
│   ├── donor_registration.py           # Donor registration GUI
│   ├── blood_stock.py                  # Blood stock management GUI
│   ├── blood_search.py                 # Search for donors or blood groups
│   ├── main.py                         # Main application entry point
│   └── utils.py                        # Utility functions
│
├── docs/                               # Documentation for the project
│   ├── README.md                       # Project overview
│   ├── requirements.txt                # Python dependencies
│   └── setup_guide.md                  # Setup and installation instructions
│
├── tests/                              # Automated test scripts
│   ├── test_django.py                  # Tests for Django functionality
│   ├── test_tkinter.py                 # Tests for Tkinter functionality
│   └── __init__.py
│
├── scripts/                            # Standalone scripts for data management
│   ├── import_dummy_data.py            # Script to load test data into the database
│   ├── export_data.py                  # Export data from the database
│   └── backup_database.py              # Backup the SQLite database
│
└── .gitignore                          # Files and directories to ignore in Git
