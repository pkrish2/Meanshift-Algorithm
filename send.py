from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

##pubnub = PubNub(
##    publish_key = "pub-c-5547bc05-fdd3-489e-b4bc-930fb835441d",
##    subscribe_key = "sub-c-3183ed9c-3c2d-11e7-847e-02ee2ddab7fe")
##
##channel = "my_channel"
##message = "Hello"
##
##pubnub.publish(
##    channel = channel,
##    message = "Hello")

def publish_callback(result, status):
    pass
    # handle publish result, status always present, result if successful
    # status.isError to see if error happened

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-3183ed9c-3c2d-11e7-847e-02ee2ddab7fe"
pnconfig.publish_key = "pub-c-5547bc05-fdd3-489e-b4bc-930fb835441d"
pnconfig.ssl = False
 
pubnub = PubNub(pnconfig)

pubnub.publish().channel("my_channel").message(["hello", "there"])\
        .should_store(True).use_post(True).async(publish_callback)

##pubnub.subscribe().channels('my_channel').execute()
##pubnub.unsubscribe().channels("my_channel").execute()


