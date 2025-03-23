# My Flask App

Welcome to **My Flask App**! This application allows you to manage tasks efficiently.

## Features

- Add, update, and delete tasks
- Mark tasks as complete or incomplete
- Beautiful and responsive UI

## Prerequisites

- Python 3.6+
- Virtual environment (recommended)

## Installation

1. **Clone the repository:**
   ```sh
   git clone git@github.com:normAlaskari/FlaskTask.git
   cd FlaskTask
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Running the App

1. **Initialize the database:**
   ```sh
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

2. **Run the Flask application:**
   ```sh
   flask run
   ```

3. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

## Screenshots

![Home Page](screenshots/home.png)
![Edit Task](screenshots/edit.png)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

---

Made with ❤️ by [Your Name](https://github.com/normAlaskari)