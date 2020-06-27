check = {
    o"Personal": "bigbaw-busguh-5jEqse",
    "Finance": "fimfoj-syqmu0-byKpuw",
    "Programming": "janput-myzqyk-2gUxpe",
    "Other Sites": "camqeg-9zagko-woddoW",
    }


def cont():
    """To break a loop"""
    cont = input("Do you want to continue? [yes/no]")
    while True:
        if cont != "yes":
            cont_code = False
        else:
            check_pass()

def check_pass(run_code=True, cont_code=True):
    
    """ask you enter type of password to check"""
      
    while run_code:
        type_pass = input("Enter what I should check?")
        if type_pass.title() == "Personal":
            while cont_code:
                if check["Personal"] == input("Enter password: "):
                    print("Valid")
                    cont()
                else:
                    print("\nTry one more time. Enter type right.")
                    check_pass()
        if type_pass.title() == "Finance":
            while cont_code:
                if check["Finance"] == input("Enter password: "):
                    print("Valid")
                    cont()
                else:
                    print("\nTry one more time. Enter type right.")
                    check_pass()
        if type_pass.title() == "Programming":
            while cont_code:
                if check["Programming"] == input("Enter password: "):
                    print("Valid")
                    cont()
                else:
                    print("\nTry one more time. Enter type right.")
                    check_pass()
        if type_pass.title() == "Other":
            while cont_code:
                if check["Other Sites"] == input("Enter password: "):
                    print("Valid")
                    cont()
                else:
                    print("\nTry one more time. Enter type right.")
                    check_pass()

        else:
            print("Invalid input. Try again.")
            run_code = False

check_pass()
