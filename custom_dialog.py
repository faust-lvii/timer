import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox

class CustomDatePickerDialog(tk.Toplevel):
    def __init__(self, parent=None, title="Select Date and Time"):
        super().__init__(parent)
        self.title(title)
        self.result = None
        
        # Make dialog modal
        self.transient(parent)
        self.grab_set()
        
        # Create the widgets
        self.create_widgets()
        
        # Center the dialog
        self.geometry("+%d+%d" % (parent.winfo_rootx() + 50,
                                 parent.winfo_rooty() + 50))
        
    def create_widgets(self):
        # Create main frame
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Date entry
        now = datetime.now()
        
        # Date spinboxes
        date_frame = ttk.Frame(main_frame)
        date_frame.grid(row=0, column=0, pady=5)
        
        self.year_var = tk.StringVar(value=str(now.year))
        self.month_var = tk.StringVar(value=str(now.month))
        self.day_var = tk.StringVar(value=str(now.day))
        
        ttk.Label(date_frame, text="Year:").grid(row=0, column=0)
        self.year_sb = ttk.Spinbox(date_frame, from_=2024, to=2100, width=6,
                                  textvariable=self.year_var)
        self.year_sb.grid(row=0, column=1, padx=2)
        
        ttk.Label(date_frame, text="Month:").grid(row=0, column=2)
        self.month_sb = ttk.Spinbox(date_frame, from_=1, to=12, width=4,
                                   textvariable=self.month_var)
        self.month_sb.grid(row=0, column=3, padx=2)
        
        ttk.Label(date_frame, text="Day:").grid(row=0, column=4)
        self.day_sb = ttk.Spinbox(date_frame, from_=1, to=31, width=4,
                                 textvariable=self.day_var)
        self.day_sb.grid(row=0, column=5, padx=2)
        
        # Time spinboxes
        time_frame = ttk.Frame(main_frame)
        time_frame.grid(row=1, column=0, pady=5)
        
        self.hour_var = tk.StringVar(value=str(now.hour))
        self.minute_var = tk.StringVar(value=str(now.minute))
        
        ttk.Label(time_frame, text="Hour:").grid(row=0, column=0)
        self.hour_sb = ttk.Spinbox(time_frame, from_=0, to=23, width=4,
                                  textvariable=self.hour_var)
        self.hour_sb.grid(row=0, column=1, padx=2)
        
        ttk.Label(time_frame, text="Minute:").grid(row=0, column=2)
        self.minute_sb = ttk.Spinbox(time_frame, from_=0, to=59, width=4,
                                    textvariable=self.minute_var)
        self.minute_sb.grid(row=0, column=3, padx=2)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, pady=10)
        
        ttk.Button(button_frame, text="OK", command=self.ok).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Cancel", command=self.cancel).grid(row=0, column=1, padx=5)
    
    def ok(self):
        try:
            # Validate and create datetime object
            dt = datetime(
                int(self.year_var.get()),
                int(self.month_var.get()),
                int(self.day_var.get()),
                int(self.hour_var.get()),
                int(self.minute_var.get())
            )
            self.result = dt
            self.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid date and time values")
    
    def cancel(self):
        self.result = None
        self.destroy()
    
    def get_date(self):
        return self.result
