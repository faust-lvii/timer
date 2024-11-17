# main.py
import os
import tkinter as tk
from tkinter import ttk
import threading
from clock import AnalogClock
from reminders import ReminderManager
from notifications import send_notification
from custom_dialog import CustomDatePickerDialog

def main():
    root = tk.Tk()
    root.title("Reminder Clock")
    
    style = ttk.Style()
    style.theme_use('clam')  # Using the 'clam' theme for a modern look

    clock = AnalogClock(root, width=200, height=200)
    clock.pack(pady=20)
    clock.start()

    reminder_manager = ReminderManager()

    # Hatırlatıcı eklemek için etiketler ve giriş alanları
    time_label = ttk.Label(root, text="Zaman (SS:DD):")
    time_label.pack()
    time_entry = ttk.Entry(root)
    time_entry.pack()

    message_label = ttk.Label(root, text="Mesaj:")
    message_label.pack()
    message_entry = ttk.Entry(root)
    message_entry.pack()

    # --- Define on_add_reminder BEFORE using it ---
    def on_add_reminder():
        time_str = time_entry.get()  # Zaman girişinden değeri als
        message = message_entry.get() # Mesaj girişinden değeri al
        reminder_manager.add_reminder(time_str, message)
        time_entry.delete(0, tk.END)  # Giriş alanlarını temizle
        message_entry.delete(0, tk.END)

    # Hatırlatıcı ekleme düğmesi (ttkbootstrap stilleri ile)
    add_button = ttk.Button(root, text="Hatırlatıcı Ekle")
    add_button.pack()

    # Background thread for checking reminders
    reminder_thread = threading.Thread(target=reminder_manager.check_reminders, 
                                        args=(send_notification,))
    reminder_thread.daemon = True
    reminder_thread.start()

    root.mainloop()

if __name__ == "__main__":
    main()