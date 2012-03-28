from errors import Error
from ConfigParser import SafeConfigParser
from datetime import datetime
import argparse
import pickle

class DDLGen(object):
    
    def __init__(self, name):
        try:
            self.name = name
            f = open('%s.pkl' % self.name, 'r')
            self.idx = pickle.load(f)
            self.ddl = open("%s_ddl.sql" % self.name, 'w')
        except Error as e:
            raise Error("%s: Unable to open files: %s" % (self.name, e.value))  
        else:
            f.close()
    
    def generate(self):
        self.title()
        self.database()
        self.table()
        self.index()
        self.ddl.close()
    
    def title(self):
        self.ddl.write("-- NoSQL 2 SQL generator\n")
        self.ddl.write("-- https://github.com/tomplace/nosql2sql.git\n")
        self.ddl.write("-- DateTime: %s\n\n" % datetime.now())
        
    def database(self):
        self.ddl.write("-- Creating output database\n")
        self.ddl.write("CREATE DATABASE %s\n" % self.name)
        self.ddl.write("GO\n\n")
        
    def table(self):
        for e in self.idx['entities']:
            self.ddl.write("-- Creating table %s\n" % e)
            self.ddl.write("CREATE TABLE %s {\n" % e) 
            [self.ddl.write ("    [%s] VARCHAR(%s) NULL, \n" % (k,v)) for k,v in self.idx['attributes'][e].items()]
            self.ddl.write("}\n")     
            self.ddl.write("GO\n\n")
        
    def index(self):
        for i in self.idx['index']:
            e, a = i.split('_')
            self.ddl.write('CREATE NONCLUSTERED INDEX %s ON %s(%s)\n' % (i,e,a))
            self.ddl.write("GO\n\n")
        
        
if __name__ == "__main__":
    
    argparser = argparse.ArgumentParser(description='NoSQL to Python indexer')
    argparser.add_argument('--configfile', dest='conf', type=str, default='db.ini', help='Configuration File')
    args = argparser.parse_args()
    confparser = SafeConfigParser()
    confparser.read(args.conf)
    
    for section in confparser.sections():
        ddl = DDLGen(section)
        ddl.generate()