import redis
from errors import Error

class engine(object):
    
    def __init__(self):
        pass
   
    def build(self, entityregex, indexregex, fkregex):
        pass

class redisengine(engine):
    def __init__(self, host, port):
        try:
            self.db = redis.StrictRedis(host, port)
            self.db.set("nosql2sql-engine", "1")
            self.db.delete ("nosql2sql-engine")
        except Error as e:
            raise Error("Unable to connect to Redis database: %s" % e.value)   
    
    def build(self, entityregex, indexregex, fkregex):

        enityattrib = {}
        for e in self.db.keys(entityregex):
            entity = e[0:e.find(":")]
            tmp_atrib = {}
            for key in self.db.hgetall(e):
                oldlength = tmp_atrib.get(key)
                tmp_atrib[key] = len(self.db.hget(e, key))
                if oldlength > tmp_atrib[key]:
                    tmp_atrib[key] = oldlength
            enityattrib[entity] = tmp_atrib
        
        return {"rows" : self.db.keys(entityregex), "entities" : enityattrib.keys(),
                "index" : self.db.keys(indexregex), "attributes" : enityattrib}
        
        

