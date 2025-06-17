if __name__ == "__main__":
    b = int(input("Enter b: "))
    a = int(input("Enter a: "))

def is_valid_inputs(a, b):
    if b > 0 and a > 1:
        if b > a:
            if (b-a) % 2 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

while not is_valid_inputs(a, b):
    print("Invalid input.")
    b = int(input("Enter b: "))
    a = int(input("Enter a: "))
print()

space = int((b-a-2)/2)

if space == 0:
    print(int(2*b-1)*"b")

else:
    print(int(2*b-1)*"b")
    for i in range(space):
        print("b",(2*b-5) * " ","b")

for j in range(a):
    spaces = int(b-j-4)
    if spaces < 0:
        print("b",int(2*j + 1)*"a","b",end="")
        print()
    else:
        print("b",spaces*" ",int(2*j+1)*"a",spaces*" ","b",end="")
        print()

if space == 0:
    print(int(2*b-1)*"b")
else:
    for i in range(space):
        print("b",(2*b-5) * " ","b")
    print(int(2*b-1)*"b")