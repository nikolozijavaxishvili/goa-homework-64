"""  2) შექმენით 5 ცვლადი რომლებშიც შეინახავთ წიგნების თავდაპირველ ფასს, შემდეგ შექმენით ცვლადი რომელშიც შეინახავთ ფასდაკლების ოდენობას, შექმენით ახალი ფასის მქონე წიგნების ცვლადები, რომელთა მნიშვნელობა იქნება ძველ მნიშვნელობას გამოკლებული ახალი, საბოლოოდ კი დაბეჭდეთ ახალი წიგნების ფასები (გამოიყენეთ კარგი მიდგომები: რომ ცვლადის მნიშვნელობის მინიჭებისას შეგიძლიათ სხვა ცვლადის გამოყენება, კოდი ახსენით კომენტარების საშვალებით, ცვლადებს დაარქვით აღმწერი სახელები snake_case-ის სტილში)     """

book1 = 90    
book2 = 21
book3 = 67
book4 = 321
book5 = 12

pasdakleba = 4

newbook1 = book1 // pasdakleba 
newbook2 = book2 // pasdakleba 
newbook3 = book3 // pasdakleba 
newbook4 = book4 // pasdakleba 
newbook5 = book5 // pasdakleba 

print(newbook1)
print(newbook2)
print(newbook3)
print(newbook4)
print(newbook5)


""" 3) (ტექსტურ ფაილში) თქვენი სიტყვებით ახსენით რა არის input და output, მოიყვანეთ მაგალითები და დაურთეთ სურათები  """

# inputi aris ekrans rom sheexebi da gamozravdeba 
# output aris yursasmens rom sheaerteb da yursasmenshi xmar rom gaigoneeb 

""" 4) დაწერეთ პითონის კოდი რომელიც მომხმარებელს input-ის საშვალებით შეეკითხება და ცვლადში შეინახავს შემდეგ ინფორმაციას: """

name = input ("enter your name")
surname = input ("enter your surname")
age = input ("enter your age")
location = input ("enter your nlocation (city)")
occupation = input ("enter your occupation")
hobby = input ("enter your hobby")
print(name +" "+ surname +" "+ age +" "+ location +" "+ occupation +" "+ hobby  )


""" 5) შექმენით 10 string ტიპის და 10 ინტეჯერ ტიპის ცვლადი, გააკეთეთ 5 კონკატინაციისა (სტრინგების შეერთების) და 5 მათემატიკური ჯამის მაგალითი  """

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
num6 = 6
num7 = 7
num8 = 8
num9 = 9
num10 = 10

print(num1 + num2)
print(num3 + num4)
print(num4 + num5)

print(num1 / num2)
print(num3 = num4)
print(num4 *  num5)
