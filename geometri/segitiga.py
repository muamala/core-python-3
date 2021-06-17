class Segitiga():
    def __init__(self, a, t):
        self.a = a
        self.t = t

    def info(self):
        return f'Ini adalah objek dari segitiga dengan alas {self.a} dan tinggi {self.t}'

    def hitung_luas(self):
        return self.a * self.t