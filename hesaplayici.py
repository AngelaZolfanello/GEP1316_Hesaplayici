
import time
import threading

# Oyun Karakteri Can ve Hasar Hesaplayıcısı

karakter_adi = input("Karakterin adı: ")
maksimum_can = int(input("Maksimum can (HP): "))

# Maksimum can sıfır veya negatif olamaz.
while maksimum_can <= 0:
    maksimum_can = int(input("Pozitif bir maksimum can girin: "))

mevcut_can = float(maksimum_can)
segment_sayisi = 6
oyun_aktif = True

# İki işlemin aynı anda canı değiştirmesini önler.
can_kilidi = threading.Lock()


# Can barını ve karakter durumunu gösterir.
def can_bari_goster():
    with can_kilidi:
        can = mevcut_can

    can_yuzdesi = (can / maksimum_can) * 100
    dolu_segment = int((can / maksimum_can) * segment_sayisi)
    bos_segment = segment_sayisi - dolu_segment

    can_bari = "■" * dolu_segment + "□" * bos_segment
    hayatta_mi = can > 0

    print(f"\n{karakter_adi}: [{can_bari}]")
    print(f"Can: {can:.1f}/{maksimum_can} HP (%{can_yuzdesi:.1f})")
    print(f"Hayatta mı? {hayatta_mi}")


# Can azaldıkça her saniye daha fazla HP yeniler.
def can_yenile():
    global mevcut_can

    while oyun_aktif:
        time.sleep(1)

        with can_kilidi:
            if mevcut_can <= 0:
                continue

            if mevcut_can < maksimum_can:
                eksik_can_orani = (maksimum_can - mevcut_can) / maksimum_can

                # Maksimum canın %2'si ile %10'u arasında yenilenme.
                yenilenme = maksimum_can * (0.02 + 0.08 * eksik_can_orani)

                mevcut_can = min(maksimum_can, mevcut_can + yenilenme)
                guncellendi = True
            else:
                guncellendi = False

        if guncellendi:
            print("\n+ Otomatik can yenilendi!")
            can_bari_goster()


# Yenilenme işlemini arka planda başlatır.
yenileme_thread = threading.Thread(target=can_yenile, daemon=True)
yenileme_thread.start()

print("\nOyun başladı!")
can_bari_goster()

# Oyuncu istediği kadar işlem yapabilir.
while oyun_aktif:
    print("\n1 - Hasar al")
    print("2 - Can durumunu göster")
    print("3 - Yeniden başlat")
    print("4 - Oyundan çık")

    secim = input("Seçiminiz: ")

    if secim == "1":
        hasar = float(input("Alınan hasar (HP): "))

        if hasar < 0:
            print("Hasar negatif olamaz!")
            continue

        with can_kilidi:
            mevcut_can = max(0, mevcut_can - hasar)

        can_bari_goster()

    elif secim == "2":
        can_bari_goster()

    elif secim == "3":
        with can_kilidi:
            mevcut_can = float(maksimum_can)

        print("Karakter yeniden başladı!")
        can_bari_goster()

    elif secim == "4":
        oyun_aktif = False
        print("Oyun kapatıldı.")

    else:
        print("Geçersiz seçim!")
