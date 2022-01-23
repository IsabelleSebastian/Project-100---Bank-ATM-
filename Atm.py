from string import capwords


class atm():
    def __init__(self, CardNum, PinNum, AccBal):
        self.CardNum = CardNum
        self.PinNum = PinNum
        self.AccBal = AccBal

    def AccountBalance(self):
        card = int(input("Enter Card Number: "))
        pin = int(input("Enter Pin Code: "))

        if((card == self.CardNum) and (pin == self.PinNum)):
            print("Current Account Balance: ", self.AccBal)
        else:
            print("Incorrect Verification... try again.")

number = atm(1234, 5678, "$1800")
number.AccountBalance()