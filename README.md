# Melmi

**Melmi** is a Flask-based application designed to simplify the process of organizing group events. With Melmi, users can easily find common availability among a group of participants and select the best time for everyone. The app is designed to be intuitive and user-friendly, offering features like event creation, availability tracking, and automatic scheduling.

*I basically created this app because I was tired of not finding a date to meet with my friends (adult problems) and they don't know how to use doodle.*

## Features

- **Event Creation with Unique URL**: Create events and generate a unique URL to share with your friends.
- **Interactive Availability Input**: Participants can easily input their availability using an interactive calendar.
- **Dynamic Event Management**: The app dynamically updates to show the best available times based on participant input.
- **Conflict Management**: If no common time is available, the app suggests alternatives.
- **Slug-based URLs**: Events are accessible via user-friendly URLs based on event names.
- **Autocomplete for Names**: When entering availability, participants can select their names from a list of previously entered names to update their availability.

## Installation

### Prerequisites

- Python 3.7+
- Flask
- Flask-WTF
- Flask-SQLAlchemy
- Flask-Migrate
- Unidecode
- Jinja2
- jQuery
- FullCalendar

### Setup

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/melmi.git
    cd melmi
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:

    Initialize the database and apply migrations:

    ```sh
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. **Run the application**:

    ```sh
    # $env:FLASK_APP="src/app:create_app"
    flask run
    ```

    The app will be available at `http://127.0.0.1:5000`.

## Usage

### Creating an Event

1. Navigate to the home page and create a new event by entering the event name.
2. A unique URL will be generated based on the event name. If the event name already exists, a random suffix will be added to ensure uniqueness.
3. Share the URL with participants.

### Entering Availability

1. Participants can enter their availability using the interactive calendar.
2. If a participant's name already exists, their availability will be updated rather than duplicated.
3. The app automatically calculates the best common availability and displays it on the event page.

### Viewing and Managing Events

- The main event page displays the name of the event, the common availability, and the availability of all participants.
- The URL of the event is user-friendly, based on the event name, making it easy to share.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

### To contribute:

1. Fork the repository.
2. Create a new branch with your feature or bugfix.
3. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

*Happy organizing with Melmi!*