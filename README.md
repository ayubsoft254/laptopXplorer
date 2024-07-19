# laptopXplorer

## Description

The Student Management System is a Django-based web application designed to manage student records. It allows administrators to perform CRUD (Create, Read, Update, Delete) operations on student data, including details like first name, last name, email, phone number, and course.

## Features

- **List Students:** View a list of all students with their details.
- **Add Student:** Add new students to the system.
- **Update Student:** Modify existing student information.
- **Delete Student:** Remove students from the database.
- **Search Students:** Search for students based on various criteria (first name, last name, email, course, phone).

## Technologies Used

- **Backend:** Django, Python
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default for Django development)
- **Version Control:** Git, GitHub

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ayubsoft254/Student_Management.git
   cd Student_Management
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` (login with superuser credentials).
- Use the provided views and forms to manage student records.
- Navigate to `http://127.0.0.1:8000/` to view and interact with the student management interface.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or fixes.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
