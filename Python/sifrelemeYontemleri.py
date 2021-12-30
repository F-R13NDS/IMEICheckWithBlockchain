import hashlib

class sifrelemeYontemleri:
    def __init__(self):
        self.fileName = "encrypted.txt"

    def kontrol(self, string):
        if (string == ""):
            raise Exception("Boş değer girdiniz!")

    def writeFile(self, sifre):
        self.kontrol(sifre)
        with open(self.fileName, "w") as file:
            file.write(sifre)

    def md5(self, string):
        result = hashlib.md5(string.encode("utf-8")).hexdigest()
        return result

    def md5_file(self, string):
        sifre = self.md5(string)
        self.writeFile(sifre)

    def sha256(self, string):
        hasher = hashlib.sha256()
        hasher.update(string.encode("utf-8"))
        sifre = hasher.hexdigest()
        return sifre

    def sha256_file(self, string):
        sifre = self.sha256(string)
        self.writeFile(sifre)

    def blake2(self, string):
        hasher = hashlib.blake2b()
        hasher.update(string.encode('utf-8'))
        sifre = hasher.hexdigest()
        return sifre

    def blake2_file(self, string):
        sifre = self.blake2(string)
        self.writeFile(sifre)

    def shake256(self, string):
        hasher = hashlib.sha256()
        hasher.update(string.encode('utf-8'))
        sifre = hasher.hexdigest()
        return sifre

    def shake256_file(self, string):
        sifre = self.shake256(string)
        self.writeFile(sifre)

    def ceaser(self, string, s):
        sifre = ""
        for i in range(len(string)):
            char = string[i]
            if(char.isupper()):
                sifre += chr((ord(char) + s - 64) % 26 + 65)
            else:
                sifre += chr((ord(char) + s - 96) % 26 + 97)
        return sifre

    def ceaser_file(self, string, s):
        sifre = self.ceaser(string, s)
        self.writeFile(sifre)

    def binary(self, num, length=8):
        b = bin(num).lstrip("0b")
        b = "0" * (length - len(b)) + b
        return b

    def spn(self, string, key):
        plaintext = string
        keyLength = len(key)
        cipherBin = ""

        for i in range(0, len(plaintext)):
            j = i % keyLength
            xor = ord(plaintext[i]) ^ ord(key[j])
            cipherBin = cipherBin + self.binary(xor) + " "

        return cipherBin

    def spn_file(self, string, key):
        sifre = self.spn(string,key)
        self.writeFile(sifre)


    def sha512(self, string):
        hasher = hashlib.sha512()
        hasher.update(string.encode("utf-8"))
        sifre = hasher.hexdigest()
        return sifre

    def sha512_file(self, string):
        sifre = self.sha512(string)
        self.writeFile(sifre)








