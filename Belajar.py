cashback_mentah = ["25000", "50000", "SYSTEM_DOWN",
                   "-15000", "100000", "ZONK_BONUS"]

total_cashback = 0

with open("laporan_cashback.txt", "w") as file_out:
    for data in cashback_mentah:
        try:
            angka_cashback = int(data)
            if angka_cashback > 0:
                total_cashback += angka_cashback
                file_out.write(str(angka_cashback) + "\n")
                print(f"Angka {angka_cashback} lolos filter")
        except ValueError:
            print(f"Data {data} rusak wok!")
            continue

print("\n--- KESIMPULAN ---")

with open("laporan_cashback.txt", "a") as file_out:
    file_out.write("Total poin yang valid: " + str(angka_cashback) + "\n")
    print("Kalimat kesimpulan berhasil ditambahkan")

print(f"\nProses selesai! Hasil total akhir cashback: {angka_cashback}")
