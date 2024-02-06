with open("zadania maturalne czerwiec 2019\liczby.txt", 'r') as f: liczby = [x.rstrip() for x in f]
with open("zadania maturalne czerwiec 2019\pierwsze.txt", 'r') as f: pierwsza = [x.rstrip() for x in f]
def pierw(n):
    for i in range(2,n):
        if n%i == 0:
            return False
        return True
for liczba in liczby:
    x = liczba[::-1]
    if pierw(int(x)):
        print(liczba)