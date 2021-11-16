import unittest
from kassapaate import Kassapaate 
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate() 

    def test_kassa_luotu_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kateisosto_edukkaat_rahaa_on(self):
        maksu = 300
        palautus = self.kassa.syo_edullisesti_kateisella(maksu)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(palautus, maksu - 240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kateisosto_maukkaat_rahaa_on(self):
        maksu = 500 
        palautus = self.kassa.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(palautus, maksu - 400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kateisosto_edukkaat_rahaa_ei_ole(self):
        maksu = 100 
        palautus = self.kassa.syo_edullisesti_kateisella(maksu)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(palautus, maksu)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kateisosto_maukkaat_rahaa_ei_ole(self):
        maksu = 100 
        palautus = self.kassa.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(palautus, maksu)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_korttiosto_edukkaat_kun_rahaa_on(self):
        kortti = Maksukortti(10000)
        syo_edukas = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(syo_edukas, True)
        self.assertEqual(kortti.saldo, 10000 - 240)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_korttiosto_edukkaat_kun_rahaa_ei_ole(self):
        kortti = Maksukortti(10)
        syo_edukas = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(syo_edukas, False)
        self.assertEqual(kortti.saldo, 10)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_korttiosto_maukas_kun_rahaa_on(self):
        kortti = Maksukortti(10000)
        maukas = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(maukas, True)
        self.assertEqual(kortti.saldo, 10000 - 400)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_korttiosto_maukas_kun_rahaa_ei_ole(self):
        kortti = Maksukortti(10)
        maukas = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(maukas, False)
        self.assertEqual(kortti.saldo, 10)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kortille_rahan_lataus_positiivinen_raha(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)

    def test_kortille_rahan_lataus_negatiivinen_raha(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)




