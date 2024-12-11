import tkinter as tk
from tkinter import messagebox, filedialog
import database
import os
from PIL import Image, ImageTk
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
        tk.Button(self.current_frame, text="Select Map Directory", command=self.select_map_directory, width=20).pack(pady=5)

    def switch_to_add_match(self):
        self.switch_frame(self.add_match)
    
    def switch_to_map_selection(self):
        self.switch_frame(self.map_selection)
    
    def select_map_directory(self):
        self.select_map_dir = filedialog.askdirectory(title="Select Map Images Directory")
        if not self.select_map_dir:
            messagebox.showerror("Error", "Please select directory for map images")

    def map_selection(self):
        """
        Selects map using an image of the map
        Asks user to add the directory where the r6_maps images are
        """
        if not self.select_map_dir:
            self.select_map_directory()
        
        if not self.select_map_dir:
            return

        map_names = ["bank", "border", "chalet", "clubhouse", "coastline", "consulate", 
             "kafe", "oregon", "skyscraper", "theme", "villa", "nighthaven",
             "emerald", "kanal", "lair", "outback"]
        
        def select_map(map_name):
            self.selected_map.set(map_name)
            self.switch_to_add_round()

        row, col = 1, 0
        for map_name in map_names:
            try:
                map_image_path = os.path.join(self.select_map_dir, f"r6-maps-{map_name}.png")
                map_image = Image.open(map_image_path)
                #makes images higher quality
                map_image = map_image.resize((100, 100), Image.Resampling.LANCZOS)
                map_picture = ImageTk.PhotoImage(map_image)

                button = tk.Button(self.current_frame, image=map_picture, command=lambda m=map_name: select_map(m))

                button.image = map_picture
                button.grid(row=row, column=col, padx=5, pady=5)

                col += 1
                if col >= 4:
                    col = 0
                    row += 1

            except Exception as e:
                print(f"Error loading image for {map_name}: {e}")
        self.selected_map = tk.StringVar(value="Select Map")

        # tk.Label(self.current_frame, text="Select from dropdown instead: ").grid(row=0, column=0, padx=5)
        # map_dropdown = tk.OptionMenu(self.current_frame, self.selected_map, *map_names)
        # map_dropdown.grid(row=row + 1, column = 2, columnspan=2)

        # tk.Button(self.current_frame, text="Confirm Map Selection", command=lambda: select_map(self.selected_map.get(), width=20)).grid(row=row+2, column=0, columnspan=4, pady=10)

        # tk.Button(self.current_frame, text="Add Rounds", command=self.switch_to_add_round, width=20).grid(row=row+3, column=0, columnspan=4, pady=10)

        tk.Button(self.current_frame, text="Back to Menu", command=self.switch_to_main_menu, width=20).grid(row=row+4, column=0, columnspan=4, pady=10)

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
            "site": tk.StringVar(value="Select Site"),
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

        map_sites = {
        "lair": ["2F Master Office and 2F R6 Room", "1F Floor Bunks and 1F Floor Briefing",
                "1F Floor Armory and 1F Floor Weapons Maintenance", "Basement Lab and Lab Support"],
        "nighthaven": ["2F Command and 2F Server", "1F Control and 1F Storage",
                            "1F Kitchen and  1F Cafeteria", "Basement Tank and Assembly"],
        "bank": ["2F Ceo Office and 2F Executive Lounge", "1F Open Area and 1F Staff Room",
                "1F Floor Tellers' Office and 1F Archives", "Basement CCTV Room and Basement Lockers"],
        "border": ["2F Armory Lockers and 2F Archives", "1F Suppy Room and 1F Customs Inspection",
                "1F Workshop and 1F Ventilation Room", "1F Bathroom and 1F Tellers"],
        "chalet": ["2F Office and 2F Master Bedroom", "1F Gaming Room and 1F Bar",
                "1F Kitchen and 1F Dining Room", "Basement Wine Cellar and Basement Snowmobile Garage"],
        "clubhouse": ["2F Bedroom and 2F Gym", "2F Cash Room and 2F CCTV Room",
                    "1F Bar and 1F Stock Room", "Basement Church and Basement Arsenal Room"],
        "consulate": ["2F Meeting Room and 2F Consulate Office", "1F Piano Room and 1F Exposition Room",
                    "1F Tellers and Basemnt Servers", "Basement Cafeteria and Basement Garage"],
        "kafe": ["3F Cocktail Lounge", "2F Fireplace Hall and 2F Mining Room",
                            "2F Reading Room and 2F Fireplace Hall", "1F Kitchen Service and 1F Kitchen Cooking"],
        "skyscraper": ["2F Tea Room and 2F Karaoke", "2F Work Office and 2F Exhibition",
                    "1F BBQ and 1F Kitchen", "1F Bedroom and 1F Bathroom"],
        "coastline": ["2F Billiard Rooms and 2F Hookah Lounge", "2F Theater and 2F Penthouse",
                    "1F Kitchen and 1F Service Entrance", "1f Blue Bar and 1F Sunrise Bar"],
        "emerald":["2F CEO Office and 2F Administration", "2F Private Gallery and 2F Meeting",
                        "1F Bar and 1F Lounge", "1F Dining and 1F Kitchen"],
        "kanal": ["2F Server Room and 2F Radar Room", "1F Security Room and 1F Map Room",
                "1F Coast Guard Meeting Room and 1F Lounge", "Basement Kayaks and Supply Room"],
        "oregon": ["2F Kids Dorms and 2F Dorms Main Hall", "1F Kitchen and 1F Dining Hall",
                "1F Meeting and 1F Kitchen", "Basement Laundry Room and Basement Supply Room"],
        "outback": ["2F Laundry Room and 2F Games Room", "2F Party Room and 2F Office",
                    "1F Nature Room and 1F Bushranger Room", "1F Compressor Room and 1F Gear Store"],
        "theme": ["2F Initiation Room and 2F Office", "2F Bunk and 2F Day Care",
                    "1F Armory and 1F Throne Room", "1F Lab and 1F Storage"],
        "villa": ["2F Aviator Room and 2F Games Room", "2F Trophy Room and 2F Statuary Room",
                "1F Living Room and 1F Library", "1F Dining Room and 1F Kitchen"]
}
        
        self.map_sites = map_sites.get(self.selected_map.get())

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
        site_dropdown = tk.OptionMenu(round_frame, round_data["site"], *self.map_sites)
        site_dropdown.grid(row=0, column=3, padx=5)

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

        def save_match():
            match_data = []
            for round_data in self.round_input:
                match_data.append({key: var for key, var in round_data.items()})
            self.selected_map = self.selected_map.get()
            match_id = database.save_match_with_map(self.selected_map, match_data)
            messagebox.showinfo("Match Saved", f"Match ID {match_id} has been saved!")

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

        tk.Button(self.current_frame, text="View All Matches", command=self.display_match_list).pack(pady=5)

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
    
    def display_match_list(self):
        #all matches from database
        matches = database.get_all_matches()
        
        #create the frame for the matches
        match_list_frame = tk.Frame(self.current_frame)
        match_list_frame.pack(pady=10, fill=tk.X)
        
        #iterate through the matches
        for i, match in enumerate(matches):
            match_id = match[0]
            map_name = match[1]

            try:
                #images and shtuff
                map_image_path = os.path.join("D:\\Homework\\CIS350\\R6Stats\\map_pictures", f"r6-maps-{map_name}.png")
                map_image = Image.open(map_image_path)
                map_image = map_image.resize((50,50))
                map_picture = ImageTk.PhotoImage(map_image)

                #buttons
                match_button = tk.Button(match_list_frame, image=map_picture, command=lambda m_id=match_id: self.display_indepth_match(m_id))
                match_button.image = map_picture
                match_button.grid(row=i // 4, column=i % 4, padx=5, pady=5)
            
            except Exception as e:
                print(f"Error loading map image for {map_name}: {e}. Make sure the map image is named r6-maps-{map_name}.png")

                match_button = tk.Button(match_list_frame, text=map_name, command=lambda m_id=match_id: self.display_indepth_match(m_id))
                match_button.grid(row=i // 4, column=i % 4, padx=5 , pady=5)

    def display_indepth_match(self, match_id):
        match_stats = database.get_match_stats(match_id)
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Match ID: {match_id}")
        round = 0
        for stat in match_stats:
            round += 1
            stats_text = f"Round {round}: Side: {stat[1]}, Site: {stat[2]}, Kills: {stat[3]}, Deaths: {stat[4]}, Assists: {stat[5]}, Operator: {stat[6]}, Result: {stat[7]}\n"
            tk.Label(details_window, text=stats_text).pack()

    
    
root = tk.Tk()
app = R6StatsApp(root)
root.mainloop()
