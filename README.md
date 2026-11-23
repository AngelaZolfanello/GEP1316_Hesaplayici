
# Oyun Karakteri Can ve Hasar Hesaplayıcısı

GEP1316 Kodlama Okuryazarlığı - Ödev 3

## Projenin Amacı

Python ile geliştirilen bu program, oyun karakterinin can durumunu ve aldığı hasarı hesaplar. Karakterin canı azaldıkça otomatik yenilenme miktarı artar.

## Özellikler

- 6 segmentli can barı
- Hasar alma sistemi
- Her saniye otomatik can yenilenmesi
- Can azaldıkça artan yenilenme miktarı
- Karakterin hayatta olup olmadığını kontrol etme
- Negatif hasar kontrolü
- Karakteri yeniden başlatma

## Kullanılan Teknolojiler

- Python 3
- time
- threading

## Çalıştırma

Terminalde aşağıdaki komutu kullanın:

```powershell
py hesaplayici.py
```

## Kullanım

Program başladığında karakterin adını ve maksimum can değerini girin.

Menü seçenekleri:

1. Hasar al
2. Can durumunu göster
3. Yeniden başlat
4. Oyundan çık

## Testler

- 100 HP, 70 hasar: 30 HP kalır ve otomatik yenilenme başlar.
- 100 HP, 200 hasar: Karakter ölür.
- Negatif hasar: Program girdiyi reddeder.

## Yapay Zekâ Kullanımı

Proje, ChatGPT desteğiyle geliştirilmiş ve kullanıcı tarafından test edilmiştir.
