from sifrelemeYontemleri import *
import help as yardim
from dilKontrol import *

sifreleme = sifrelemeYontemleri()
dilBilgisi = dilKontrol()


def help():
    return yardim.help.__init__(yardim)

def kelimelereAyir(string):
    return dilBilgisi.kelimelereAyir(string)

def cumlelereAyir(string):
    return dilBilgisi.cumlelereAyir(string)

def sesliHarfler(string):
    return dilBilgisi.sesliHarfler(string)

def buyukUnluUyumu(string):
    return dilBilgisi.buyukUnluUyumu(string)

def turkceKarakterDuzeltme(string):
    return dilBilgisi.turkceKarakterDuzeltme(string)

def md5(string):
    return sifreleme.md5(string)

def md5_file(string):
    sifreleme.md5_file(string)

def sha256(string):
    return sifreleme.sha256(string)

def sha256_file(string):
    sifreleme.sha256_file(string)

def blake2(string):
    return sifreleme.blake2(string)
def blake2_file(string):
    sifreleme.blake2_file(string)

def shake256(string):
    return sifreleme.shake256(string)

def shake256_file(string):
    sifreleme.shake256_file(string)

def ceaser(string, s):
    return sifreleme.ceaser(string, s)

def ceaser_file(string, s):
    sifreleme.ceaser_file(string, s)

def binary(num, length=8):
    return sifreleme.binary(num, length)

def spn(string, key):
    return sifreleme.spn(string, key)

def spn_file(string, key):
    sifreleme.spn_file(string, key)

def sha512(string):
    return sifreleme.sha512(string)

def sha512_file(string):
    sifreleme.sha512_file(string)


