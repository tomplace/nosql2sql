import redis
from errors import Error

class Client(object):
    
    def __init__(self, host, port):
                    
        self.server = redis.StrictRedis(host, port)
        try:
            self.keys = self.server.keys("*")
        except:
            raise Error("Unable to connect to Redis database")

        # Get all 'rows' (i.e. instances of each entity)
        self.rows = [object for object in self.keys 
                            if object.find(":") != -1]
                
        # Iterate over the instances to create unique entity list 
        entities = {}
        for e in self.rows:
            entities[e[0:e.find(":")]] = 1
        self.entities = entities.keys()
        
        # Get all 'indices' 
        self.indices = [object for object in self.keys 
                                if object.find("_") != -1]
     
        # TODO: Create data generators 
        