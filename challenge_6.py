def parrot_trouble(talking,hour):
    if(talking and (hour<7 or hour>20)):
        print('True')
    else:
        print('False')
hour=int(input("Enter talking hour:"))
parrot_trouble(hour)