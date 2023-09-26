
def greeter(name, vorname, herkunft="dem Universum"):
    print("Hallo {0} {1}".format(vorname, name))
    print("Du kommst aus {0}".format(herkunft))
    
def sum(summand1, summand2, *args):
    summe = summand1 + summand2
    for summand in args:
        summe += summand
    return summe

def bundesland(**kwargs):
    for name, bundesland in kwargs.items():
        print("{0} kommt aus {1}".format(name, bundesland))


#print(sum(1,2,3))

bundesland(Viktor= 'Canada')









#def sum(summand1, summend2):
#summe = summand1 + summend2
#return summe

#def diff(minuenden, subtrahenden):
#return minuenden - subtrahenden

#def greet():
#print("Hallo!")
        
#greet()    
#print(diff(subtrahenden=10, minuenden=5))
