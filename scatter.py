import random

def scatter_dynamic_generator():
    try:
        print("--- TEORI SIMULASI SCATTER ---")
        landasan_input = input("Masukkan angka landasan (seed): ")
        wajib_input = input("Masukkan angka wajib (max 6 digit): ")

        seed_val = int(landasan_input)
        digit_wajib = list(set([int(d) for d in str(wajib_input)]))

        if len(digit_wajib) > 6:
            print("Kritik: Angka wajib terlalu banyak!")
            return

        random.seed(seed_val)
        pool = list(range(10))
        sisa_pool = [n for n in pool if n not in digit_wajib]

        kebutuhan = 6 - len(digit_wajib) 
        random.shuffle(sisa_pool)
        hasil_tambahan = sisa_pool[:kebutuhan]

        hasil_akhir = digit_wajib + hasil_tambahan
        random.shuffle(hasil_akhir)

        print("\n" + "="*40)
        print(f"HASIL ANALISIS SCATTER")
        print("="*40)
        print(f"Landasan Seed : {seed_val}")
        print(f"Angka Keluar  : {' - '.join(map(str, hasil_akhir))}")
        print("="*40)

    except ValueError:
        print("Kesalahan: Input harus berupa angka bulat!")

if __name__ == "__main__":
    scatter_dynamic_generator()
