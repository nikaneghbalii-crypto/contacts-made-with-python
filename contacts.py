def add(name, number):
    with open("contacts.txt", "a") as cons :
        content = cons.write(name + " " + number + "\n" )
def search(number, name):
    cons = open("contacts.txt", "r")
    content = cons.read()
    if number in content or name in content:
        cons.close()
        return number + " " + name
    else:
        print("Contact Not Found")
        cons.close()
    
def delete(name, number):
    cons = open("contacts.txt", "r")
    content = cons.readlines()
    conts = []
    for lines in content:
        if name not in lines and number not in lines:
            conts.append(lines)
    cons.close()
    cons = open("contacts.txt", "w")
    cons.writelines(conts)

while 1 < 2:
    inpt = str(input("""
   ***Welcome***
   1.add
   2.search
   3.delete
   4.close
"""))

    if inpt == "1":
        adingcontct = add(str(input("name: ")), str(input("number: ")))
        print("contact added!")
    if inpt == "2":
        srch = search(str(input("number: ")), str(input("name: ")))
        print(srch)
    if inpt == "3":
        dlt = delete(str(input("name: ")), str(input("number: ")))
    if inpt == "4":
        print("bye hava goood timen")
        break
