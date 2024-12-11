# Reminder Application

The Reminder Application is a desktop software that allows users to add and manage reminders. Users can set reminders for specific times and receive notifications when those reminders are due.

## Features

- **User-Friendly Interface:** Intuitive and straightforward design for ease of use.
- **Time Input:** Allows users to enter hours (0-23) and minutes (0-59).
- **Custom Reminder Messages:** Users can add personalized messages for their reminders.
- **Active Reminders Display:** Users can view their current active reminders.
- **Reminder Deletion:** Easily remove unwanted reminders with a click.
- **Data Management:** Saves and loads reminders when the application is closed.
- **Daily Reset:** Automatically activates reminders at the start of each day.

## Requirements

- **Python 3.x**
- `customtkinter` library
- `clock` module
- `reminders` module
- `notifications` module

## Installation

1. Clone or download the project:
   ```bash:clock.py
   git clone https://github.com/faust-lvii/timer
   cd timer
   ```

2. Install the required libraries:
   ```bash
   pip install customtkinter
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage

1. After launching the application, navigate to the "Add New Reminder" section.
2. Enter the time (hours 0-23, minutes 0-59).
3. Input your reminder message.
4. Click the "Add Reminder" button.
5. View your added reminders in the active reminders section.
6. To delete a reminder, click the ❌ button.

## Contributing

If you would like to contribute to this project, please create a pull request or report any issues. All contributions and feedback are welcome and appreciated.

## License

This project is licensed under the [MIT License](LICENSE).