import unittest
import weather_api_script


class WeatherApiTests(unittest.TestCase):

    def test_resolve_city_name_single_name(self):
        city_list = ["wROcLaw", "WROCLAW", "wroclaw", "WrOcLAW", "wroCLAW", "WROcla"]
        for city in city_list:
            city_name_function = weather_api_script.resolve_city_name(city)
            self.assertEqual("Wroclaw", city_name_function)

    def test_resolve_city_name_compound_name(self):
        city_list = ["Bielsko Biala", "bielsko biala", "BielskO BIALA", "BiElSko BiAlA", 'BIELSKO BIALA']
        for city in city_list:
            city_name_function = weather_api_script.resolve_city_name(city)
            self.assertEqual(['Bielsko', 'Biala'], city_name_function)

    def test_resolve_city_name_hyphen(self):
        city_list = ["kedzierzyn-kozle", "KEDZIERZYN-KOZLE", "kedzierzyn-kozle"]
        for city in city_list:
            city_name_function = weather_api_script.resolve_city_name(city)
            self.assertEqual("Kedzierzyn-Kozle", city_name_function)


if __name__ == '__main__':
    unittest.main()
