import unittest
import formatter

class TestFormatter(unittest.TestCase):
    def test_lower(self):
        test_text = "SoRNA MuRUGAN"
        result = formatter.convert_lower(test_text)
        print(result)
        self.assertEqual(result, "sorna murugan")

    def test_upper(self):
        test_text = "Sorna Murugan"
        result = formatter.convert_upper(test_text)
        print(result)
        self.assertEqual(result, "SORNA MURUGAN")

if __name__ =="__main__":
    unittest.main()
