# clock.py
import customtkinter as ctk
from datetime import datetime
import math

class ModernClock(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        # Renk paleti
        self.COLORS = {
            'bg': "#1a1a1a",
            'text_bright': "#ffffff",
            'text_dim': "#888888"
        }
        
        # Saat container'ı
        self.clock_container = ctk.CTkFrame(
            self,
            fg_color=self.COLORS['bg'],
            corner_radius=20
        )
        self.clock_container.pack(pady=20, padx=20)
        
        # Dijital saat gösterimi
        self.time_frame = ctk.CTkFrame(
            self.clock_container,
            fg_color="transparent"
        )
        self.time_frame.pack(pady=20, padx=30)
        
        # Saat
        self.hours_label = ctk.CTkLabel(
            self.time_frame,
            text="00",
            font=ctk.CTkFont(size=80, weight="bold"),
            text_color=self.COLORS['text_bright']
        )
        self.hours_label.pack(side="left", padx=10)
        
        # İki nokta
        self.colon = ctk.CTkLabel(
            self.time_frame,
            text=":",
            font=ctk.CTkFont(size=80, weight="bold"),
            text_color=self.COLORS['text_dim']
        )
        self.colon.pack(side="left")
        
        # Dakika
        self.minutes_label = ctk.CTkLabel(
            self.time_frame,
            text="00",
            font=ctk.CTkFont(size=80, weight="bold"),
            text_color=self.COLORS['text_bright']
        )
        self.minutes_label.pack(side="left", padx=10)
        
        # Tarih gösterimi
        self.date_label = ctk.CTkLabel(
            self.clock_container,
            text="",
            font=ctk.CTkFont(size=16),
            text_color=self.COLORS['text_dim']
        )
        self.date_label.pack(pady=(0, 20))
        
        self.update_clock()
    
    def update_clock(self):
        current_time = datetime.now()
        
        self.hours_label.configure(text=f"{current_time.hour:02d}")
        self.minutes_label.configure(text=f"{current_time.minute:02d}")
        
        date_str = current_time.strftime("%d %B %Y, %A")
        self.date_label.configure(text=date_str)
        
        # İki nokta animasyonu
        self.colon.configure(
            text_color=self.COLORS['text_bright'] 
            if current_time.second % 2 == 0 
            else self.COLORS['text_dim']
        )
        
        self.after(1000, self.update_clock)