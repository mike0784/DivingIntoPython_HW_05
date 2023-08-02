def fibonachi(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        temp = a+b
        a = b
        b = temp
        i += 1
        yield temp

n = int(input("Номер элемента ряда Фибоначчи: "))
rr = fibonachi(n)
print(list(rr))
