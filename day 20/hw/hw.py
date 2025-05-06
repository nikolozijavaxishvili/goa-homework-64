"""   შექმენით პროგრამა რომელიც მომხმარებლისგან მიიღებს რიცხვს, შემდეგ დაადგენს დადებითია, უარყოფითი თუ ნული if-elif-else ის საშვალებით, თუ რიცხვი დადებითია შეამოწმეთ არის თუ არა ლუწი თუ არის დაბეჭდეთ "The number is positive and even." ხოლო სხვა შემთხვევაში დაბეჭდეთ "The number is positive and odd."  """


number = int(input("enter number"))


if number > 0:
    print("dadebitita")

    if number % 2==0:
           print("ricxvi dadebitia da luwia")

   
    else:
        print("")    
else:
     print("neagtiuri ricxvi ")   











