import unittest
from .leafpy import Leaf
import vcr, time

VIN = 'dummyvin'
custom_sessionid = 'dummy_csid'

class APICallTests(unittest.TestCase):

    @vcr.use_cassette('tests/unit/cassettes/test_call_with_no_params.yaml', 
        filter_post_data_parameters=['VIN','custom_sessionid'])
    def test_call_with_no_params(self):
        leaf = Leaf(VIN=VIN, custom_sessionid=custom_sessionid)

        result = leaf.BatteryStatusRecordsRequest()

        assert result['status'] == 200

    @vcr.use_cassette('tests/unit/cassettes/test_call_with_params.yaml', 
        filter_post_data_parameters=['VIN','custom_sessionid'])
    def test_call_with_params(self):
        leaf = Leaf(VIN=VIN, custom_sessionid=custom_sessionid)

        response = leaf.BatteryStatusCheckRequest()
        assert response['status'] == 200
        #time.sleep(140)   # only need to pause here when running against live service
        response2 = leaf.BatteryStatusCheckResultRequest(resultKey=response['resultKey'])
        assert response2['status'] == 200

    @vcr.use_cassette('tests/unit/cassettes/test_call_to_nonexistent_endpoint.yaml', 
        filter_post_data_parameters=['VIN','custom_sessionid'])
    def test_call_to_nonexistent_endpoint(self):
        leaf = Leaf(VIN=VIN, custom_sessionid=custom_sessionid)

        with self.assertRaises(Exception):
            response = leaf.this_doesnt_exist()

    
