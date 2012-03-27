from errors import Error
from datetime import datetime
from client import Client
        
class DDLGen(object):
    
    def __init__(self, filename, host, port): 
        
        self.client = Client(host, port) 

        try:
            self.f = open(filename, 'w')
        except IOError:
            raise Error("unable to open output file: %s" % filename) 
        else:
            self.f.write("-- Redis SQL generator\n")
            self.f.write("-- https://github.com/tomplace/relational_redis.git\n")
            self.f.write("-- Host: %s\n" % host)
            self.f.write("-- Port: %s\n" % port)
            self.f.write("-- DateTime: %s\n\n" % datetime.now())
            
    def getDDL(self, dbname):
        #TODO: Allow subset of DDL to be called     
        self.database(dbname)
        for e in self.client.entities:
            self.table(e)
            
        for i in self.client.indices:
            self.index(i)

    def table(self, e):
        self.f.write("-- Creating table %s\n" % e)
        self.f.write("CREATE TABLE %s {\n" % e)  
        
        # TODO: Figure out datatypes 
        columns={}  
        for a in self.client.rows:
            row = self.client.server.hgetall(a)
            for key in row:
                oldmax = columns.get(key)
                columns[key] = len(row[key])
                if oldmax > len(row[key]):
                    columns[key] = oldmax
        
        # Write Columns
        for item in columns:
            self.f.write ("    [%s] VARCHAR(%s) NULL, \n" % (item, columns[item]))
        self.f.write("GO\n\n")
    

    def index(self, i):
        #TODO: Index
        pass 

    def database(self, dbname):
        self.f.write("-- Creating output database\n")
        self.f.write("CREATE DATABASE %s\n" % dbname)
        self.f.write("GO\n\n")
