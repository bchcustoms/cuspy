========
meursing
========


.. image:: https://img.shields.io/pypi/v/meursing.svg
        :target: https://pypi.python.org/pypi/meursing

.. image:: https://img.shields.io/travis/bchcustoms/meursing.svg
        :target: https://travis-ci.com/bchcustoms/meursing

.. image:: https://readthedocs.org/projects/meursing/badge/?version=latest
        :target: https://meursing.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Meursing coder - creates customs master data for agrifood products requiring a four-digit additional code for customs and duty purposes


* Free software: MIT license
* Documentation: https://meursing.readthedocs.io.


Features
--------

"Meursing codes" are 4 digit codes owned and managed by the EU for the purpose of applying customs import duties to certain agri-food products 
according to their key agricultual ingredients. Only products falling under certain TARIC commodity codes require the determination of the additional MEURSING code,
thus the accurate base classification for agri-food imported products is key. 

If a product falls into one of the affected TARIC codes, the importer needs to apply analytical data regarding the ingredioent compositions (and there are specific 
analytical methods defined for this) to get to the 4 digit MEURSING code.

The relevant agricultural components groups (dimensions) are:
- milk fat
- milk protein
- starch/glucose
- sucrose/invert sugar

There are some services that enable a user input the % ingredient contents to get to the MEURSING code. This software aims to make this available in code form 
e.g. so it can be integrated into a wider application and/or trade master data management/governance programme.


Credits
-------

The data on Meursing codes and associated master data (including customs duties) is based on the European Union law and provisions - see 