# Hirafic Project
![Hirafic Project Logo](Client/src/assets/readme.jpg)

Hirafic is a web application that connects clients with artisans. The project consists of a backend server built with Flask and a frontend client built with React.

## Table of Contents

- [Motivation](#motivation)
- [Authors](#authors)
- [Technologies Used](#technologies-used)
    - [Backend](#backend)
    - [Frontend](#frontend)
    - [Authentication](#authentication)
    - [Additional Technologies](#additional-technologies)
- [Features](#features)
- [Challenges](#challenges)
- [Future Enhancements](#future-enhancements)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
    - [Backend](#backend-1)
    - [Frontend](#frontend-1)
- [Running the Application](#running-the-application)
    - [Backend](#backend-2)
    - [Frontend](#frontend-2)
- [Contributing](#contributing)
- [License](#license)

## Motivation 💡

The Hirafic project was created to bridge the gap between clients and artisans by providing a seamless platform for booking and managing services. The goal is to empower local artisans by giving them a digital presence and making it easier for clients to find and book their services.
 
## Authors:
### Backend Developers
- **Duaa Obeid**    [GitHub](https://github.com/duaarabie) | [LinkedIn](https://www.linkedin.com/in/duaarabie)
- **Oliver Maketso**    [GitHub](https://github.com/OliverMaketso)

###  Frontend Developers
- **Paul Levites**  [GitHub](https://github.com/Paulcode2) | [LinkedIn](https://linkedin.com/in/paul-ifeoluwa-levites)
- **Selasi Agbenyegah Mensah**  [GitHub](https://github.com/Selasi-Mensah)

## Technologies Used 🛠️

#### Backend
- **Languages**: Python
- **Frameworks**: Flask, Flask-SQLAlchemy
- **Caching**: Redis
- **Code Quality**: pycodestyle
#### Frontend
- **Libraries**: React
- **HTTP Client**: Axios
#### Authentication
- **Method**: JWT (JSON Web Tokens)
#### Additional Technologies
- **Version Control**: Git
- **Testing**: pytest

## Features
- **User Authentication and Authorization**: Secure login and registration for both clients and artisans using JWT.
- **Artisan and Client Profiles**: Detailed profiles for artisans and clients, including personal information and service details, with the ability to update them.
- **Booking System**: Clients can book artisans for services, with real-time updates and notifications.
- **Real-Time Email Notifications**: Automated email notifications for bookings, cancellations, and updates.
- **Direct Communication**: In-app messaging system for clients and artisans to communicate directly.
- **Booking Feature**: Clients and artisans can manage and view their bookings. Clients can book services and track the status of their bookings, including pending, confirmed, rejected, and completed. Artisans can update the status of bookings.
- **Search and Filter Feature**: Clients can search for artisans based on distance and filter them by specialization.
- **Report Feature**: Allow clients to report artisans.
- **Map or List View**: Clients can view artisans and their information on a map or in a list format.

## Challenges 🚧

- **Authentication**: Implementing JWT for stateless authentication presented challenges, especially with newer versions that had issues related to verifying the `sub` claim.
- **Scalability**: Ensuring the application could handle an increasing number of users and bookings required adhering to best practices for database design.
- **Performance**: To enhance performance, we optimized queries and database interactions, avoided the use of database listeners, and kept future growth in mind.
- **Security**: Protecting user data and ensuring secure transactions was a top priority.
- **Integration**: Seamlessly integrating various third-party services and APIs required cross-platform compatibility and the use of CORS.
- **Non-Technical Challenges**: Coordinating meetings and communication was difficult due to the team's diverse cultures, languages, and time zones. Additionally, the limited time available posed a significant challenge.


## Future Enhancements 🚀

- **Rating and Review System**: Allow clients to rate and review artisans.
- **Payment Integration**: Integrate payment gateways for secure online transactions.
- **Calendar Integration**: Sync bookings with popular calendar applications like Google Calendar and Outlook.
- **System Support**: Improve the Reporting feature and provide an advance customer support to assist users with any issues or inquiries.
- **Multilingual Support**: Add support for multiple languages to cater to a broader audience.
- **AI Recommendations**: Use machine learning to recommend artisans to clients based on their preferences and booking history.
- **Mobile Application**: Develop a mobile app for both Android and iOS platforms.

## Project Structure

```bash
Hirafic-project/
├── backend/
│   ├── __init__.py
│   ├── run.py
│   ├── config.py
│   ├── extensions.py
│   ├── requirements.txt
│   ├── models/
│   │   ├── __init__.py
│   │   ├── artisan.py
│   │   ├── base.py
│   │   ├── booking.py 
│   │   ├── client.py
│   │   ├── report.py
│   │   └── user.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── artisan.py
│   │   ├── auth.py
│   │   ├── booking.py
│   │   ├── client.py
│   │   └── handlers.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_forms/
│   │   │   ├── __init__.py
│   │   │   ├── test_auth.py
│   │   │   ├── test_artisan.py
│   │   │   └── test_client.py
│   │   ├── test_models/
│   │   │   ├── __init__.py
│   │   │   ├── test_base.py
│   │   │   ├── test_user.py
│   │   │   ├── test_artisan.py
│   │   │   ├── test_client.py
│   │   │   └── test_booking.py
│   │   ├──test_routes/
│   │   │   ├── __init__.py
│   │   │   ├── test_auth.py
│   │   │   ├── test_artisan.py
│   │   │   ├── test_client.py
│   │   │   └── test_handlers.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── email_service.py
├── Client/
│   ├── package.json
│   ├── package-lock.json
│   └── ...
└── README.md
```

## Prerequisites 📋 
- Python 3.12
- pip
- Node.js (v18.3.1 or higher)
- npm or yarn
- Redis server

## Installation ⚙️

### Backend

1. **Clone the repository**:

```sh
git clone https://github.com/Selasi-Mensah/Hirafic-project
cd Hirafic-project/backend
```

2. **Create a virtual environment and activate it**:
Use your preferred way to create a virtual environment:
You can use:

```sh
python3 -m venv myenv
source myenv/bin/activate
```

3. **Install the required Python packages**:

```sh
pip install -r requirements.txt
```

4. **Set up the database**:

```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Frontend

1. **Navigate to the client directory**:

```sh
cd ../Client
```

2. **install the required npm packages**:

```sh
npm install
# Or
yarn install
```

## Running the Application

### Backend

1. **Start the Redis server**:

```sh
redis-server
```

2. **Start the Flask server**:

```sh
flask run
```

### Frontend

1. **Start the React development server**:

```sh
npm run dev
```

## Contributing 🤝

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes with a conventional commit(`git commit -m '<type>[optional_scope]: <description>'...`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Explanation

1. **Features**: Lists the main features of the project.
2. **Project Structure**: Provides an overview of the project's directory structure.
3. **Prerequisites**: Lists the software and tools required to run the project.
4. **Installation**: Detailed steps to set up the backend and frontend of the project.
5. **Running the Application**: Instructions to start the backend and frontend servers, including running both servers concurrently.
6. **API Endpoints**: Lists the available API endpoints for authentication, booking, and profile management.
7. **Contributing**: Guidelines for contributing to the project.
8. **License**: Information about the project's license.

### Summary

This `README.md` file provides a comprehensive guide to setting up, running, and contributing to the Hirafic project. It includes detailed instructions and explanations for each step, ensuring that users and contributors can easily understand and work with the project. Adjust the content as needed to fit your specific project details.

