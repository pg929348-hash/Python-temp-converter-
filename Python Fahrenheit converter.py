print("** fehrenheit to celcius converter**")

while True:
        try:
            feh=float(input(" enter the temperature in fehrenheit :-"))
            cel=(feh-32)*5/9
            print("temperature in celcius  °",(round(cel,2)))
        except:
            print("enter only number")
