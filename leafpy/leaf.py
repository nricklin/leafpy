from auth import login

class Leaf(object):
    """Make requests to the Nissan Connect API to get Leaf Info"""
    custom_sessionid  = None
    VIN = None

    def __init__(self, username=None, password=None, custom_sessionid=None, VIN=None):

    	# If you instantiate with a username & password, login.
        if username and password:
        	self.custom_sessionid, self.VIN = login(username, password)
        elif custom_sessionid and VIN:
        	self.custom_sessionid = custom_sessionid
        	self.VIN = VIN
        else:
        	raise Exception('Need either username & password or custom_sessionid & VIN.')