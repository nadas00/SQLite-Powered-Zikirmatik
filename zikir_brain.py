import sqlite3


class Zikir:

    def __init__(self, zikir, dua, sayac):
        self.zikir = zikir
        self.dua = dua
        self.sayac = sayac

    def __str__(self):
        return """***\nZikir : {} Dua: {} Sayac: {}\n***""" \
            .format(self.zikir, self.dua, self.sayac)


class Zikirmatik:

    def __init__(self):
        self.baglanti_kur()

    def zikirleri_ver(self):
        """
        zikirleri txtye aktar
        :return:
        """
        pass

    def baglanti_kur(self):
        self.connection = sqlite3.connect('zikirmatik.db')
        self.cursor = self.connection.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS zikirler (zikir,dua,sayac)"
        self.cursor.execute(sorgu)
        self.connection.commit()

    def zikirleri_goser(self):
        sorgu = "SELECT * FROM zikirler"
        self.cursor.execute(sorgu)
        zikirler = self.cursor.fetchall()
        if len(zikirler) == 0:
            print('KAYITLI ZİKİR YOK...')
        else:
            for i in zikirler:
                zikirim = Zikir(i[0], i[1], i[2])
                print(zikirim)

    def zikir_sec(self):
        sorgu = "SELECT * FROM zikirler"
        self.cursor.execute(sorgu)
        secilizikir = self.cursor.fetchall()

        for i, j in enumerate(secilizikir):
            print('\n'+j[0].upper() + ' zikrini seçmek için : ', i)

        try:
            secimim = int(input('\nSecim bekleniyor... : '))
            zikirmatik.zikir_cek(secilizikir[secimim])
        except (IndexError, ValueError):
            print('Yanlış bir tuşlama yaptınız... Ana menüye yönlendiriliyorsunuz....')



    def zikir_ekle(self, zikirismi, duaismi):
        sorgu = "INSERT INTO zikirler VALUES (?,?,?)"
        self.cursor.execute(sorgu, (zikirismi, duaismi, 0,))
        self.connection.commit()

    def zikir_sil(self, zikirismi):
        sorgu = "DELETE FROM zikirler WHERE zikir = ?"
        self.cursor.execute(sorgu, (zikirismi,))
        self.connection.commit()

    def zikir_cek(self, zikirsecimim):
        sayac = int(zikirsecimim[2])
        zikirim = zikirsecimim[0]
        print(zikirsecimim[0]+' zikri için ENTER\'layınız.\nÇıkmak için herhangi bir tuşa basınız.\n'+zikirsecimim[1])
        while True:
            x = input('')

            if x == '':
                print(zikirsecimim[1])
                sayac += 1
            else:
                print("ALLAH KABUL ETSİN...")
                break
        sorgu = "UPDATE zikirler SET sayac = ? WHERE zikir = ?"
        self.cursor.execute(sorgu, (sayac, zikirim,))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()


zikirmatik = Zikirmatik()
print("""
    ZİKİRMATİĞE HOŞGELDİNİZ...
    ***************************************
    ZIKIRLERI GORUNTULEMEK ICIN --------- 1
    ZIKIR EKLEMEK ICIN ------------------ 2
    ZIKIR CEKMEK ICIN ------------------- 3
    ZIKIR SILMEK ICIN ------------------- 4
    ***************************************
    """)
while True:
    secim = input('Seciminiz: ')
    if secim == '1':
        zikirmatik.zikirleri_goser()
    elif secim == '2':
        zikir = input('Zikir adı giriniz: ')
        dua = input('Dua giriniz: ')
        zikirmatik.zikir_ekle(zikir, dua)
    elif secim == '3':
        zikirmatik.zikir_sec()
    elif secim == '4':
        secim = input('Silmek istediğiniz Zikir ismini giriniz...')
        zikirmatik.zikir_sil(secim)
    else:
        zikirmatik.close_connection()
        break
