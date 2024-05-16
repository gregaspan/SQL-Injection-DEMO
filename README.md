## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/gregaspan/SQL-Injection-DEMO.git
    cd project-name
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment:**

    - On macOS and Linux:

        ```bash
        source env/bin/activate
        ```

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

4. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1. **Seed the database with default users:**

    ```bash
    python seed.py
    ```

## Running the Application

1. **Start the Flask application:**

    ```bash
    flask run
    ```

    The application should now be running at `http://127.0.0.1:5000/`.
