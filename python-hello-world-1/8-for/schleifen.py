#Liste 
namen = ["Alice", "Bob", "Carol", "Dave", "Eve"]
alter = [25, 18, 37, 32, 21]


    
#i = 0
#while i < len(namen):
#   print("{0} ist {1} Jahre alt".format(namen[i], alter[i]))
#   i += 1
    
    
entfernungen = {
    "Merkur": 58000,
    "Venus": 108,
    "Erde": 150,
    "Mars": 228,
    "Jupiter": 778,
    "Saturn": 1427,
    "Uranus": 2884,
    "Neptun": 4509
}


    
#range()

for i in range(0, 10):
    for j in range(0, 10):
        print("{0} * {1} = {2}" .format(i, j, i*j))
        
    print("")