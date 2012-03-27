import argparse
from ddlgen import DDLGen       

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Redis SQL generator')
    parser.add_argument('--host', dest='host', type=str, default='localhost', help='Redis host')
    parser.add_argument('--port', dest='port', type=int, default=6379, help='Redis port')
    parser.add_argument('--action', dest='action', type=str, default='all', 
                        help='Select ddl, dml or all to be generated')
    parser.add_argument('--ddlfilename', dest='ddlfilename', type=str, default='ddl.sql', 
                        help='Output Data Definition Language Filename')
    parser.add_argument('--dbname', dest='dbname', type=str, default='REDISDB', 
                        help='Output Data Definition Language DATABASE NAME')    
    parser.add_argument('--dmlfilename', dest='dmlfilename', type=str, default='dml.sql', 
                        help='Output Data Modification Language Filename')
    options = parser.parse_args()
    
    if options.action == 'all' or options.action == 'ddl':
        ddl = DDLGen(options.ddlfilename, options.host, options.port)
        ddl.getDDL(options.dbname)
        
    # TODO: DML
