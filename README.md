Big data project

0. Environment

	● OS X, Java 1.8.0_111, python 2.7, Hadoop 2.7.3, Spark 2.0.1, MySQL
	
	● Python packeges: sqlalchemy

1. Down load dataset

	● Go to NYC Open Data to down load dataset exported as .csv , https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95, and put it under this project folder.

2. Run command

			python dataclean.py [year] [K]
			
			#year = 2012 ~ 2026, K is number of centers