import redis

class redisengine(object):
    def __init__(self, host, port):
        self.db = redis.StrictRedis(host, port)   
    
    def buildindex(self):
        pass
        # Check for entity / column hmaps that exist
        # unique entities and for each union of cols with max length 
        # Update existing where timestamp is > last run
        # Add new
