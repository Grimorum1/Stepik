# put your python code here
n = input()
x = "+7(123)456-78-99"
res = True
if len(n) == len(x):
    for i in range(len(x)):
        if n[i]==x[i]:
            continue
        else:
            if n[i].isdigit() and i!=1 and x[i].isdigit():
                continue
            res = False
            break
print("ДА" if res else "НЕТ")