# Defining the Starship class:
class starship:
    def __init__(self, name, model, role, crew_size):
        self.name = name
        self.model = model
        self.role = role
        self.crew_size = crew_size

    
    def get_info(self):
        return f"Starship: {self.name}\nModel: {self.model}\nRole: {self.role}\nCrew Size: {self.crew_size}\n"
    def to_dict(self):
        return {
            "name": self.name,
            "model": self.model,
            "role": self.role,
            "crew size": self.crew_size
        }
    
class GalacticDataManager:
    def __init__(self):
        self.data = {}

    def add_starship(self, starship):
        self.data[starship.name] = starship.to_dict()

    def display_all_starships(self):
        for starship_name, starship_data in self.data.items():
            print(f"{starship_name}")
            for attribute, value in starship_data.items():
                print(f"       {attribute.capitalize()}: {value}")
            print("\n")

millennium_falcon = starship("Millennium Falcon", "YT-1300F", "Freighter", 4)
star_destroyer = starship("Star Destroyer", "Imperial I-class", "Destroyer", 37000)

galactic_data_manager = GalacticDataManager()
galactic_data_manager.add_starship(millennium_falcon)
galactic_data_manager.add_starship(star_destroyer)

galactic_data_manager.display_all_starships()

