import argparse
from ConfigParser import SafeConfigParser
import engine
import threading
from datetime import datetime, timedelta
import time

class Indexer(threading.Thread):
    
    def __init__(self, type, host, port, interval):
        if type == 'redis':
            self.engine = engine.redisengine(host, port)
            self.interval = interval
    
    def run(self):
        while(True):
            start = datetime.now()
            self.engine.buildindex()
            end = datetime.now()
            if (end - start) < timedelta(seconds = self.interval):
                time.sleep(self.interval)
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='NoSQL to SQL generator')
    parser.add_argument('--configfile', dest='conf', type=str, default='db.ini', help='Configuration File')
    options = parser.parse_args()
    confparse = SafeConfigParser()
    confparse.read(options.conf)
    
    for section in confparse.sections():
        Indexer(confparse.get(section, "Type"),
                confparse.get(section, "Host"),
                confparse.get(section, "Port"),
                confparse.get(section, "IndexInterval").start())