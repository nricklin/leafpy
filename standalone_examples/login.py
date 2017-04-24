import requests
import base64
from Crypto.Cipher import Blowfish

USERNAME = '<your-username>'
PASSWORD = '<your-password>'

# # initial app response.  The whole point here is to get baseprm, 
# # which seems to always be = 'uyI5Dj9g8VCOFDnBRUbr3g'.  so we can probably just skip it.
# url = 'https://gdcportalgw.its-mo.com/gworchest_160803A/gdc/InitialApp.php'
# data = {
# 	"RegionCode": 'NNA',
# 	"lg": "en-US",
# 	"initial_app_strings": "geORNtsZe5I4lRGjG9GZiA"
# }
# r = requests.post(url, data=data)
# r.raise_for_status()
# if not r.json()['status'] == 200:
# 	raise Exception['Something wrong while doing InitialApp.php']
# baseprm = r.json()['baseprm']
baseprm = 'uyI5Dj9g8VCOFDnBRUbr3g'

# once we've got baseprm, we can encrypt your password before sending it.
c1  = Blowfish.new(baseprm, Blowfish.MODE_ECB)
packingLength = 8 - len(PASSWORD) % 8
packedPassword = PASSWORD + chr(packingLength) * packingLength
encryptedPassword = c1.encrypt(packedPassword)
encodedPassword = base64.standard_b64encode(encryptedPassword)

# Now actually login
url = "https://gdcportalgw.its-mo.com/gworchest_160803A/gdc/UserLoginRequest.php"
data = {
	"RegionCode": 'NNA',
	"UserId": USERNAME,
	"initial_app_strings": "geORNtsZe5I4lRGjG9GZiA",
	"Password": encodedPassword,
}

r = requests.post(url,data=data)
print r.status_code
print r.text


# Now get stuff we need for making future requests:
custom_sessionid = r.json()['VehicleInfoList']['vehicleInfo'][0]['custom_sessionid']
VIN = r.json()['CustomerInfo']['VehicleInfo']['VIN']

# Future requests can be made with VIN & custom_sessionid:
url = "https://gdcportalgw.its-mo.com/gworchest_160803A/gdc/BatteryStatusRecordsRequest.php"
data = {
	"RegionCode": 'NNA',
	"custom_sessionid": custom_sessionid,
	"VIN": VIN
}

r = requests.post(url,data=data)
print r.status_code
print r.text





