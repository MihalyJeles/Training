while True:
    p1 = (input("Please give me the password:"))
    p2 = (input("Please confirm the password:"))
    if p1 == p2:
        print("Your password is saved!")

        try:
            file = open("code.txt", 'w')
            file.write(p1 + '\n')
        except FileNotFoundError as e:
            print("Unable to open file: "+ str(e))
        finally:
            file.close()
        break
    else:
        print("Password do not match!")
