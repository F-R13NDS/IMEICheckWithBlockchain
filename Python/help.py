class help:
    def __init__(self):
        return """
            Python Türkçe yazım ve şifreleme modülü
        
        Bu modul verilen metin üzerinde Türkçe kontoller yapmak ve metni şifrelemek için yazılmıştır.
        
        Türkçe sınıfı:
            Bu modulu çağırıken parametre olarak uygulanacak metin gönderilmelidir.
            fonksiyonlar:
            - kelimelereAyir
            - cumlelereAyir
            - sesliHarfler
            - buyukUnluUyumu
            - turkceKarakterDuzeltme
            
            
            1- kelimelereAyir(metin)
                Fonksiyon gönderilen metnin içindeki kelime sayısını verir.
                Dönüş değeri sayıdır.
            
            2- cumlelereAyir(metin)
                Fonksiyon gönderilen metnin içindeki cümle sayısını verir.
                Dönüş değeri sayıdır.
            
            3- sesliHarfler(metin)
                Gönderilen metnin içindeki sesli harf sayısını verir.
                Dönüş değeri sayıdır
            
            4- buyukUnluUyumu(metin)
                Metnin içindeki kelimelerden kaç tanesinin büyük ünlü 
                uyumuna uyduğunun ve kaç tanesinin uymadığınını
                sayısını verir.
                Dönüş değeri dictionary seklinde {"uyan" : sayı, "uymayan" : sayı}
                
            5- turkceKarakterDuzeltme(metin)
                Parametreyle gönderilen metnin içindeki türkçe karakterleri ["ş", "ç", "ö", "ğ", "ü", "ı", "Ş", "Ç", "Ö", "Ğ", "Ü", "İ"]
                dönüştürür ["s", "c", "o", "g", "u", "i", "S", "C", "O", "G", "U", "I"]
                Dönüş değeri metnin dönüşmüş halidir.
        
        
        Şifreleme sınıfı:
            Bu modülü çağırırken şifrelenecek metin parametre olarak gönderilmelidir.
            ! Dosyaya yazan fonksiyonların dönüş değerleri yoktur.
                - writeFile
                - md5
                - md5_file
                - sha256
                - sha256_file
                - blake2
                - blake2_file
                - shake256
                - shake256_file
                - ceaser
                - ceaser_file
                - binary
                - spn
                - spn_file
                - sha512
                - sha512_file
                
            1- writeFile(sifre)
                Parametre olarak aldığı değeri "encrypted.txt" isimli dosyaya yazar.
            
            2- md5(string)
                Parametre olarak aldığı değeri md5 algoritmasına gire şifreler.
                Dönüş değeri şifrelenmiş metindir.
            
            3- md5_file(string)
                Parametre olarak gönderilen değeri md5 algoritamsına göre şifreleyip dosyaya yazar.
            
            4- sha256(string)
                Parametre olarak aldığı değeri sha256 algoritmasına göire şifreler.
                Dönüş değeri şifrelenmiş metindir.
            
            5- sha256_file(string)
                Parametre olarak gönderilen değeri sha256 algoritamsına göre şifreleyip dosyaya yazar.
            
            6- blake2(string)
                Parametre olarak aldığı değeri blake2 algoritmasına göre şifreler.
                Dönüş değeri şifrelenmiş metindir.
            
            7- blake2_file(string)
                Parametre olarak gönderilen değeri blake2 algoritamsına göre şifreleyip dosyaya yazar.
            
            8- shake256(string)
                Parametre olarak aldığı değeri shake256 algoritmasına göre şifreler.
                Dönüş değeri şifrelenmiş metindir.
            
            9- shake256_file(string)
                Parametre olarak gönderilen değeri shake256 algoritamsına göre şifreleyip dosyaya yazar. 
                
            10- ceaser(string, kaydırma_miktarı)
                Parametre olarak aldığı değeri, 2. parametre olarak aldığı sayı değerine göre kaydırarak ceaser algoritmasına göre şifreler.
                Dönüş değeri şifrelenmiş metindir.
            
            11- ceaser_file(string, kaydırma_miktarı)
                Parametre olarak gönderilen değeri 2. parametre olarak aldığı sayı değerine göre kaydırarak ceaser algoritamsına göre şifreleyip dosyaya yazar. 
                
            12- binary(sayı, lenght = 8)
                Parametre olarak aldığı sayıyı binary türüne çevirir. Default olarak uzunluk 8 verilmiştir. 2. bir parametre göndererek uzunluk değiştirilebilir.
                Dönüş değeri sayının binary halidir.
            
            13- spn(string, key)
                Parametre olarak aldığı metni 2. parametre olarak aldığı key e göre spn algoritması kullanarak şifreler.
                Dönüş değeri şifreli metindir.
            
            14- spn_file(string, key)
                Parametre olarak aldığı metni 2. parametre olarak aldığı key e göre spn algoritması kullanarak şifreler ve dosyaya yazar.
                 
            15- sha512(string, kaydırma_miktarı)
                Parametre olarak aldığı değeri sha512 algoritmasına göire şifreler.
                Dönüş değeri şifrelenmiş metindir.
            
            16- sha512_file(string)
                Parametre olarak gönderilen değeri sha512 algoritmasına göre şifreleyip dosyaya yazar. 
                
        """