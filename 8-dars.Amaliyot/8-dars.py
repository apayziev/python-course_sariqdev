"""08-DARS. RO'YXATLAR BILAN ISHLASH"""

#AMALIYOT

#1)
# davlatlar = ["O'zbekisoton", "AQSH", "Germaniya","Rossiya"]
# print(davlatlar)

#2)
# print("Ro'yxat uzunligi -",len(davlatlar))

#3)
# print(sorted(davlatlar))

#4)
# print(sorted(davlatlar, reverse=True))

#5)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

#6)
# sonlar = list(range(120,1200,2))
# print(sonlar)

#7)
sonlar1 = list(range(120,1200))
print(sum(sonlar1))

#8)
# print(max(sonlar1)-min(sonlar1))

#9)
# print(len(sonlar1))

#10)
# print(sonlar1[:20])
# print(sonlar1[530:550])
# print(sonlar1[-20:])

#10)
taomlar = ["osh","somsa","manti","chuchvara","kabob"]

#11)
nonushta = taomlar[:]

#12)
# nonushta.remove('osh')
# nonushta.remove('manti')
# nonushta.remove('somsa')
# nonushta.insert(0, 'shirinlik')
# nonushta.insert(1,'mevalar')
# print(nonushta)
# print(taomlar)
# nonushta=tuple(nonushta)
# nonushta[0]=" qaymoq va non"
# print(nonushta)

#13)
toys = ['taddy', 'bird','car','bus','bear']
toys.append('robot')
toys.remove('bird')
toys = tuple(toys)
print(toys)