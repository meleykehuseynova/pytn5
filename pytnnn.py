class Bank:
    def __init__(self, hesab_nomresi, balans):
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def balans_artir(self, mebleg):
        self.balans += mebleg
        print("Balansınız artırıldı. Yeni balans:", self.balans)

    def pul_cixar(self, mebleg):
        if self.balans >= mebleg:
            self.balans -= mebleg
            print("Balansınızdan", mebleg, "məbləğində pul çıxarıldı. Yeni balans:", self.balans)
        else:
            print("Balansınızda kifayət qədər məbləğ yoxdur.")

    def balans_goster(self):
        print("Hesab nömrəsi:", self.hesab_nomresi)
        print("Cari balans:", self.balans)


class Kredit(Bank):
    def __init__(self, hesab_nomresi, balans, kredit_meb):
        super().__init__(hesab_nomresi, balans)
        self.kredit_meb = kredit_meb

    def kredit_ver(self):
        self.balans += self.kredit_meb
        print("Kreditiniz hesabınıza əlavə edildi. Yeni balans:", self.balans)

    def kredit_odenişi(self):
        ayliq_odenis = self.kredit_meb / 12
        self.balans -= ayliq_odenis
        print("Kredit ödənişi uğurla tamamlandı. Yeni balans:", self.balans)


musteri1 = Bank(123456789, 5000)

musteri2 = Kredit(987654321, 10000, 12000)

musteri1.balans_artir(2000)
musteri1.pul_cixar(3000)
musteri1.balans_goster()


musteri2.kredit_ver()
musteri2.kredit_odenişi()
musteri2.balans_goster()