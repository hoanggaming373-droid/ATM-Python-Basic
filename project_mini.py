tai_khoan = []
dang_nhap_thanh_cong = False
account_logined = None
def create_account():
    print("------Sign Up------")
    so_du = 0
    while True:

        input_create_account = input("Input Account: ").strip()
        if len(input_create_account) < 8 :
            print("phai lon hon hoac bang 8 ky tu!")
        elif " " in input_create_account:
            print("Chua dau cach!")
        else:
            break

    while True:
        input_create_password = input("Input Password: ")
        if len(input_create_password) < 6:
            print("phai lon hon hoac bang 6 ky tu!")
        elif " " in input_create_password:
            print("Chua dau cach!")
        elif input_create_password == input_create_account:
            print("Mat khau trung Tai khoan!")
        else:
            break
    tai_khoan.append({"account" : input_create_account,"password" : input_create_password, "so_du" : so_du})
    print("Dang ky thanh cong...")

def log_in_account():
    global dang_nhap_thanh_cong, account_logined
    print("------Log In------")
    while True:
        input_account = input("Input Acoount: ")
        input_password = input("Input Password: ")
        for check_accounts in tai_khoan:
            if input_account == check_accounts['account'] and input_password == check_accounts['password']:
                print("Dang Nhap Thanh Cong")
                dang_nhap_thanh_cong = True
                account_logined = check_accounts
                return
        print("Sai tai khoan hoac mat khau !")
 

def deposite_money(account_logined):
    print("------DEPOSIT MONEY------")
    while True:
        try:
            amount = int(input("Amount: ").strip())
            if amount < 0 :
                print("! Error !")
                break
            elif " " in str(amount):
                print("Chua ky tu dau cach !")
                break
            else: 
                account_logined["so_du"] += amount
                print(f"Nap tien thanh cong! So du hien tai: {account_logined['so_du']}")
                break
        except ValueError:
            print("! ERROR !")
            break

def withdraw_money(account_logined):
    print("------WITHDRAW MONEY------")
    while True:
        try:
            amount = int(input("Amount: ").strip())
            if amount < 0 :
                print("! Error !")
                break
            elif amount > account_logined['so_du']:
                print("So du khong du!")
                break
            elif " " in str(amount):
                print("Chua ky tu dau cach !")
                break
            else:
                account_logined['so_du'] -= amount
                print(f"Rut tien thanh cong! So du hien tai: {account_logined['so_du']}")
                break
        except ValueError:
            print("! Error !")
            break


def show_balance(account_logined):
    print("-" * 12)
    print(f"So du hien tai: {account_logined['so_du']}")
    print("-" * 12)
    

def menu_LogIn_SignUp():
    print("----------------")
    print("1. Log in")
    print("2. Sign Up")
    print("----------------")
    while True:
        try:
            choices_LogIn_SignUp = int(input("Choices(1 or 2): "))
            if choices_LogIn_SignUp == 1 :
                if account_logined == None:
                    print("Chua co tai khoan!")
                    continue
                log_in_account()
                break
            if choices_LogIn_SignUp == 2:
                create_account()
                log_in_account()
                break

        except:
            print("! Error !")    
            continue

def menu_choices():
    print("1. Xem Số Dư")
    print("2. Nạp Tiền")
    print("3. Rút Tiền")

def choice_in_menu_choices(account_logined):
    while True:
        try:
            input_choice = int(input("Input Your Choice: ").strip())
            if input_choice == 1:
                show_balance(account_logined)
            elif input_choice == 2:
                deposite_money(account_logined)
            elif input_choice == 3:
                withdraw_money(account_logined)
            else:
                print("! Error !")
                continue
        except: 
            print("! Error !")
            break

def main_menu():
    menu_LogIn_SignUp()
    if dang_nhap_thanh_cong:
        menu_choices()
        choice_in_menu_choices(account_logined)

main_menu()
    

        
        



    


    