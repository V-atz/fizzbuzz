#for every multiple of 3 print fizz and for every multiple
#of 5 print buzz and for 15 print fizzbuzz
for number in range(1,101) :
    if number % 3 == 0 and number % 5 == 0 :
        print("fizzbuzz")
    elif number % 3 == 0 :
        print("fizz")
    elif number % 5 == 0 :
        print("buzz")
    else :
        print(number)