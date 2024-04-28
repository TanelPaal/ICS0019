import subprocess
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import http.client
import json

# Start the api.py and app.py scripts
subprocess.Popen(["python", "api.py"])
subprocess.Popen(["python", "app.py"])

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Canteens App")
        self.master.geometry("800x400")
        self.pack()
        self.create_widgets()

        # Get screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate position of window's top left corner
        x = (screen_width // 2) - (800 // 2)
        y = (screen_height // 2) - (400 // 2)

        # Set the position of the window to the center of the screen
        self.master.geometry(f'800x400+{x}+{y}')

    def create_widgets(self):
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("ID", "Name", "Location", "time_open", "time_closed")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("ID", width=50, anchor=tk.W)
        self.tree.column("Name", width=100, anchor=tk.W)
        self.tree.column("Location", width=100, anchor=tk.W)
        self.tree.column("time_open", width=100, anchor=tk.W)
        self.tree.column("time_closed", width=100, anchor=tk.W)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("ID", text="ID", anchor=tk.W)
        self.tree.heading("Name", text="Name", anchor=tk.W)
        self.tree.heading("Location", text="Location", anchor=tk.W)
        self.tree.heading("time_open", text="Open Time", anchor=tk.W)
        self.tree.heading("time_closed", text="Close Time", anchor=tk.W)

        self.tree.pack(side="top", fill="both", expand=True)

        # Create a frame for the buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side="left", fill="both", expand=True)

        self.get_button = tk.Button(self.button_frame)
        self.get_button["text"] = "Refresh canteens"
        self.get_button["command"] = self.get_canteens
        self.get_button.pack(side="top", fill="x")

        self.query_button = tk.Button(self.button_frame)
        self.query_button["text"] = "Query canteens by open time"
        self.query_button["command"] = self.query_canteens
        self.query_button.pack(side="top", fill="x")

        self.add_button = tk.Button(self.button_frame)
        self.add_button["text"] = "Add new canteen"
        self.add_button["command"] = self.add_canteen
        self.add_button.pack(side="top", fill="x")

        self.update_button = tk.Button(self.button_frame)
        self.update_button["text"] = "Update canteen"
        self.update_button["command"] = self.update_canteen
        self.update_button.pack(side="top", fill="x")

        self.delete_button = tk.Button(self.button_frame)
        self.delete_button["text"] = "Delete canteen"
        self.delete_button["command"] = self.delete_canteen
        self.delete_button.pack(side="top", fill="x")

    def send_request(self, method, url, body=None, headers=None):
        if headers is None:
            headers = {}
        conn = http.client.HTTPConnection('localhost', 5001)
        conn.request(method, url, body, headers)
        response = conn.getresponse()
        data = response.read().decode()
        conn.close()
        try:
            return response.status, json.loads(data) if data else None
        except json.JSONDecodeError:
            return response.status, None

    def get_canteens(self):
        status, data = self.send_request('GET', '/canteen')
        if status == 200:
            for i in self.tree.get_children():
                self.tree.delete(i)
            for canteen in data:
                self.tree.insert("", "end", values=(canteen[0], canteen[1], canteen[2], canteen[3], canteen[4]))
        else:
            print(f"Error: status code {status}, response data {data}")
            messagebox.showerror("Error", "Could not get canteens")

    def query_canteens(self):
        time_open = simpledialog.askstring("Input", "Enter the open time (format: HH:MM)")
        status, data = self.send_request('GET', f'/canteen/{time_open}')
        if status == 200:
            for i in self.tree.get_children():
                self.tree.delete(i)
            for canteen in data:
                self.tree.insert("", "end", values=(canteen[0], canteen[1], canteen[2], canteen[3], canteen[4]))
        else:
            messagebox.showerror("Error", "Could not get canteens")

    def add_canteen(self):
        data = simpledialog.askstring("Input", "Enter the canteen data (format: Name,Location,time_open,time_closed)")
        name, location, time_open, time_closed = data.split(',')
        body = json.dumps({"Name": name, "Location": location, "time_open": time_open, "time_closed": time_closed})
        headers = {"Content-Type": "application/json"}
        status, _ = self.send_request('POST', '/canteen', body, headers)
        if status == 200:
            messagebox.showinfo("Success", "Canteen added successfully")
            self.get_canteens()
        else:
            messagebox.showerror("Error", "Could not add canteen")

    def update_canteen(self):
        id = simpledialog.askstring("Input", "Enter the ID of the canteen to update")
        data = simpledialog.askstring("Input", "Enter the new canteen data (format: Name,Location,time_open,time_closed)")
        name, location, time_open, time_closed = data.split(',')
        body = json.dumps({"Name": name, "Location": location, "time_open": time_open, "time_closed": time_closed})
        headers = {"Content-Type": "application/json"}
        status, _ = self.send_request('PUT', f'/canteen/{id}', body, headers)
        if status == 200:
            messagebox.showinfo("Success", "Canteen updated successfully")
            self.get_canteens()
        else:
            messagebox.showerror("Error", "Could not update canteen")

    def delete_canteen(self):
        id = simpledialog.askstring("Input", "Enter the ID of the canteen to delete")
        status, _ = self.send_request('DELETE', f'/canteen/{id}')
        if status == 200:
            messagebox.showinfo("Success", "Canteen deleted successfully")
            self.get_canteens()
        else:
            messagebox.showerror("Error", "Could not delete canteen")

root = tk.Tk()
app = Application(master=root)
app.mainloop()