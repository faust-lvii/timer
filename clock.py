# clock.py
import customtkinter as ctk
from datetime import datetime
import math

class ModernClock(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Saat container'ı
        self.clock_container = ctk.CTkFrame(self, fg_color="transparent")
        self.clock_container.pack(pady=20)
        
        # Dijital saat gösterimi
        self.time_frame = ctk.CTkFrame(self.clock_container, fg_color="#2B2B2B")
        self.time_frame.pack(pady=10)
        
        # Saat
        self.hours_label = ctk.CTkLabel(
            self.time_frame,
            text="00",
            font=ctk.CTkFont(size=60, weight="bold"),
            text_color="#4CAF50"
        )
        self.hours_label.pack(side="left", padx=10)
        
        # İki nokta
        self.colon = ctk.CTkLabel(
            self.time_frame,
            text=":",
            font=ctk.CTkFont(size=60, weight="bold"),
            text_color="#FFFFFF"
        )
        self.colon.pack(side="left")
        
        # Dakika
        self.minutes_label = ctk.CTkLabel(
            self.time_frame,
            text="00",
            font=ctk.CTkFont(size=60, weight="bold"),
            text_color="#4CAF50"
        )
        self.minutes_label.pack(side="left", padx=10)
        
        # Tarih gösterimi
        self.date_label = ctk.CTkLabel(
            self.clock_container,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="#888888"
        )
        self.date_label.pack(pady=5)
        
        self.update_clock()
    
    def update_clock(self):
        current_time = datetime.now()
        
        # Saat ve dakika güncelleme
        self.hours_label.configure(text=f"{current_time.hour:02d}")
        self.minutes_label.configure(text=f"{current_time.minute:02d}")
        
        # Tarih güncelleme
        date_str = current_time.strftime("%d %B %Y, %A")
        self.date_label.configure(text=date_str)
        
        # Her saniyede bir güncelle
        self.after(1000, self.update_clock)