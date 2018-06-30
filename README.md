# leafpydome
Lightweight python interface to the nissan leaf.  Check battery status, turn on the AC, start charging, etc.

[![PyPI version](https://badge.fury.io/py/leafpydome.svg)](https://badge.fury.io/py/leafpydome) 
[![Build Status](https://travis-ci.org/nricklin/leafpydome.svg?branch=master)](https://travis-ci.org/nricklin/leafpydome)
[![codecov](https://codecov.io/gh/nricklin/leafpydome/branch/master/graph/badge.svg)](https://codecov.io/gh/nricklin/leafpydome)


# Installation
```
pip install leafpydome
```

# Examples:

Login:
----

```python
from leafpydome import Leaf
leaf = Leaf('<your-username>', '<your-password>')
```

Or with custom_sessionid & VIN:

```python
from leafpydome import Leaf
leaf = Leaf(custom_sesionid='<your-custom_sessionid>', VIN='<your-VIN>')
# you can get these values from a previous login:
# leaf.VIN, leaf.custom_sessionid
```

*Check Battery Status:*
-----
```python
leaf.BatteryStatusRecordsRequest()
```
results in:
```json
{
	"status": 200,
	"BatteryStatusRecords": {
		"BatteryStatus": {
			"BatteryRemainingAmountkWH": "",
			"SOC": {
				"Value": "100"
			},
			"BatteryChargingStatus": "NOT_CHARGING",
			"BatteryRemainingAmount": "240",
			"BatteryCapacity": "240",
			"BatteryRemainingAmountWH": "28880"
		},
		"OperationResult": "START",
		"NotificationDateAndTime": "2017/04/24 23:43",
		"CruisingRangeAcOff": "198000",
		"OperationDateAndTime": "2017/04/24 23:43",
		"CruisingRangeAcOn": "192000",
		"PluginState": "CONNECTED",
		"TargetDate": "2017/04/24 23:43"
	},
	"VoltLabel": {
		"HighVolt": "240",
		"LowVolt": "120"
	}
}
```
*Query for Battery Status:*
-----
```python
response = leaf.BatteryStatusCheckRequest()
# Wait a few seconds for the request to be made to the car
leaf.BatteryStatusCheckResultRequest(resultKey=response['resultKey'])
```
results in:
```json
{
	"status": 200,
	"currentChargeLevel": "0",
	"timeRequiredToFull": {
		"hours": "",
		"minutes": ""
	},
	"timeRequiredToFull200_6kW": {
		"hours": "",
		"minutes": ""
	},
	"operationResult": "START",
	"timeStamp": "2017-04-25 05:23:48",
	"pluginState": "CONNECTED",
	"cruisingRangeAcOff": "198000.0",
	"timeRequiredToFull200": {
		"hours": "",
		"minutes": ""
	},
	"batteryCapacity": "240",
	"cruisingRangeAcOn": "192000.0",
	"responseFlag": "1",
	"batteryDegradation": "240",
	"charging": "NO",
	"chargeStatus": "CT",
	"chargeMode": "NOT_CHARGING"
}
```

*Turn on Climate Control:*
-----
```python
response = leaf.ACRemoteRequest()
# Wait a few seconds for the request to be made to the car
# Check status if you don't want to assume it worked:
leaf.ACRemoteResult(resultKey=response['resultKey'])
```
results in:
```json
{
	"status": 200,
	"hvacStatus": "ON",
	"operationResult": "START",
	"timeStamp": "2017-04-25 05:38:09",
	"acContinueTime": "7200",
	"responseFlag": "1"
}
```

*Turn off Climate Control:*
-----
```python
response = leaf.ACRemoteOffRequest()
# Wait a few seconds for the request to be made to the car
# Check status if you don't want to assume it worked:
leaf.ACRemoteOffResult(resultKey=response['resultKey'])
```
results in:
```json
{
	"status": 200,
	"timeStamp": "2017-04-25 05:40:27",
	"hvacStatus": "OFF",
	"operationResult": "START",
	"responseFlag": "1"
}
```

*Get latest climate control status:*
-----
```python
leaf.RemoteACRecordsRequest()
```
results in:
```json
{
	"status": 200,
	"RemoteACRecords": {
		"ACDurationPluggedSec": "7200",
		"ACStartStopDateAndTime": "2017/04/25 05:40",
		"ACStartStopURL": "",
		"PreAC_temp": "75",
		"OperationResult": "START",
		"PreAC_unit": "F",
		"OperationDateAndTime": "2017/04/25 05:40",
		"PluginState": "CONNECTED",
		"ACDurationBatterySec": "900",
		"RemoteACOperation": "STOP"
	}
}
```

*Get Car Location:*
-----
This just gets the most recent location.
```python
leaf.MyCarFinderLatLng()
```
results in:
```json
{
	"status": 200,
	"receivedDate": "2017/04/25 05:47",
	"lng": "-100.000000000",
	"lat": "50.00000000",
	"TargetDate": "2017/04/25 05:47"
}
```
To query for location then get the result:
```python
response = leaf.MyCarFinderRequest()
# now wait a while
leaf.MyCarFinderResultRequest(resultKey=response['resultKey'])
```

*Start Charging:*
-----
```python
leaf.BatteryRemoteChargingRequest()
```

*Schedule Climate Control:*
-----
```python
leaf.ACRemoteNewRequest(ExecuteTime='2016-02-09 17:24')
```

*Update Scheduled Climate Control:*
-----
```python
leaf.ACRemoteUpdateRequest(ExecuteTime='2016-02-09 17:24')
```

*Cancel Scheduled Climate Control:*
-----
```python
leaf.ACRemoteCancelRequest()
```

*Get Climate Control Schedule:*
-----
```python
leaf.GetScheduledACRemoteRequest()
```

*Get Driving Analysis:*
-----
```python
leaf.DriveAnalysisBasicScreenRequestEx()
```

*Get Price Simulation:*
-----
```python
leaf.PriceSimulatorDetailInfoRequest()
```
