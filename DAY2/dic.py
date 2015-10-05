m={1:'jan',2:'feb',3:'mar',4:'apr',5:'may',6:'jun',7:'jul',8:'aug',9:'sep',10:'oct',11:'nev',12:'dec'}
d1={'1':'numan','b':15,25:35.25}
d2={1:786}
print d1
print min(d1)
print max(d1)
print len(d1)

print d1.items()	
print d1.keys()
print d1.values()
print d1.get('b')
print d1.has_key(1)
d1.update(d2)
print d1
d1.clear()	
print d1

#print mont.get(1)
