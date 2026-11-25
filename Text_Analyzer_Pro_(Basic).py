p = input("Enter your paragraph : ")
ws = input("Enter the word which you want to search : ")
wr = input ("Enter the word which you want to replace : ")
rw = input ("Enter the word which you want there in place of replaced word : ")
x = len(p)
z = len(p.split())
a = p.count(ws)
b = p.replace(wr,rw)
r = p.upper()
s = p.lower()
sc = 0
previous = ""
for ch in p:
    if ch in "!.?" and previous not in "!.?":
        sc +=1
    previous = ch 
print ("*"*10,"Text Analyser Pro","*"*10)
print(f"Character count : {x}")
print(f"Word Count : {z}")
print(f"Sentence count : {sc}")
print(f"Search Word Occurance : {a}")
print(f"Replaced paragraph : {b}")
print(f"Uppercase paragraph : {r}")
print(f"Lowercase paragraph : {s}")
print ("*"*39)

