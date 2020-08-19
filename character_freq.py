s = input("enter a string: ")
dic = {}
for n in s:
    z = s.count(n)
    dic[n] = str(z)
                                             
tuple1 = tuple(dic)
tuple1 =sorted(dic.items(), reverse = True, key = lambda x : x[1])
print("Output:\n")
for x in tuple1:
    print(x[0] + "=" +x[1])

          
