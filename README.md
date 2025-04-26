
# Blood Bank Management System
<br />

<p align="center">

  <h3 align="center">Blood Bank Management System</h3>

  <p align="center">
    A robust and user-friendly blood bank management system built with Tkinter, Django, and SQLite.
    <br />
    <a href="https://github.com/vishalbarai007/blood-bank-management-system"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="https://github.com/vishalbarai007/blood-bank-management-system/issues">Report Bug</a>
    ·
    <a href="https://github.com/vishalbarai007/blood-bank-management-system/issues">Request Feature</a>
  </p>
</p>

---

## Table of Contents

- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Snapshots](#snapshots)
- [Program Flow](#program-flow)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

## About The Project

The **Blood Bank Management System** is a comprehensive Python-based solution developed to streamline the critical operations of blood banks.  
It combines a **Tkinter graphical frontend**, a **Django REST API backend**, and **SQLite storage** to manage donor registrations, stock inventory, and hospital requests.

Key Features:
- Role-based authentication
- Real-time blood stock updates
- Hospital request management
- Intuitive GUI for admins and users
- Scalability-ready modular architecture

( [Back to Top](#table-of-contents) )

---

## Built With

- [Python 3.12.3](https://www.python.org/)
- [Django 4.x](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [SQLite](https://www.sqlite.org/)

( [Back to Top](#table-of-contents) )

---

## Getting Started

To set up the project locally, follow these simple steps:

### Prerequisites

- Python installed (>= 3.12.3)
- pip package manager

```bash
pip install --upgrade pip
```

### Installation

1. Clone the repo
   ```bash
   git clone https://github.com/vishalbarai007/blood-bank-management-system.git
   ```

2. Navigate to the backend folder and install Django and DRF
   ```bash
   pip install django djangorestframework
   ```

3. Navigate to the frontend folder and install required packages (requests, etc.)
   ```bash
   pip install requests
   ```

4. Run migrations for the backend
   ```bash
   python manage.py migrate
   ```

5. Start the Django server
   ```bash
   python manage.py runserver
   ```

6. Launch the frontend
   ```bash
   python blood_bank_client.py
   ```

( [Back to Top](#table-of-contents) )

---

## Usage

- Admins can:
  - Log in
  - Register donors
  - Manage blood stock
  - View and approve hospital requests
- Standard users:
  - Submit blood requests via Contact Us page

The system ensures smooth and secure blood management operations by leveraging modern Python technologies.

( [Back to Top](#table-of-contents) )

---

## Snapshots

### Login Page
<p align="center">
  <img src="https://github.com/user-attachments/assets/129bb879-5685-43d0-b5f8-685206f0302a" alt="Login Page" width="700" />
 
</p>

### Admin Dashboard
<p align="center">
  <img src="https://github.com/user-attachments/assets/c831c321-5b92-4fbc-b085-96e9666e6ef2" alt="Admin Dashboard" width="700" />

</p>

### Donor Registration Form
<p align="center">
  <img src="https://github.com/user-attachments/assets/4ad917e9-724c-4850-9095-03f6d1292ecd" alt="Donor Registration" width="700" />
</p>

### Contact Us Page
<p align="center">
  <img src="https://github.com/user-attachments/assets/9942683d-00b7-4a94-84bf-a93db4c4ccd1" alt="Contact Us" width="700" />
</p>

### Database Snapshot
<p align="center">
  <img src="https://github.com/user-attachments/assets/040d4089-c522-4a5e-8f02-8d9b9a967450" alt="Database Snapshot" width="700" />
</p>


( [Back to Top](#table-of-contents) )

---

## Program Flow

- User logs in via the frontend.
- Admin dashboard appears with options:
  - Donor Registration
  - Blood Stock Management
  - Contact Form Access
- Tkinter interacts with Django REST API endpoints to fetch, update, and submit data.
- SQLite maintains all donor, stock, and request data.

( [Back to Top](#table-of-contents) )

---

## Roadmap

- [ ] Add Admin Panel Enhancements
- [ ] Implement Email Notifications for Requests
- [ ] Integrate Google Maps API for Hospital Location
- [ ] PWA / Desktop App Packaging
- [ ] Add Search and Filter in Donor List

See [open issues](https://github.com/vishalbarai007/blood-bank-management-system/issues) for more ideas.

( [Back to Top](#table-of-contents) )

---

## Contributing

Contributions are what make the open-source community so amazing. Any contribution you make is **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Top contributors:

<p align="center">
  <a href="https://contrib.rocks">
    <img src="https://contrib.rocks/image?repo=vishalbarai007/blood-bank-management-system" />
  </a>
   <a href="https://contrib.rocks">
    <img src="https://contrib.rocks/image?repo=srb114719/blood-bank-management-system" />
  </a>
</p>

( [Back to Top](#table-of-contents) )

---

## License

Distributed under the **Unlicense License**. See `LICENSE` for more information.

( [Back to Top](#table-of-contents) )

---

## Contact

Shravani Bhogle - shravanibhogle@gmail.com  
Vishal Barai - vishalbaraiofficial01@gmail.com

Project Link: [https://github.com/vishalbarai007/blood-bank-management-system](https://github.com/vishalbarai007/blood-bank-management-system)

( [Back to Top](#table-of-contents) )

---

## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/en/4.0/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Tkinter Official Docs](https://docs.python.org/3/library/tkinter.html)
- [SQLite Documentation](https://www.sqlite.org/)
- [Python Software Foundation](https://www.python.org/)

( [Back to Top](#table-of-contents) )

---
