import tkinter as tk
import psutil


class SystemMonitorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("System Monitor")
        self.root.geometry("800x400")

        self.metrics = self.init()


    def init(self):
        metrics = {
        "cpu": {
            "element": None,
            "label": "CPU Usage",
            "unit": "%",
            "value": lambda : psutil.cpu_percent()
        },
        "ram": {
            "element": None,
            "label": "RAM",
            "unit": "%",
            "value": lambda: psutil.virtual_memory().percent
        },
        "disk": {
            "element": None,
            "label": "Disk",
            "unit": "%",
            "value": lambda : psutil.disk_usage('/').percent
        }
    }
        def make_label(text=None):
            font = ("Helvetica", 14)
            label = tk.Label(self.root, text=text, font=font)
            label.pack(side=tk.LEFT, padx=10)
            return label
        
        
        for metric, config in metrics.items():
            metrics[metric]["element"] = make_label(config["label"])

        print(f"creating metrics: {metric}")
        return metrics
        
    def update_loop(self):
        for metric, config in self.metrics.items():
            self.metrics[metric]["element"].config(text=f"{config['label']}: {config['value']()}{config['unit']}")

        self.root.after(1000, self.update_loop)  # Refresh every 1000ms (1 second)


if __name__ == "__main__":
    app = SystemMonitorApp()
    app.update_loop()  # Initial call to start the loop

    app.root.mainloop()
