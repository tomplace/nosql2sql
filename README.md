# NoSQL 2 SQL 

An experimental SQL reverse engineering tool for nosql databases (currently Redis)

## Description
	Configure one to many 'Indexer' threads which will build python data structures representing the object relational state of a redis database
	These index's run on a defined schedule to stay current with changing data and implied schema
	Run batch processes to generate both DDL and DML from these indexers on demand   
	Its intended use case is a batch 'dump' of a nosql database into a relational model to facilitate reporting and integration with legacy tools

## Installation

    $ git clone https://github.com/tomplace/nosql2sql

## Getting Started

### Configuration	
	Edit db.ini to specify your nosql database (currently redis supported), specify the timing of your index rebuild and pass in the regex's that match the objects 
	the engine should consider as entities, index's and foreign keys.      

### Run 
	$> python indexer.py

## Notes
* Assumes 'entities' are hashmaps
* Assumes 'indexes' are sets

## Roadmap

This is currently a very bare-bones implementation. Contributions are encouraged!

The following is on the roadmap:
* Data Type indentification
* NULL / NOT NULL indentification
* Multi key indexes
* Add FK support
* Data migration   
* This solution may not scale well to complex or large databases. As such additional optionality and control options around the indexing is planned 
* Additional support for other nosql databases 
* Tested with SQL Server, extensions to other output RDBMS 
* Better IPC (Vs Pickle used today)

## Author
NoSQL 2 SQL is developed and maintained by Thomas Place (thomas.place@gmail.com)
It can be found here: https://github.com/tomplace/nosql2sql.git






