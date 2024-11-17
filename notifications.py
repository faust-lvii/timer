# notifications.py
from plyer import notification
import platform
import subprocess
import time

def send_notification(title, message, timeout=10):
    try:
        # Try using plyer first
        notification.notify(
            title=title,
            message=message,
            app_name="ReminderClock",
            timeout=timeout
        )
    except Exception as e:
        print(f"Primary notification method failed: {str(e)}")
        try:
            # Fallback to platform-specific methods
            system = platform.system().lower()
            
            if system == "windows":
                # Windows fallback using PowerShell
                powershell_script = f'powershell -Command "& {{Add-Type -AssemblyName System.Windows.Forms; $notify = New-Object System.Windows.Forms.NotifyIcon; $notify.Icon = [System.Drawing.SystemIcons]::Information; $notify.Visible = $true; $notify.ShowBalloonTip(10, \'{title}\', \'{message}\', [System.Windows.Forms.ToolTipIcon]::None)}}"'
                subprocess.run(powershell_script, shell=True)
            
            elif system == "darwin":  # macOS
                subprocess.run(["osascript", "-e", f'display notification "{message}" with title "{title}"'])
            
            elif system == "linux":
                # Linux fallback using notify-send
                subprocess.run(["notify-send", title, message])
            
        except Exception as fallback_error:
            print(f"Fallback notification method failed: {str(fallback_error)}")
            # Last resort: print to console
            print(f"\nNOTIFICATION:\nTitle: {title}\nMessage: {message}\n")