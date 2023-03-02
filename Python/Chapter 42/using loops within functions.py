def func(params):
    for value in params:
        print ('Got value {}'.format(value))
        if value == 1:
            print (">>>> Got 1")
            return
        print ("Still looping")

func([5, 3, 1, 2, 8, 9])