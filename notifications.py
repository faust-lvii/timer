# notifications.py
from plyer import notification
import platform
import os

def send_notification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_icon=None,  # Buraya bir icon path ekleyebilirsiniz
            timeout=10,
        )
    except Exception as e:
        print(f"Bildirim gönderilemedi: {e}")