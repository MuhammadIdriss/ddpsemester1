# info_gempa.py
from Gempa import Gempa

# Membuat objek-objek Gempa
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)

# Memanggil fungsi dampak() untuk masing-masing objek Gempa
print("Dampak Gempa 1:")
gempa1.dampak()

print("\nDampak Gempa 2:")
gempa2.dampak()

print("\nDampak Gempa 3:")
gempa3.dampak()

print("\nDampak Gempa 4:")
gempa4.dampak()

print("\nDampak Gempa 5:")
gempa5.dampak()
