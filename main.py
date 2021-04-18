def swapp () :
    F1 = input (" Enter your 1st file name")
    F2 = input (" Enter your 2nd file name")

    with open (F1 , "r" )as a :
       Data1  = a.read()

    with open (F2 , "r" )as b :
       Data2  = b.read()

    with open (F1 , "w" )as a :
       a.write(Data2) 

    with open (F2 , "w" )as b :
       b.write(Data1)


swapp()


