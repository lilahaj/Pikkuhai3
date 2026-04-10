import random
import time

class HotelLightingControl:
    def __init__(self):
        self.total_lights = 100
        self.lights_on = random.randint(0, 100)
        self.burned_lights = random.randint(0, 10)
        # Oletetaan että yksi lamppu kuluttaa 10-15W
        self.power_per_light = 12  # watts
        self.emergency_mode = False
        
        # Varatut huoneet: 10 huonetta (~4 valoa/huone) + 5 huonetta (~7 valoa/huone)
        self.reserved_rooms_5lights = random.randint(0, 10)  # 0-10 huonetta
        self.reserved_rooms_10lights = random.randint(0, 5)  # 0-5 huonetta
        self.total_reserved_rooms = self.reserved_rooms_5lights + self.reserved_rooms_10lights
    
    def get_lights_on(self):
        """Palauttaa montako valoa on päällä"""
        return self.lights_on
    
    def get_burned_lights(self):
        """Palauttaa montako valoa on palanut"""
        return self.burned_lights
    
    def get_energy_consumption(self):
        """Laskee energiankulutuksen kilowatteina (kW)"""
        # Lisätään pieni satunnainen vaihtelu kulutukseen
        base_consumption = self.lights_on * self.power_per_light
        
        # Hätävalaistus käyttää 10% tehosta
        if self.emergency_mode:
            base_consumption = base_consumption * 0.1
        
        variation = random.uniform(-0.05, 0.05)  # ±5% vaihtelu
        total_watts = base_consumption * (1 + variation)
        return total_watts / 1000  # muutetaan kilowateiksi
    
    def activate_emergency_lighting(self):
        """Aktivoi hätävalaistus (käytävän valot 10% kirkkaudella)"""
        self.emergency_mode = True
        # Käytävän valot (oletetaan ~20-30 valoa)
        self.lights_on = random.randint(20, 30)
        print("⚠️  SÄHKÖKATKO HAVAITTU!")
        print("🚨 Hätävalaistus aktivoitu - Käytävän valot 10% kirkkaudella")
    
    
    def display_status(self):
        """Näyttää järjestelmän tilan"""
        print("\n" + "="*50)
        print("   ÄLYVALOHAI - OHJAUSKESKUS")
        print("="*50)
        print(f"Valoja yhteensä:        {self.total_lights} kpl")
        print(f"Valoja päällä:          {self.lights_on} kpl")
        print(f"Valoja epäkunnossa:       {self.burned_lights} kpl")
        
        energy = self.get_energy_consumption()
        if self.emergency_mode:
            print(f"Energiankulutus:        {energy:.2f} kW (HÄTÄVALAISTUS 10%)")
        else:
            print(f"Energiankulutus:        {energy:.2f} kW")
        
        print(f"Toimivia valoja:        {self.total_lights - self.burned_lights} kpl")
        print("-" * 50)
        print(f"Varatut huoneet yhteensä: {self.total_reserved_rooms}/15 kpl")
        print(f"  • Pieni huone:      {self.reserved_rooms_5lights}/10 huonetta")
        print(f"  • Suuri huone:     {self.reserved_rooms_10lights}/5 huonetta")
        
        if self.emergency_mode:
            print("-" * 50)
            print("⚠️  SÄHKÖKATKO HAVAITTU! HÄTÄVALAISTUS AKTIIVINEN ⚠️")
        
        print("="*50)

def main():
    system = HotelLightingControl()
    
    while True:
        system.display_status()
        print("\nVALIKKO:")
        print("1. Näytä tilanne")
        print("2. Päivitä järjestelmä")
        print("3. Aktivoi hätävalaistus")
        print("4. Poistu")
        
        choice = input("\nValitse toiminto (1-4): ")
        
        if choice == "1":
            continue
        elif choice == "2":
            system.lights_on = random.randint(0, 100)
            system.burned_lights = random.randint(0, 10)
            system.reserved_rooms_5lights = random.randint(0, 10)
            system.reserved_rooms_10lights = random.randint(0, 5)
            system.total_reserved_rooms = system.reserved_rooms_5lights + system.reserved_rooms_10lights
            system.emergency_mode = False
            print("✓ Järjestelmä päivitetty uusilla arvoilla")
        elif choice == "3":
            system.activate_emergency_lighting()
        elif choice == "4":
            print("\nKiitos käytöstä! Hyvää päivänjatkoa.")
            break
        else:
            print("✗ Virheellinen valinta!")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
