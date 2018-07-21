prime_set = set([])
happy_set = set([])
common_set = set([])

prime = open("C:\Anamitra_JnJ_Laptop\Training\Python\PyProject\Challenge\prime.txt", 'r')
happy = open("C:\Anamitra_JnJ_Laptop\Training\Python\PyProject\Challenge\happy.txt", 'r')

for p in prime:
    prime_set.add(int(p))

for h in happy:
    happy_set.add(int(h))


common_set = sorted(prime_set.intersection(happy_set))

overlap = open("C:\Anamitra_JnJ_Laptop\Training\Python\PyProject\Challenge\overlap.txt", 'w+')
for o in common_set:
    print(o)
    overlap.write(str(o)+'\n')




