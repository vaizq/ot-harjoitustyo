import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(90)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(20);
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_riittavatko_rahat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20), False)
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)

