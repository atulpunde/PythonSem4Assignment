# Atul Rajaram Punde
# Roll No 1655

# Q5.	Write python program to create BankAccount class with deposit, withdraw functions.
# Use exception handling if sufficient amount is not available for withdrawal of amount.
# Write Custom exception.

# custom exception 
class AccountBalanceException(Exception):       # inherit class from base class Exception 
    def __init__(self,str):     
        super().__init__(str)                   # invoke constructor of base class using super() 

class Bank(object):
    pin = 0.0   # initial declaration
    accBal = 0.0    #Initial account balance 

    def __init__(self,pin):
        self.pin = pin

    def Withdraw(self,nAccBal):
        if nAccBal>self.accBal:     # Main account balance should be grater than withdrawal amount
            return False
        else:
            self.accBal = self.accBal - nAccBal # If condition satisfy deduct amount from account
            return self.accBal

    def Deposit(self,nAccBal):
        self.accBal = self.accBal + nAccBal # simply add amount to account balance 
        return self.accBal

    def ViewBalance(self):
        return self.accBal  # Returning currnt balance 

    def changePin(self,pin):
        self.pin = pin  # replace previous pin 

    def verifiedUser(self,pin):
        if pin == self.pin: # If pin is matched to saves pin
            return True
        else:
            return False

def wantToContinue():   # Instead of writing repeating code I have function for code reduciability
    choice = input("\nDo you want to continue..? (Y/N) ")
    if choice == 'y' or choice == 'Y':
        return True
    else:
        return False

if __name__ == "__main__":  # Appropriate way to start python code.
    print("\n-------- WELCOME TO BANK --------")

    while True:
        try:
            pin = int(input("\nEnter your pin : "))
            if (len(str(pin))!=4) or (pin<=1):                # validation of PIN
                print("\nLength of PIN should be exactly 4.")
                continue
            else:
                bank = Bank(pin)   
                break
        except ValueError as v:
            print("\nPIN should be integer : ",v)
            continue

    while True:
        try:
            print("\n1. Withdraw")
            print("2. Deposit")
            print("3. View Balance")
            print("4. Change PIN")
            print("5. EXIT")
            ch = int(input("Enter Your Choice = "))

            if ch==1:
                while True:
                    try:
                        pin = int(input("\nEnter your pin : "))
                        if len(str(pin))!=4 or pin<=1:                # validation of PIN
                            print("\nLength of PIN should be exactly 4.")
                            continue
                        else:
                            break
                    except ValueError as v:
                        print("\nPIN should be integer : ",v)
                        continue
                
                try:
                    if bank.verifiedUser(pin):                      # did tansaction only if user is varified 
                        accBal = float(input("Enter amount to debit : "))
                        if accBal<=0:
                            print("\nAmount is not valid..Try again..")
                            continue
                        balance = bank.Withdraw(accBal)
                        if balance == False:
                            raise AccountBalanceException("\nInsufficient account balance.")
                            # Raised custom exception, if sufficient amount is not available for withdrawal of amount
                        else:
                            print("\nRemaining account balance is : ",balance," Rs")
                    else:
                        print("\nPIN is Incorrect..\nTry Again..\n")
                except AccountBalanceException as accbalexception:
                    print(accbalexception)

                if wantToContinue():
                    continue
                else:
                    break
                
            if ch==2:
                while True:
                    try:
                        pin = int(input("\nEnter your pin : "))
                        if len(str(pin))!=4 or pin<=1:                # validation of PIN
                            print("\nLength of PIN should be exactly 4.")
                            continue
                        else:
                            break
                    except ValueError as v:
                        print("\nPIN should be integer : ",v)
                        continue

                try:
                    if bank.verifiedUser(pin):  # If user is verified give access to acount
                        nAccBal = float(input("\nEnter amount to Credit : "))
                        if nAccBal<=0:
                            print("\nAmount is not valid..Try again..")
                            continue
                        print(f"\nYur account has been deposited {nAccBal} Rs")
                        print("\nNew account Balance is ",bank.Deposit(nAccBal)," Rs only.")
                    else:
                        print("\nPIN is Incorrect..\nTry Again..\n")
                except ValueError as v:
                    print("\nAmount is not valid..")
                if wantToContinue():
                    continue
                else:
                    break

            if ch==3:
                while True:
                    try:
                        pin = int(input("\nEnter your pin : "))
                        if len(str(pin))!=4 or pin<=1:                # validation of PIN
                            print("\nLength of PIN should be exactly 4.")
                            continue
                        else:  
                            break
                    except ValueError as v:
                        print("\nPIN should be integer : ",v)
                        continue

                if bank.verifiedUser(pin):  # If user is verified give access to acount
                    print("\nYour current account balance is : ",bank.ViewBalance()," Rs only.")
                else:
                    print("\nPIN is Incorrect..\nTry Again..\n")
                if wantToContinue():
                    continue
                else:
                    break

            if ch==4:
                while True:
                    try:
                        pin = int(input("\nEnter your pin : "))
                        if len(str(pin))!=4 or pin<=1:                # validation of PIN
                            print("\nLength of PIN should be exactly 4.")
                            continue
                        else: 
                            break
                    except ValueError as v:
                        print("\nPIN should be integer : ",v)
                        continue

                try:
                    if bank.verifiedUser(pin):
                        pin = int(input("\nEnter new pin : "))
                        new_pin = int(input("Enter again to confirmed : "))
                        if pin == new_pin:      # strictly checked password condition
                            bank.changePin(pin)
                            print("\nPIN changed Successfully...")
                        else:
                            print("\nPIN is Incorrect..\nTry Again..\n")
                    else:
                        print("\nPIN is Incorrect..\nTry Again..\n")
                except ValueError as v:
                    print("\nYour PIN is invalid..")

                if wantToContinue():
                    continue
                else:
                    break

            if ch == 5:
                print("\nSuccessfully EXIT...")
                break
            if ch>=5:
                print("\nEnter proper choice...\n")
        except ValueError as e: 
            print("\nError : ",e)

print("\nBank is closed...")