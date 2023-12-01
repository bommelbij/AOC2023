with open ("AOC21-1.txt","r") as readfile:
    txt = readfile.readlines()

sum = 0
for line in  txt:
    temp = ""
    for c in line:
        if c.isdigit():
            temp += c
            break
    for c in line[::-1]:
        if c.isdigit():
            temp += c
            break
    sum+= int(temp)
print(sum)

sum = 0
for line in  txt:
    temp = ""
    line =  line.replace("one","o1e")
    line =  line.replace("two","t2o")
    line =  line.replace("three","t3e")
    line =  line.replace("four","f4r")
    line =  line.replace("five","f5e")
    line =  line.replace("six","s6x")
    line =  line.replace("seven","s7n")
    line =  line.replace("eight","e8t")
    line =  line.replace("nine","n9e")
    for c in line:
        if c.isdigit():
            temp += c
            break
    for c in line[::-1]:
        if c.isdigit():
            temp += c
            break
    sum+= int(temp)
print(sum)
