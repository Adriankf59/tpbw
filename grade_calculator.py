def calculate_mountain_grade(elevation_gain, slope_degree, hiking_time, is_route_available, requires_advanced_gear):
    """
    Kalkulator grade gunung berdasarkan parameter-parameter seperti ketinggian, kemiringan, waktu tempuh, ketersediaan jalur,
    dan kebutuhan peralatan pendakian.
    
    Parameters:
    - elevation_gain (int): Ketinggian puncak gunung dalam meter.
    - slope_degree (int): Kemiringan rata-rata jalur dalam derajat.
    - hiking_time (float): Waktu tempuh rata-rata dalam jam.
    - is_route_available (bool): Apakah jalur sudah tersedia atau jarang dilalui (True jika tersedia, False jika jarang).
    - requires_advanced_gear (bool): Apakah memerlukan peralatan pendakian lanjutan (True jika ya, False jika tidak).
    
    Returns:
    - str: Level kesulitan gunung.
    """
    
    if elevation_gain <= 1500 and slope_degree <= 10 and hiking_time <= 6 and is_route_available and not requires_advanced_gear:
        return "Level I (Mudah)"
    elif elevation_gain <= 2000 and slope_degree <= 15 and hiking_time <= 10 and is_route_available and not requires_advanced_gear:
        return "Level II (Menengah)"
    elif elevation_gain <= 3000 and slope_degree <= 20 and hiking_time <= 15 and is_route_available:
        return "Level III (Menantang)"
    elif elevation_gain <= 4000 and slope_degree <= 30 and hiking_time <= 20 and not is_route_available:
        return "Level IV (Sulit)"
    elif elevation_gain > 4000 or slope_degree > 30 or not is_route_available or requires_advanced_gear:
        return "Level V (Ekstrem)"
    else:
        return "Data tidak mencukupi untuk klasifikasi"

# Contoh penggunaan kalkulator
elevation_gain = int(input("Masukkan ketinggian puncak gunung (dalam meter): "))
slope_degree = int(input("Masukkan kemiringan rata-rata jalur (dalam derajat): "))
hiking_time = float(input("Masukkan waktu tempuh (dalam jam): "))
is_route_available = input("Apakah jalur tersedia dan sering dilalui? (ya/tidak): ").lower() == "ya"
requires_advanced_gear = input("Apakah memerlukan peralatan pendakian lanjutan? (ya/tidak): ").lower() == "ya"

grade = calculate_mountain_grade(elevation_gain, slope_degree, hiking_time, is_route_available, requires_advanced_gear)
print(f"Tingkat kesulitan gunung: {grade}")
