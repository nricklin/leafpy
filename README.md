# leafpy
lightweight python interface to the nissan leaf


# Login with Username & Password:

```python
from leafpy import Leaf
leaf = Leaf('<your-username>', '<your-password>')
```

This takes a while, so it's recommended that you cache somewhere your VIN & custom_sessionid and instantiate like so:

```python
from leafpy import Leaf
leaf = Leaf(custom_sesionid='<your-custom_sessionid>', VIN='<your-VIN>')
# you can get these values from a previous login:
# leaf.VIN, leaf.custom_sessionid
```

# Check Battery Status:
```python
leaf.BatteryStatusRecordsRequest()
```
and you get the raw output from the API:
```python
{   u'BatteryStatusRecords': {   u'BatteryStatus': {   u'BatteryCapacity': u'240',
                                                       u'BatteryChargingStatus': u'NOT_CHARGING',
                                                       u'BatteryRemainingAmount': u'240',
                                                       u'BatteryRemainingAmountWH': u'28880',
                                                       u'BatteryRemainingAmountkWH': u'',
                                                       u'SOC': {   u'Value': u'100'}},
                                 u'CruisingRangeAcOff': u'198000',
                                 u'CruisingRangeAcOn': u'192000',
                                 u'NotificationDateAndTime': u'2017/04/24 23:43',
                                 u'OperationDateAndTime': u'2017/04/24 23:43',
                                 u'OperationResult': u'START',
                                 u'PluginState': u'CONNECTED',
                                 u'TargetDate': u'2017/04/24 23:43'},
    u'VoltLabel': {   u'HighVolt': u'240', u'LowVolt': u'120'},
    u'status': 200}
```