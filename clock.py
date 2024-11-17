# clock.py
import tkinter as tk
import time
import math

class AnalogClock(tk.Canvas):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width=width, height=height, bg="black", **kwargs)
        self.width = width
        self.height = height
        self.running = False

    def start(self):
        self.running = True
        self._update_clock()

    def stop(self):
        self.running = False

    def _update_clock(self):
        if not self.running:
            return

        self.delete("all")
        now = time.localtime()
        hour, minute, second = now.tm_hour, now.tm_min, now.tm_sec

        # Clock center
        center_x = self.width / 2
        center_y = self.height / 2
        radius = min(center_x, center_y) - 10

        # Draw clock face
        self.create_oval(center_x - radius, center_y - radius, 
                        center_x + radius, center_y + radius, 
                        outline="white", width=2)

        # Draw hour markers
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            marker_length = 10 if i % 3 == 0 else 5
            start_x = center_x + (radius - marker_length) * math.cos(angle)
            start_y = center_y + (radius - marker_length) * math.sin(angle)
            end_x = center_x + radius * math.cos(angle)
            end_y = center_y + radius * math.sin(angle)
            self.create_line(start_x, start_y, end_x, end_y, fill="white")

        # Draw clock hands
        # Hour hand
        hour_angle = math.radians((hour % 12 + minute / 60) * 30 - 90)
        hour_length = radius * 0.5
        self.create_line(center_x, center_y,
                        center_x + hour_length * math.cos(hour_angle),
                        center_y + hour_length * math.sin(hour_angle),
                        fill="white", width=4)

        # Minute hand
        minute_angle = math.radians(minute * 6 - 90)
        minute_length = radius * 0.7
        self.create_line(center_x, center_y,
                        center_x + minute_length * math.cos(minute_angle),
                        center_y + minute_length * math.sin(minute_angle),
                        fill="white", width=3)

        # Second hand
        second_angle = math.radians(second * 6 - 90)
        second_length = radius * 0.8
        self.create_line(center_x, center_y,
                        center_x + second_length * math.cos(second_angle),
                        center_y + second_length * math.sin(second_angle),
                        fill="red", width=1)

        # Center dot
        self.create_oval(center_x-4, center_y-4, center_x+4, center_y+4, fill="white")

        self.after(1000, self._update_clock)