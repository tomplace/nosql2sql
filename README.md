# relational_redis

An experimental SQL reverse engineering tool for nosql databases (currently Redis)

## Installation

    $ git clone https://github.com/tomplace/nosql2sql

## Getting Started

	TBD    

## Notes
* Relies on patters established by Kevin Manleys redisql client (https://github.com/kmanley/redisql.git)
* 'Rows' are assumes to be of the name <entity>:<id>
* 'Index's' are assumed to be of name <entity>_<column>
* 'Primary Key' is assumed to be <enity>_id

## Roadmap

This is currently a very bare-bones implementation. Contributions are encouraged!

The following are on the roadmap:

* potential re-engineering of the patterns in the notes above (dependent on https://github.com/kmanley/redisql.git))
* data type identification 
* dml creation 

Author
------
relational_redis is developed and maintained by Thomas Place (thomas.place@gmail.com)

It can be found here: https://github.com/tomplace/relational_redis.git

License
------
MIT License (MIT)

relational_redis Copyright (c) 2012 Thomas R. Place

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.





