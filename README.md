# JedanCare - Flask Web Application

JedanCare is  web application developed using Flask, a micro web framework in Python. The application offers features for managing medical appointments, user authentication, and an admin dashboard for administration.

![Project Completion](https://img.shields.io/badge/Project%20Completion-45%25%20Complete-brightgreen) ![Tests](https://github.com/solomonkassa/Jedan-Care/workflows/Tests/badge.svg) ![Development](https://img.shields.io/badge/Development-In%20Progress-yellow)



🏥 **Features:**

- **Effortless Scheduling:** Seamlessly schedule medical appointments with an intuitive interface.
- **Secure Authentication:** Prioritize security with a reliable user authentication system.
- **Admin Dashboard:** Empower administrators to manage appointments, doctors, and departments.
- **Responsive Design:** Enjoy a smooth experience on any device, from desktops to mobiles.

🚀 **Use Cases:**

- **Patients:** Conveniently book appointments and access appointment history.
- **Doctors:** Manage appointments, availability, and patient communication.
- **Administrators:** Oversee the scheduling process and optimize healthcare services.


## Project Structure

The project follows a modular structure using Flask blueprints:

- `app`: Contains the main application setup, configuration, models, and blueprints.
- `app/blueprints/main`: Handles main routes and user-facing features.
- `app/blueprints/auth`: Manages user authentication and registration.
- `app/blueprints/admin`: Provides admin dashboard and management features.
- `run.py`: Script to run the Flask application.
- `requirements.txt`: List of required Python packages.

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/solomonkassa/JedanCare.git
   ```
2. Navigate to the project directory:
   ```
   cd JedanCare
   ```
3. Create a virtual environment:
   ```
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```
5. Install required packages:
   ```
   pip install -r requirements.txt
   ```
6. Initialize the database:
   ```
   python run.py db init
   ```
7. Apply database migrations:
   ```
   python run.py db migrate
   ```
8. Apply migrations to the database:
   ```
   python run.py db upgrade
   ```
9. Run the application:
   ```
    python run.py runserver
   ```

🔨 **Project Progress:**

- [x] Setup Flask application structure.
- [x] Implement user authentication and registration.
- [x] Create appointment scheduling form.
- [ ] Build admin dashboard for appointments and doctors.
- [ ] Enhance security and validation features.
- [ ] Deploy to production environment for real-world usage.

## Usage

- Access the application by visiting `http://localhost:5000` in your browser.
- Patients can schedule appointments by filling out the appointment form.
- Admins can log in to the admin dashboard to manage appointments, doctors, and departments.


## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m "Add your message"`
4. Push to your branch: `git push origin feature-name`
5. Create a pull request from your branch to the main repository.

## License

This project is licensed under the [GNU Affero General Public License (AGPL-3.0)](LICENSE). This license requires sharing modifications and derivative works under the same license.

