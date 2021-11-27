import shell

while True:
    try:
        sample="""if (var_1 == 2, 0, if (var_2 == 4, 15, 0) ) + if (var_2 == 3, 5, 0) - if (var_4 == 2, 0, 5) + if (var_3 == 3, 5, 0) """
        inpt = input("Enter variable as object:  ")
        shell.run(sample, inpt)
    except Exception as e:
        print(e)

#input example
# {var_1: 1, var_2: 4, var_3: 2, var_4: 3}
