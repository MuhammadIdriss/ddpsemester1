# Gempa.py

class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print(f"Gempa di {self.lokasi} tidak berasa.")
        elif 2 <= self.skala < 4:
            print(f"Gempa di {self.lokasi} menyebabkan bangunan retak-retak.")
        elif 4 <= self.skala < 6:
            print(f"Gempa di {self.lokasi} menyebabkan bangunan roboh.")
        else:
            print(f"Gempa di {self.lokasi} menyebabkan bangunan roboh dan berpotensi tsunami.")
