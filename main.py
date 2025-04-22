import tkinter as tk
import psutil

def update_loop():
    cpu_percent = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
    ram_label.config(text=f"RAM: {ram}%")
    disk_label.config(text=f"Disk: {disk}%")

    frame.after(1000, update_loop)  # Refresh every 1000ms (1 second)

frame = tk.Tk()
frame.title("CPU Monitor")

cpu_label = tk.Label(frame, text="CPU Usage: ", font=("Helvetica", 14))
cpu_label.pack(side=tk.LEFT, pady=21)

ram_label = tk.Label(frame, text="RAM: ", font=("Helvetica", 14))
ram_label.pack(side=tk.LEFT, padx=10)

disk_label = tk.Label(frame, text="Disk: ", font=("Helvetica", 14))
disk_label.pack(side=tk.LEFT, padx=10)

update_loop()  # Initial call to start the loop

frame.mainloop()
