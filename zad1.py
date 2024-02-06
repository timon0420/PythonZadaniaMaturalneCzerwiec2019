with open("zadania maturalne czerwiec 2019\liczby.txt", 'r') as f: liczby = [x.rstrip() for x in f]
with open("zadania maturalne czerwiec 2019\pierwsze.txt", 'r') as f: pierwsza = [x.rstrip() for x in f]
def pierw(n):
    for i in range(2,n):
        if n%i == 0:
            return False
        return True
x = [liczba for liczba in liczby if int(liczba) >= 100 and int(liczba) <= 5000 and liczba in pierwsza]
print(x)
# for i in liczby:
#     if int(i) >= 100 and int(i) <= 5000:
#         for x in pierwsza:
#             if i == x:
#                 print(i)