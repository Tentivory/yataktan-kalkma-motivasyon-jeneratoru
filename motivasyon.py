#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Yataktan Kalkma Motivasyon Jeneratörü
Bilimsel temelli, abartılı derecede ciddi bir sabah motivasyon sistemi.
"""

import random
import datetime
import time

def motivasyon_uret():
    saat = datetime.datetime.now().hour
    baz_motivasyonlar = [
        "Yataktan kalkmazsan, kahve fincanın seni yalnız bırakıp başka birine gidebilir.",
        "Bugün yataktan kalkarsan, evrenin entropisi senin lehine 0.000001% azalacak. Bilim.",
        "Kalkmazsan, telefonun şarjı bitince seni kurtarmaya kimse gelmez. Çünkü herkes uyuyor.",
        "Yatakta kalırsan, komşunun kedisi senin yerine sabah kahvaltısını yer. Gerçek.",
        "Kalk! Yoksa bugünki güneş doğuşunu başka biri görecek ve o kişi sen olmayacaksın.",
        "Yataktan kalkmak, yerçekimine karşı verdiğin en kahramanca mücadeledir. Tarihe geçersin.",
        "Eğer kalkmazsan, yastığın seni yavaş yavaş emmeye başlayacak. Fizik kanunu.",
        "Sabahları kalkmak zorunda değilsin. Ama kalkmazsan öğle yemeğini de yatakta yersin. Üstüne kırıntı dökerler.",
        "Bugün kalkarsan, dünyadaki tüm kediler senin adına bir dakikalık saygı duruşunda bulunur. Belki.",
        "Kalkmazsan, alarm saatin intikam alır ve yüzüne tükürür. Elektronik olarak."
    ]
    
    # Saat bazlı abartılı ek
    if saat < 7:
        ek = " Bu saatte kalkmak seni yasal olarak kahraman yapar."
    elif saat < 10:
        ek = " Hâlâ geç değil. Evren seni bekliyor."
    else:
        ek = " Geç kaldın ama geç kalmanın da bir güzelliği var."
    
    motivasyon = random.choice(baz_motivasyonlar) + ek
    return motivasyon

def ana():
    print("=" * 60)
    print("YATAKTAN KALKMA MOTİVASYON JENERATÖRÜ v1.0")
    print("Resmi olmayan resmi sabah protokolü")
    print("=" * 60)
    print()
    
    for i in range(3):
        print(f"Motivasyon {i+1}:")
        print(motivasyon_uret())
        print()
        time.sleep(1)
    
    print("Artık kalkabilirsin. Ya da kalkma. Seçim senin.")
    print("Ama unutma: yatak seni seviyor. Çok fazla seviyor.")

if __name__ == "__main__":
    ana()
