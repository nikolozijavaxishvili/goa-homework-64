"""  მოხმარებელს შემოატანინეთ რიცხვი, შემდეგ კი დაუბეჭდეთ ეს რიცხვი დადებითია, უარყოფითი თუ ნეიტურალი ანუ ნული. შემდეგ კომენტარებით ახსენით რა გასნხვავებაა if-სა და elif-ს შორის რატომ არ შეიძლება ზოგერ elif-ს ნაცვლად if-ის გამოყენება  """  
number = int(input("enter number"))

if number > 0: 
           print("dadebiti")

elif number ==0: 
           print("neitraluri")           

else: 
      print("uaryofitia")


# if viyenebt pirvel pirobis shesrulebashi 
# elifi damatebit pirobis shesasrulebat 




""" მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ თუ ეს რიცხვი დადებითია დაბეჭდეთ ეს და კიდევ შეამოწმეთ ლუწია თუ კენტი, ხოლო თუ არაა დადებითი მხოლოდ დაბეჭდეთ რომ უარყოფითია """



number = int(input("enter number"))


if number > 0:
    print("yes")

    if number % 2==0:
           print("luwia")


    else:
        print("kentia")    
else:
     print("neagtiuri ricxvi ")   








"""  შექმენით ბოსტენულის სია და დაბეჭდეთ მთლიანად, შემდეგ კი ამ სიაში ელემენტების პოზიციების საშვალებით დაბეჭდეთ თითეული სიის ელემენტი ცალ-ცალკე  """





list = [ "banana" "aple"  "grape"  "melon"    ]


print(list (0))
print(list (1))
print(list (2))
print(list (3))




           