#coding: utf-8

for i in range(1,128):
	f = open("RS/sound"+str(i)+".RS",'r+b')
	res=f.read()
	f.close()
	j=1
	foo = open("csvA/soundA"+str(i)+".csv",'w')
	foo.write("x0,y\n")
	bar = open("csvB/soundB"+str(i)+".csv",'w')
	bar.write("x0,y\n")
	res = res.split("\n")
	for r in res:
		e = r.split(",")
		foo.write(str(j)+","+e[0]+"\n")
		bar.write(str(j)+","+e[1]+"\n")
		j+=1
	foo.close()
	bar.close()
	print "FILES CSV #"+str(i)+" CREATED. OK. DONE."
	