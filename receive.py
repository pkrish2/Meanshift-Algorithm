from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
 
pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-3183ed9c-3c2d-11e7-847e-02ee2ddab7fe"
pnconfig.publish_key = "pub-c-5547bc05-fdd3-489e-b4bc-930fb835441d"
pnconfig.ssl = False

pubnub = PubNub(pnconfig)

pubnub.subscribe().channels('my_channel').execute()
