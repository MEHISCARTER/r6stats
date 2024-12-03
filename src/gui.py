import tkinter as tk
from tkinter import messagebox
import database

class R6StatsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("R6 Stats Tracker")
        self.current_frame = None
        self.switch_to_main_menu()

    def switch_frame(self, frame_func):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(padx=10, pady=10)
        frame_func()

    def switch_to_main_menu(self):
        self.switch_frame(self.main_menu)

    def main_menu(self):
        tk.Label(self.current_frame, text="R6 Stats Tracker", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.current_frame, text="Add Match", command=self.switch_to_add_match, width=20).pack(pady=5)
        tk.Button(self.current_frame, text="Check Stats", command=self.switch_to_check_stats, width=20).pack(pady=5)

    def switch_to_add_match(self):
        self.switch_frame(self.add_match)

    def add_match(self):
        tk.Label(self.current_frame, text="Add Match", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.current_frame, text="Map Name:").pack(pady=5)
        map_name_var = tk.StringVar()
        tk.Entry(self.current_frame, textvariable=map_name_var).pack(pady=5)

        round_inputs = []

        def add_round():
            round_frame = tk.Frame(self.current_frame)
            round_frame.pack(pady=5, fill=tk.X)

            round_data = {
                "side": tk.StringVar(),
                "site": tk.StringVar(),
                "kills": tk.IntVar(),
                "deaths": tk.IntVar(),
                "assists": tk.IntVar(),
                "operator": tk.StringVar(),
                "result": tk.StringVar()
            }

            tk.Label(round_frame, text="Side:").grid(row=0, column=0, padx=5)
            tk.Entry(round_frame, textvariable=round_data["side"]).grid(row=0, column=1, padx=5)

            tk.Label(round_frame, text="Site:").grid(row=0, column=2, padx=5)
            tk.Entry(round_frame, textvariable=round_data["site"]).grid(row=0, column=3, padx=5)

            tk.Label(round_frame, text="Kills:").grid(row=1, column=0, padx=5)
            tk.Entry(round_frame, textvariable=round_data["kills"]).grid(row=1, column=1, padx=5)

            tk.Label(round_frame, text="Deaths:").grid(row=1, column=2, padx=5)
            tk.Entry(round_frame, textvariable=round_data["deaths"]).grid(row=1, column=3, padx=5)

            tk.Label(round_frame, text="Assists:").grid(row=2, column=0, padx=5)
            tk.Entry(round_frame, textvariable=round_data["assists"]).grid(row=2, column=1, padx=5)

            tk.Label(round_frame, text="Operator:").grid(row=2, column=2, padx=5)
            tk.Entry(round_frame, textvariable=round_data["operator"]).grid(row=2, column=3, padx=5)

            tk.Label(round_frame, text="Result:").grid(row=3, column=0, padx=5)
            tk.Entry(round_frame, textvariable=round_data["result"]).grid(row=3, column=1, padx=5)

            round_inputs.append(round_data)

        def save_match():
            map_name = map_name_var.get()
            if not map_name:
                messagebox.showerror("Error", "Please enter the map name.")
                return

            match_data = []
            for round_data in round_inputs:
                match_data.append({key: var.get() for key, var in round_data.items()})

            try:
                match_id = database.save_match_with_map(map_name, match_data)
                messagebox.showinfo("Match Saved", f"Match ID {match_id} has been saved with map {map_name}!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.current_frame, text="Add Round", command=add_round, width=20).pack(pady=5)
        tk.Button(self.current_frame, text="Save Match", command=save_match, width=20).pack(pady=5)
        tk.Button(self.current_frame, text="Back to Menu", command=self.switch_to_main_menu, width=20).pack(pady=5)
    def switch_to_check_stats(self):
        self.switch_frame(self.check_stats)

    def check_stats(self):
        tk.Label(self.current_frame, text="Check Stats", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.current_frame, text="Enter Match ID:").pack(pady=5)
        match_id_var = tk.StringVar()
        tk.Entry(self.current_frame, textvariable=match_id_var).pack(pady=5)

        def show_stats():
            match_id = match_id_var.get()
            if not match_id:
                messagebox.showerror("Error", "Please enter a Match ID.")
                return

            try:
                match_stats = database.get_match_stats(match_id)
                if not match_stats:
                    messagebox.showerror("Error", "No match found with that ID.")
                    return

                stats_text = f"Stats for Match ID {match_id}:\n"
                # Get the map name from the first row (all rows should have the same map name)
                map_name = match_stats[0][1]
                stats_text += f"Map: {map_name}\n\n"

                for stat in match_stats:
                    stats_text += f"Round {stat[2]}: Side: {stat[3]}, Site: {stat[4]}, Kills: {stat[5]}, Deaths: {stat[6]}, Assists: {stat[7]}, Operator: {stat[8]}, Result: {stat[9]}\n"

                messagebox.showinfo("Match Stats", stats_text)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.current_frame, text="Show Stats", command=show_stats, width=20).pack(pady=5)
        tk.Button(self.current_frame, text="Back to Menu", command=self.switch_to_main_menu, width=20).pack(pady=5)

root = tk.Tk()
app = R6StatsApp(root)
root.mainloop()
