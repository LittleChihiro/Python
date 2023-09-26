def greeter():
    print("Wilkommen in der Anwendung")
    
def sum(summand1, summand2, *args):
    summe = summand1 + summand2
    for summand in args:
        summe += summand
    return summe 