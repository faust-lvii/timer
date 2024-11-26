# reminders.py
import time
from datetime import datetime
import json

class ReminderManager:
    def __init__(self):
        self.reminders = []
    
    def add_reminder(self, time_str, message):
        self.reminders.append({
            'time': time_str,
            'message': message,
            'active': True
        })
    
    def get_reminders(self):
        return self.reminders
    
    def check_reminders(self, notification_callback):
        while True:
            current_time = datetime.now()
            current_time_str = current_time.strftime("%H:%M")
            
            for reminder in self.reminders:
                if reminder['active'] and reminder['time'] == current_time_str:
                    notification_callback(
                        title="Hatırlatıcı",
                        message=reminder['message']
                    )
                    reminder['active'] = False  # Bir kez bildirim verdikten sonra deaktif et
            
            time.sleep(30)  # Her 30 saniyede bir kontrol et
    
    def remove_reminder(self, index):
        if 0 <= index < len(self.reminders):
            self.reminders.pop(index)