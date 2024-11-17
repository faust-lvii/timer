# reminders.py
import time
from persistence import load_reminders, save_reminders

class ReminderManager:
    def __init__(self):
        self.reminders = load_reminders() 

    def add_reminder(self, time_str, message):
        # Convert time_str to timestamp
        try:
            timestamp = self.convert_to_timestamp(time_str)
            self.reminders.append({"time": timestamp, "message": message})
            save_reminders(self.reminders)
        except ValueError as e:
            print(f"Error adding reminder: {e}")

    def convert_to_timestamp(self, time_str):
        try:
            # Parse HH:MM format
            if not ':' in time_str:
                raise ValueError("Time must be in HH:MM format")
            
            hours, minutes = map(int, time_str.split(':'))
            if not (0 <= hours <= 23 and 0 <= minutes <= 59):
                raise ValueError("Invalid hours or minutes")

            # Get current time components
            current_time = time.localtime()
            # Create a timestamp for today with the specified time
            future_time = time.mktime((
                current_time.tm_year,
                current_time.tm_mon,
                current_time.tm_mday,
                hours,
                minutes,
                0,  # seconds
                current_time.tm_wday,
                current_time.tm_yday,
                current_time.tm_isdst
            ))

            # If the time has already passed today, schedule for tomorrow
            if future_time <= time.time():
                future_time += 24 * 60 * 60  # Add 24 hours

            return future_time
        except Exception as e:
            raise ValueError(f"Invalid time format. Please use HH:MM (e.g., 14:30). Error: {str(e)}")

    def check_reminders(self, notification_func): 
        while True:
            try:
                current_time = time.time()
                reminders_to_remove = []

                for reminder in self.reminders:
                    if current_time >= reminder["time"]:
                        try:
                            notification_func("Reminder", reminder["message"])
                            reminders_to_remove.append(reminder)
                        except Exception as e:
                            print(f"Error sending notification: {str(e)}")

                # Remove processed reminders
                for reminder in reminders_to_remove:
                    self.reminders.remove(reminder)
                
                if reminders_to_remove:
                    save_reminders(self.reminders)

                # Sleep for a shorter interval for more precise timing
                time.sleep(10)
            except Exception as e:
                print(f"Error in reminder check loop: {str(e)}")
                time.sleep(60)  # Wait longer if there's an error