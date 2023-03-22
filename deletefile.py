import os
import shutil

dosya_silmek = input("Silmek istediğiniz dosyanın konumunu giriniz: ")
klasör_silmek = input("Silmek istediğiniz klasörün konumunu giriniz:")
tüm_herşeyi_silmek = input("İcindeki her şeyi silmek istediğiniz dosyanın konumunu giriniz:")

#path = input("Dosya konumunu yazınız : ")
try:
    os.remove(dosya_silmek)
except FileNotFoundError:
        print("Dosya bulunamadı")

except ValueError:
    print("Yanlış değer girdiniz")

except PermissionError:
    print("Dosyayı silmek icin yeterli yetkiye sahip değilsin")
except OSError:
    print("Bu fonksiyon ile dosyayı silemezsin")
except NameError:
    print("Dosya yolu girmediniz")
else:
    print(dosya_silmek+"was deleted")

try:
    os.rmdir(klasör_silmek )


except FileNotFoundError:
        print("Dosya bulunamadı")

except ValueError:
    print("Yanlış değer girdiniz")

except PermissionError:
    print("Dosyayı silmek icin yeterli yetkiye sahip değilsin")
except OSError:
    print("Bu fonksiyon ile dosyayı silemezsin")
except NameError:
    print("Dosya yolu girmediniz")
else:
    print(klasör_silmek +"was deleted")

try:
    shutil.rmtree(tüm_herşeyi_silmek)
except FileNotFoundError:
        print("Dosya bulunamadı")

except ValueError:
    print("Yanlış değer girdiniz")

except PermissionError:
    print("Dosyayı silmek icin yeterli yetkiye sahip değilsin")
except OSError:
    print("Bu fonksiyon ile dosyayı silemezsin")
except NameError:
    print("Dosya yolu girmediniz")
else:
    print(tüm_herşeyi_silmek+"was deleted")
