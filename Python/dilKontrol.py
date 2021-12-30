class dilKontrol:

    def __init__(self):
        self.sesliler = ["a", "ı", "o", "u", "e", "i", "ö", "ö"]
        self.kalinUnlu = ["a", "ı", "o", "u"]
        self.inceUnlu = ["e", "i", "ö", "ö"]
        self.turkceHarfler = ["ş", "ç", "ö", "ğ", "ü", "ı", "Ş", "Ç", "Ö", "Ğ", "Ü", "İ"]
        self.cevirilecekHarfler = ["s", "c", "o", "g", "u", "i", "S", "C", "O", "G", "U", "I"]

    def metinKontrol(self, string):
        if(type(string) != str):
            raise ValueError("Sadece metin değeri giriniz!")

    def kelimelereAyir(self, string):
        self.metinKontrol(string)
        kelimeler = string.split(" ")
        return len(kelimeler)

    def cumlelereAyir(self, string):
        self.metinKontrol(string)
        cumleler = string.split(".")
        return len(cumleler)

    def sesliHarfler(self, string):
        self.metinKontrol(string)
        harfler = [char for char in string]
        sayac = 0
        for harf in harfler:
            if (harf in self.sesliler):
                sayac+=1
        return sayac

    def buyukUnluUyumu(self, string):
        self.metinKontrol(string)
        kelimeler = string.split(" ")
        uyan = 0
        uymayan = 0
        for i in kelimeler:
            kelime = i
            if (sum(kelime.count(kalin) for kalin in self.kalinUnlu)) != 0 and (sum(kelime.count(ince) for ince in
                                                                                   self.inceUnlu)) != 0:
               uymayan += 1
            else:
                uyan +=1

        sonuc = {"uyan" : uyan, "uymayan": uymayan}
        return sonuc

    def turkceKarakterDuzeltme(self, string):
        self.metinKontrol(string)
        for i in range(12):
            string = string.replace(self.turkceHarfler[i], self.cevirilecekHarfler[i])
        return string