import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)
        print("Set up goes here")

    def test_konstructori_asettaa_saldon_oikein(self):
        saldo = str(self.kortti)
        self.assertEqual(saldo, "Kortilla on rahaa 10 euroa")

    def test_syo_maukkaasti_alentaa_saldoa(self):
        self.kortti.syo_maukkaasti()
        saldo = str(self.kortti)
        self.assertEqual(saldo, "Kortilla on rahaa 6 euroa")

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        for i in range(5):
            self.kortti.syo_maukkaasti()

        saldo = str(self.kortti)

        self.assertEqual(saldo, "Kortilla on rahaa 2 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")

