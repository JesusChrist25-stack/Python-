shop = input("Enter what do you want : ")
if (shop == "boot"):
    print('Yeah we got boot ^^ ')
    boot = input("What brand do you want Nike/Adidas: ")
    if (boot == "Nike"):
        print ("Yeah we have Nike boot") 
    size = input("Could you please tell me your size 8/10: ")
    if (size == "8"):
        print("Yeah we have number 8 size ^^ ")
        print("Thank you for Purchasing")
    elif (size == "10"):
        print ("Yeah we have number 10 size ^^")
        print("Thank you for Purchasing")
    else:
        print(" No sorry we don't have other size")   
        print ("Next time you'll get") 

elif(shop == "Puma"):
    print("Sorry! Bro we have only Two Brands Nike and Adidas")
else:
    print("I Don't understand you Bro")