import unittest
from pathlib import Path

from ptls.address import Address
from ptls.clinic import Clinic
from ptls.scrapers import Athletico

path: Path = Path(f'./data/test_files/{Athletico.company_name}')

test_urls = Athletico.test_urls

class TestScraperAthleticoClass(unittest.TestCase):

    def test_get_states_url(self):
        with path.joinpath(test_urls['states'][0]).open('rb') as f:
            raw_html: str = f.read()
        urls: [str] = Athletico._get_states_urls(raw_html)
        # print(urls)

    def test_get_state_location_urls(self):
        with path.joinpath(test_urls['locations'][0]).open('rb') as f:
            raw_html: str = f.read()
        urls: [str] = Athletico._get_location_urls(raw_html)
        # print(urls)

    def test_get_location(self):
        with path.joinpath(test_urls['clinic'][0]).open('rb') as f:
            raw_html: str = f.read()
        clinic: Clinic = Athletico._get_clinic_info(raw_html, test_urls['clinic'][0])
        # print(clinic)
        self.assertEqual(clinic,
                         Clinic(Athletico.company_name, 'Bloomington',
                                Address.from_address_str(
                                    'Bloomington 1704 Eastland Dr., Unit 15 Bloomington, IL 61704'),
                                '309-664-7766', test_urls['clinic'][0],
                                fax='309-664-6767', email='BloomingtonIL@athletico.com'))