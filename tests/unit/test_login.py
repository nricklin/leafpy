import unittest
from .leafpy import Leaf
import vcr

USERNAME = 'dummyuser'
PASSWORD = 'dummypass'

class LoginTests(unittest.TestCase):

    @vcr.use_cassette('tests/unit/cassettes/test_login.yaml', 
        filter_post_data_parameters=['UserId','Password'])
    def test_login(self):
        leaf = Leaf(USERNAME, PASSWORD)

        assert leaf.VIN == "vin123"
        assert leaf.custom_sessionid == "csessid"

    def test_login_with_custom_sessionid_and_vin(self):
        leaf = Leaf(VIN='vin345', custom_sessionid='csid123')

        assert leaf.VIN == 'vin345'
        assert leaf.custom_sessionid == 'csid123'

    @vcr.use_cassette('tests/unit/cassettes/test_exeption_raised_when_bad_credentials_passed.yaml', 
        filter_post_data_parameters=['UserId','Password'])
    def test_exeption_raised_when_bad_credentials_passed(self):
        with self.assertRaises(Exception) as w:
            leaf = Leaf('bad_email@domain.com','invalidpassword')

    @vcr.use_cassette('tests/unit/cassettes/test_exception_raised_when_bad_vin_and_customsessionid_used.yaml', 
        filter_post_data_parameters=['UserId','Password'])
    def test_exception_raised_when_bad_vin_and_customsessionid_used(self):

        leaf = Leaf(VIN='vin345',custom_sessionid='csid123')

        with self.assertRaises(Exception) as w:
            leaf.BatteryStatusRecordsRequest()

    def test_login_with_only_username_raises_exception(self):
        with self.assertRaises(Exception):
            leaf = Leaf('username')

    def test_login_with_only_VIN_raises_exception(self):
        with self.assertRaises(Exception):
            leaf = Leaf(VIN='vin123')

    def test_login_with_only_custom_sessionid_raises_exception(self):
        with self.assertRaises(Exception):
            leaf = Leaf(custom_sessionid='vin123')

    def test_login_with_no_args_raises_exception(self):
        with self.assertRaises(Exception):
            leaf = Leaf()
