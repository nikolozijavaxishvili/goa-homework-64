#  for ციკლის საშვალებით დაბეჭდეთ რიცხვები 0-იდან 20-მდე, შეამოწმეთ თითოეული რიცხვი ლუწია თუ კენტი, თუ ლუწია დაბეჭდეთ "even" თუ კენტია დაბეჭდეთ odd და გვერდზე მიუწერეთ ეს რიცხვი თითოეულ შემთხვევაში


# task 1


for i in range(20):
    if  i % 2 == 0:
       print("even", i) 
    else:
      print("odd", i)




# task 2


i = 0

while i < 20:
   if i % 2 == 0:
    print("even", i)  
else:   
    print("odd", i )




# task 3


name = "javaxa"
user = input(" enter your name ")
if user == name:
    print(" coincidence ")







score = int(input("enter you score"))
if score >= 70:  
       print("you passed yay ")

else:
       print("you faled daim ")








score = int(input("enter you score"))
if score >= 70: 
     print("A")

if score >= 60: 
     print("b")

if score >= 50: 
     print("c")


if score >= 35: 
     print("d")


if score >= 20: 
     print("f")
