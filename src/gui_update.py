import tkinter as tk
from tkinter import messagebox
import databaseS as database
import os
import map_op_sites
from PIL import Image
import copy

class R6StatsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("R6 Stats Tracker")
        self.current_frame = None
        self.round_input = []
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
    
    def switch_to_map_selection(self):
        self.switch_frame(self.map_selection)
    
    def map_selection(self):
        """
        error with images, fix later. for now map selection uses dropdown menus
        """

        # tk.Label(self.current_frame, text="Choose a Map", font=("Arial", 16)).grid(row=0, column=0, columnspan=4, pady=10)
        
        # map_images_dir = "D:\Homework\CIS350\R6Stats\map_pictures" - change for delivery

        map_names = ["bank", "border", "chalet", "clubhouse", "coastline", "consulate", 
             "kafe", "oregon", "skyscraper", "theme", "villa", "nighthaven",
             "emerald", "kanal", "lair", "outback"]
        
        # def select_map(map_name):
        #     self.selected_map = map_name
        #     self.switch_to_add_match()
        
        # row, col = 0, 0
        # for map_name in map_names:
        #     try:
        #         map_image_path = os.path.join(map_images_dir, f"r6-maps-{map_name}.png")
        #         map_image = tk.PhotoImage(file=map_image_path)

        #         btn = tk.Button(self.current_frame, image=map_image, command=lambda m=map_name: select_map(m))
        #         btn.image = map_image
        #         btn.grid(row=row, column=col, padx=5, pady=5)

        #         col += 1
        #         if col >= 4:
        #             col = 0
        #             row += 1
            
        #     except Exception as e:
        #         print(f"Error loading map image for {map_image}: {e}")

        self.selected_map = tk.StringVar(value="Select Map")

        tk.Label(self.current_frame, text="Map: ").grid(row=0, column=0, padx=5)
        map_dropdown = tk.OptionMenu(self.current_frame, self.selected_map, *map_names)
        map_dropdown.grid(row=0, column=1, padx=5)

        tk.Button(self.current_frame, text="Add Rounds", command=self.switch_to_add_round, width=20).grid(row=1, column=0, columnspan=4, pady=10)

        tk.Button(self.current_frame, text="Back to Menu", command=self.switch_to_main_menu).grid(row=2, column=0, columnspan=4, pady=10)

    def add_match(self):
        tk.Label(self.current_frame, text="Add Match", font=("Arial", 16)).pack(pady=10)

        #map selection
        tk.Button(self.current_frame, text="Choose Map", command=self.switch_to_map_selection, width=20).pack(pady=5)

        tk.Button(self.current_frame, text="Back to Menu", command=self.switch_to_main_menu, width=20).pack(pady=5)
    
    #since add_round is no longer under add_match, this function is needed. probably the root of the issue with saving data
    def switch_to_add_round(self):
        selected_map = self.selected_map.get()
        if selected_map == "Select a Map":
            messagebox.showerror("Error", "Select a map.")
            return

        self.switch_frame(self.add_round)

    def add_round(self):
        round_frame = tk.Frame(self.current_frame)
        round_frame.pack(pady=5, fill=tk.X)

        self.round_input = []

        round_data = {
            "side": tk.StringVar(value="Select Side"),
            "site": tk.StringVar(),
            "kills": tk.IntVar(),
            "deaths": tk.IntVar(),
            "assists": tk.IntVar(),
            "operator": tk.StringVar(value="Select Side"),
            "result": tk.StringVar(value="Win or Lose")
        }

        #for the dropdown menu
        attacking_operators = [
        "Ace", "Amaru", "Ash", "Blackbeard", "Blitz", "Buck", "Capitão", 
        "Dokkaebi", "Finka", "Flores", "Glaz", "Gridlock", "Hibana", 
        "Iana", "IQ", "Jackal", "Kali", "Lion", "Maverick", "Montagne", 
        "Nokk", "Nomad", "Osa", "Sledge", "Thatcher", "Thermite", 
        "Twitch", "Ying", "Zero", "Zofia"
        ]

        #for the dropdown menu
        defensive_operators = [
        "Alibi", "Aruni", "Bandit", "Castle", "Caveira", "Clash", "Doc", 
        "Echo", "Ela", "Fenrir", "Frost", "Goyo", "Jäger", "Kaid", 
        "Kapkan", "Lesion", "Maestro", "Melusi", "Mira", "Mozzie", 
        "Mute", "Oryx", "Pulse", "Rook", "Solis", "Smoke", 
        "Tachanka", "Thunderbird", "Thorn", "Valkyrie", "Vigil", "Wamai", 
        "Warden"
        ]

        #dropdown
        tk.Label(round_frame, text="Side:").grid(row=0, column=0, padx=5)
        side_dropdown = tk.OptionMenu(round_frame, round_data["side"], "Attack", "Defense")
        side_dropdown.grid(row=0, column=1, padx=5)

        #operator drop down not available until side is picked
        tk.Label(round_frame, text="Operator:").grid(row=2, column=2, padx=5)
        operator_dropdown = tk.OptionMenu(round_frame, round_data["operator"], "Select Operator")
        operator_dropdown.grid(row=2, column=3, padx=5)
        operator_dropdown.config(state="disabled")

        tk.Label(round_frame, text="Site:").grid(row=0, column=2, padx=5)
        tk.Entry(round_frame, textvariable=round_data["site"]).grid(row=0, column=3, padx=5)

        tk.Label(round_frame, text="Kills:").grid(row=1, column=0, padx=5)
        tk.Entry(round_frame, textvariable=round_data["kills"]).grid(row=1, column=1, padx=5)

        tk.Label(round_frame, text="Deaths:").grid(row=1, column=2, padx=5)
        tk.Entry(round_frame, textvariable=round_data["deaths"]).grid(row=1, column=3, padx=5)

        tk.Label(round_frame, text="Assists:").grid(row=2, column=0, padx=5)
        tk.Entry(round_frame, textvariable=round_data["assists"]).grid(row=2, column=1, padx=5)

        #dropdown
        tk.Label(round_frame, text="Result:").grid(row=3, column=0, padx=5)
        result_dropdown = tk.OptionMenu(round_frame, round_data["result"], "Win", "Lose")
        result_dropdown.grid(row=3, column=1, padx=5)
        
        #enables operator dropdown after side is chosen
        def update_operator_dropdown(*args):
            selected_side = round_data["side"].get()
            operator_dropdown["menu"].delete(0, "end")
            
            #changes operators options based on side
            if selected_side == "Attack":
                operators = attacking_operators
            elif selected_side == "Defense":
                operators = defensive_operators
            else:
                operators = []
        
            for operator in operators:
                operator_dropdown["menu"].add_command(label=operator, command=lambda value=operator: round_data["operator"].set(value))

            operator_dropdown.config(state="normal" if operators else "disabled")
            round_data["operator"].set("Select Operator")

        round_data["side"].trace("w", update_operator_dropdown)

        #possibly another issue with saving
        def save_match():
            match_data = []
            for round_data in self.round_input:
                match_data.append({key: var for key, var in round_data.items()})
            self.selected_map = self.selected_map.get()
            match_id = database.save_match_with_map(self.selected_map, match_data)
            messagebox.showinfo("Match Saved", f"Match ID {match_id} has been saved!")

        #possibly another issue with saving
        def add_round_to_match():
            #gets actual values instead of tkinter type
            round_data_values = {
                "side": round_data["side"].get(),
                "site": round_data["site"].get(),
                "kills": round_data["kills"].get(),
                "deaths": round_data["deaths"].get(),
                "assists": round_data["assists"].get(),
                "operator": round_data["operator"].get(),
                "result": round_data["result"].get()
                }

            self.round_input.append(copy.deepcopy(round_data_values))
            # Reset the fields for the next round
            round_data["side"].set("Select Side")
            round_data["site"].set("")
            round_data["kills"].set(0)
            round_data["deaths"].set(0)
            round_data["assists"].set(0)
            round_data["operator"].set("Select Operator")
            round_data["result"].set("Win or Lose")

            messagebox.showinfo("Round Added", "Round has been added!")
        
        #add match button, these havent been working either
        add_round_button = tk.Button(self.current_frame, text="Add Round", command=add_round_to_match, width=20)
        add_round_button.pack(pady=5)

            # Save Match Button
        save_match_button = tk.Button(self.current_frame, text="Save Match", command=save_match, width=20)
        save_match_button.pack(pady=5)

            # Back to Menu Button
        back_to_menu_button = tk.Button(self.current_frame, text="Back to Menu", command=self.switch_to_main_menu, width=20)
        back_to_menu_button.pack(pady=5)
    
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
                stats_text = f"Stats for Match ID {match_id}:\n\nMap: {match_stats[0][-1]}\n\n"
                for stat in match_stats:
                    stats_text += f"Round {stat[0]}: Side: {stat[1]}, Site: {stat[2]}, Kills: {stat[3]}, Deaths: {stat[4]}, Assists: {stat[5]}, Operator: {stat[6]}, Result: {stat[7]}\n"

                messagebox.showinfo("Match Stats", stats_text)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(self.current_frame, text="Show Stats", command=show_stats, width=20).pack(pady=5)
        tk.Button(self.current_frame, text="Back to Menu", command=self.switch_to_main_menu, width=20).pack(pady=5)


root = tk.Tk()
app = R6StatsApp(root)
root.mainloop()
