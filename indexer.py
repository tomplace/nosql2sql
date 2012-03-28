import argparse
from ConfigParser import SafeConfigParser
import engine
from errors import Error
from threading import Thread
from datetime import datetime, timedelta
import pickle
import time

class Indexer(Thread):
    
    def __init__(self, name, dbtype, host, port,
                 intervaltype, intervalvalue, entityregex, indexregex, fkregex):
        Thread.__init__(self)
        if dbtype == 'redis':
            self.engine = engine.redisengine(host, port)
        self.name = name
        self.intervaltype = intervaltype
        self.intervalvalue = intervalvalue
        self.entityregex = entityregex
        self.indexregex = indexregex
        self.fkregex = fkregex

    def run(self):
        while(True):
            start = datetime.now()
            self.index = self.engine.build(self.entityregex, self.indexregex, self.fkregex)
            try:
                with open("%s.pkl" % self.name, 'wb') as output:
                    pickle.dump(self.index, output) 
            except Error as e:
                raise Error("Unable to open tmp files" % e.value)  
            end = datetime.now()
            if self.intervaltype == "hour":
                if (end - start) < timedelta(hours = self.intervalvalue):
                    time.sleep(self.intervalvalue * 3600)
            
if __name__ == "__main__":
    
    argparser = argparse.ArgumentParser(description='NoSQL to Python indexer')
    argparser.add_argument('--configfile', dest='conf', type=str, default='db.ini', help='Configuration File')
    args = argparser.parse_args()
    confparser = SafeConfigParser()
    confparser.read(args.conf)
    
    workers={}
    
    for section in confparser.sections():
        workers[section] = Indexer(section,
                                   confparser.get(section, "type"),
                                   confparser.get(section, "host"),
                                   int(confparser.get(section, "port")),
                                   confparser.get(section, "indexintervaltype"),
                                   int(confparser.get(section, "indexintervalvalue")),
                                   confparser.get(section, "entityregex"),
                                   confparser.get(section, "indexregex"),
                                   confparser.get(section, "fkregex"))
        workers[section].start()