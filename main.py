# main.py
import customtkinter as ctk
import threading
from clock import ModernClock
from reminders import ReminderManager
from notifications import send_notification
import sys
from datetime import datetime
import json
import os
import time

def main():
    # Tema ayarları
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.title("Modern Reminder")
    root.geometry("700x900")
    root.minsize(400, 600)
    
    # Gradient arka plan için frame
    main_container = ctk.CTkFrame(root, fg_color="#0a0a0a")
    main_container.pack(fill="both", expand=True)

    # Başlık
    title_frame = ctk.CTkFrame(main_container, fg_color="transparent")
    title_frame.pack(pady=20, fill="x")
    
    title_label = ctk.CTkLabel(
        title_frame,
        text="Modern Reminder",
        font=ctk.CTkFont(family="Helvetica", size=32, weight="bold"),
        text_color="#ffffff"
    )
    title_label.pack()

    # Modern saat widget'ı
    clock = ModernClock(main_container)
    clock.pack(pady=30, fill="x")

    # Hatırlatıcı bölümü
    reminder_frame = ctk.CTkFrame(
        main_container,
        fg_color="#1a1a1a",
        corner_radius=15
    )
    reminder_frame.pack(padx=40, pady=20, fill="x")

    reminder_title = ctk.CTkLabel(
        reminder_frame,
        text="Yeni Hatırlatıcı Ekle",
        font=ctk.CTkFont(size=20, weight="bold"),
        text_color="#ffffff"
    )
    reminder_title.pack(pady=(20, 10))

    # Zaman girişi frame'i
    time_input_frame = ctk.CTkFrame(reminder_frame, fg_color="transparent")
    time_input_frame.pack(pady=5)

    # Saat girişi
    hours_frame = ctk.CTkFrame(time_input_frame, fg_color="transparent")
    hours_frame.pack(side="left", padx=5)
    
    hours_label = ctk.CTkLabel(
        hours_frame,
        text="Saat",
        font=ctk.CTkFont(size=14),
        text_color="#888888"
    )
    hours_label.pack()
    
    hours_entry = ctk.CTkEntry(
        hours_frame,
        placeholder_text="00-23",
        width=60,
        height=30,
        corner_radius=10,
        border_width=2,
        justify="center",
        font=ctk.CTkFont(size=16),
        fg_color="#2d2d2d",
        text_color="#ffffff",
        border_color="#888888"
    )
    hours_entry.pack()

    # İki nokta label
    colon_label = ctk.CTkLabel(
        time_input_frame,
        text=":",
        font=ctk.CTkFont(size=24, weight="bold"),
        text_color="#4CAF50"
    )
    colon_label.pack(side="left", pady=20)

    # Dakika girişi
    minutes_frame = ctk.CTkFrame(time_input_frame, fg_color="transparent")
    minutes_frame.pack(side="left", padx=5)
    
    minutes_label = ctk.CTkLabel(
        minutes_frame,
        text="Dakika",
        font=ctk.CTkFont(size=14),
        text_color="#888888"
    )
    minutes_label.pack()
    
    minutes_entry = ctk.CTkEntry(
        minutes_frame,
        placeholder_text="00-59",
        width=60,
        height=30,
        corner_radius=10,
        border_width=2,
        justify="center",
        font=ctk.CTkFont(size=16)
    )
    minutes_entry.pack()

    # Mesaj girişi
    message_frame = ctk.CTkFrame(reminder_frame, fg_color="transparent")
    message_frame.pack(pady=10)
    
    message_label = ctk.CTkLabel(
        message_frame,
        text="Hatırlatıcı Mesajı",
        font=ctk.CTkFont(size=14),
        text_color="#888888"
    )
    message_label.pack()
    
    message_entry = ctk.CTkEntry(
        message_frame,
        placeholder_text="Mesajınızı girin",
        width=300,
        height=40,
        corner_radius=10,
        border_width=2,
        font=ctk.CTkFont(size=14)
    )
    message_entry.pack()

    # Durum mesajı için label
    status_label = ctk.CTkLabel(
        reminder_frame,
        text="",
        font=ctk.CTkFont(size=14)
    )
    status_label.pack(pady=5)

    # Hatırlatıcı ekleme butonu
    add_button = ctk.CTkButton(
        reminder_frame,
        text="Hatırlatıcı Ekle",
        command=lambda: on_add_reminder(),
        width=150,
        height=35,
        corner_radius=10,
        font=ctk.CTkFont(size=15, weight="bold"),
        fg_color="#333333",
        hover_color="#404040"
    )
    add_button.pack(pady=10)

    reminder_manager = ReminderManager()

    # Aktif hatırlatıcılar bölümü
    reminders_container = ctk.CTkFrame(
        main_container,
        fg_color="#1a1a1a",
        corner_radius=15
    )
    reminders_container.pack(padx=40, pady=20, fill="both", expand=True)

    reminders_label = ctk.CTkLabel(
        reminders_container,
        text="Aktif Hatırlatıcılar",
        font=ctk.CTkFont(size=18, weight="bold"),
        text_color="#ffffff"
    )
    reminders_label.pack(pady=10)

    # Scrollable frame for reminders
    reminders_scroll = ctk.CTkScrollableFrame(
        reminders_container,
        fg_color="#2B2B2B",
        height=200
    )
    reminders_scroll.pack(fill="both", expand=True)

    def update_reminders_list():
        # Önce mevcut hatırlatıcıları temizle
        for widget in reminders_scroll.winfo_children():
            widget.destroy()
            
        # Hatırlatıcıları listele
        for index, reminder in enumerate(reminder_manager.get_reminders()):
            reminder_frame = ctk.CTkFrame(
                reminders_scroll,
                fg_color="#2d2d2d",
                corner_radius=10
            )
            reminder_frame.pack(fill="x", padx=5, pady=5)
            
            time_label = ctk.CTkLabel(
                reminder_frame,
                text=f"⏰ {reminder['time']}",
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color="#ffffff"
            )
            time_label.pack(side="left", padx=15, pady=10)
            
            message_label = ctk.CTkLabel(
                reminder_frame,
                text=reminder['message'],
                font=ctk.CTkFont(size=13, weight="bold"),
                text_color="#888888"
            )
            message_label.pack(side="left", padx=10, pady=10)
            
            # Kaldır butonu
            def delete_reminder(idx=index):
                reminder_manager.remove_reminder(idx)
                update_reminders_list()
                save_reminders()  # Değişiklikleri kaydet
            
            delete_button = ctk.CTkButton(
                reminder_frame,
                text="❌",
                width=30,
                height=30,
                corner_radius=15,
                fg_color="#444444",
                hover_color="#666666",
                command=delete_reminder
            )
            delete_button.pack(side="right", padx=10, pady=5)

    def validate_time(hours, minutes):
        try:
            h = int(hours)
            m = int(minutes)
            return (0 <= h <= 23) and (0 <= m <= 59)
        except ValueError:
            return False

    def on_add_reminder():
        hours = hours_entry.get()
        minutes = minutes_entry.get()
        message = message_entry.get()
        
        if hours and minutes and message:  # Tüm alanlar dolu mu?
            if validate_time(hours, minutes):  # Geçerli saat ve dakika mı?
                time_str = f"{int(hours):02d}:{int(minutes):02d}"
                reminder_manager.add_reminder(time_str, message)
                hours_entry.delete(0, "end")
                minutes_entry.delete(0, "end")
                message_entry.delete(0, "end")
                status_label.configure(
                    text="Hatırlatıcı başarıyla eklendi!",
                    text_color="green"
                )
                update_reminders_list()
            else:
                status_label.configure(
                    text="Geçersiz saat veya dakika! (Saat: 0-23, Dakika: 0-59)",
                    text_color="red"
                )
        else:
            status_label.configure(
                text="Lütfen tüm alanları doldurun!",
                text_color="red"
            )

    # Hatırlatıcıları kaydetme ve yükleme fonksiyonları
    def save_reminders():
        with open('reminders.json', 'w') as f:
            json.dump(reminder_manager.reminders, f)

    def load_reminders():
        if os.path.exists('reminders.json'):
            with open('reminders.json', 'r') as f:
                reminder_manager.reminders = json.load(f)
            update_reminders_list()

    # Uygulama kapatılırken hatırlatıcıları kaydet
    def on_closing():
        save_reminders()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    # Başlangıçta hatırlatıcıları yükle
    load_reminders()

    def start_reminder_thread():
        def run_check():
            while True:
                try:
                    current_time = datetime.now()
                    current_time_str = current_time.strftime("%H:%M")
                    
                    for reminder in reminder_manager.get_reminders():
                        if reminder['active'] and reminder['time'] == current_time_str:
                            send_notification(
                                title="⏰ Hatırlatıcı Zamanı!",
                                message=f"🔔 {reminder['message']}"
                            )
                            reminder['active'] = False
                            save_reminders()  # Durumu kaydet
                    
                    # Günlük sıfırlama
                    if current_time.strftime("%H:%M") == "00:00":
                        for reminder in reminder_manager.get_reminders():
                            reminder['active'] = True
                        save_reminders()
                    
                    time.sleep(1)
                except Exception as e:
                    print(f"Hatırlatıcı hatası: {e}")
                    time.sleep(1)

        reminder_thread = threading.Thread(target=run_check, daemon=True)
        reminder_thread.start()

    # Ana pencere oluşturulduktan sonra thread'i başlat
    start_reminder_thread()

    root.mainloop()

if __name__ == "__main__":
    main()