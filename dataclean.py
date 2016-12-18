import os,sys
from sqlalchemy import *

DATABASEURI = "mysql+pymysql://root:940611@localhost/project"

engine = create_engine(DATABASEURI)

###### choose a year 2012~2016
year = int(sys.argv[1])
numCenter = int(sys.argv[2])

try:
	conn = engine.connect()
except:
	print "uh oh, problem connecting to database"
	conn = None
	
if conn != None:	
	cur = conn.execute('''
	SELECT LOCATION
	FROM collision c
	WHERE c.cDATE >= %s AND c.cDATE < %s;
	''',(str(year)+'-01-01',str(year+1)+'-01-01'))
	
	filename = './location/'+'T'+str(year)+'.txt'
	print filename
	f = open(filename,'w')	
	i = -1
	for result in cur:
		#print result
		if result != (None,) :
			i = i + 1
			t = str(result).strip("('")
			t = t.strip("',)").split(',')
			ele = str(i) + ' 1:' + t[0] + ' 2:' + t[1].lstrip(' ') + '\n'
			f.write(ele)
	f.close()
	try: os.system("hadoop dfs -put " + filename)
	except: print 'file exists'
	os.system("spark-submit kmeanCluster.py " + str(year) + " " + str(numCenter) )
	os.system("open ./mapmarker/where.html")
conn.close()	