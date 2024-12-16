## CLI project

This CLI application allows you to manage a database of Technical Mentors (TMs) and their assigned students. It uses SQLAlchemy ORM for database operations and follows the CRUD (Create, Read, Update, Delete) principles.

## Installation

1.  Clone the repository: git clone https://github.com/your-username/new_cli.git
2.  Navigate to the project directory: cd new_cli
3.  Create a virtual environment (optional): python3 -m venv venv
4.  Activate the virtual environment (optional): source venv/bin/activate
5.  Install the required packages: pip install -r requirements.txt

## Usage

1.  Run the application: python cli.py
2.  Follow the prompts to perform the desired operations:
    Create TMs
    Update TMs
    Delete TMs
    Create Students
    Update Students
    Delete Students
    Assign Students to TMs
    List all TMs
    List all Students
    View Students by TM
    Exit the application

## Database

The application uses a SQLite database named tms.db. The database schema is defined using SQLAlchemy ORM in the models.py file.

## Code Structure

The code is organized into the following files:

- cli.py: The main entry point for the CLI application. It defines the functions for creating, updating, deleting TMs and students, as well as the main menu and database initialization.
- models.py: Defines the SQLAlchemy ORM models for TMs and Students. It also creates the database engine and session.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request.
