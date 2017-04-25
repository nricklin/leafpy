# leafpy
lightweight python interface to the nissan leaf

[![PyPI version](https://badge.fury.io/py/leafpy.svg)](https://badge.fury.io/py/leafpy)

# Installation
```
pip insall leafpy
```

# Examples:

Login:
----

```python
from leafpy import Leaf
leaf = Leaf('<your-username>', '<your-password>')
```

This takes a while, so it's recommended that you cache somewhere your VIN & custom_sessionid and instantiate like this:

```python
from leafpy import Leaf
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
