from twitter import *
t = twitter(auth=OAuth(<Access Token>,<Access Token Secret>,
                <Consumer Key>,<Consumer Secret>))
statusUpdate = t.statuses.update(status='Hello World!')
print(statusUpdate)