def calculate_hiking_time(vertical_gain, horizontal_distance):
    # Waktu tempuh vertikal saat mendaki (1 jam per 300 meter naik)
    time_up = vertical_gain / 300
    
    # Waktu tempuh vertikal saat menurun (1 jam per 500 meter turun)
    time_down = vertical_gain / 500
    
    # Total waktu tempuh vertikal (naik + turun)
    vertical_time = time_up + time_down
    
    # Waktu tempuh untuk jarak horizontal (1 jam per 4 kilometer)
    horizontal_time = horizontal_distance / 4
    
    # Cari waktu yang lebih kecil antara vertikal dan horizontal
    smallest_time = min(vertical_time, horizontal_time)
    
    # Bagian terkecil dibagi dua
    adjustment = smallest_time / 2
    
    # Total waktu tempuh pendakian
    total_time = vertical_time + horizontal_time + adjustment
    
    # Konversi ke jam dan menit
    hours = int(total_time)
    minutes = int((total_time - hours) * 60)
    
    return hours, minutes

# Meminta input dari pengguna
try:
    # Input elevasi puncak dan titik awal
    elevasi_puncak = float(input("Masukkan elevasi puncak (dalam meter): "))
    elevasi_start = float(input("Masukkan elevasi titik awal (dalam meter): "))
    
    # Menghitung ketinggian pendakian sebagai selisih
    vertical_gain = elevasi_puncak - elevasi_start
    
    # Input jarak horizontal
    horizontal_distance = float(input("Masukkan jarak horizontal dari titik awal ke titik akhir (dalam kilometer): "))
    
    # Memanggil fungsi dengan input pengguna
    hours, minutes = calculate_hiking_time(vertical_gain, horizontal_distance)
    print(f"Waktu total pendakian: {hours} jam {minutes} menit")
except ValueError:
    print("Harap masukkan nilai numerik yang valid.")
