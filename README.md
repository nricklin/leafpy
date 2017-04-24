# leafpy
lightweight python interface to the nissan leaf


# Get battery status:

```python
from leafpy import Leaf
leaf = Leaf(username, password)

# Tell the leaf to check itself for battery status
result = leaf.BatteryStatusCheckRequest()

# after waiting some amount of time for that to happen, get the battery status
leaf.BatteryStatusCheckResultRequest(resultKey=result['resultKey'])

# or just check whatever battery status is available without polling first:
leaf.BatteryStatusRecordsRequest()
```