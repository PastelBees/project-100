class Atm(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber

    def cashWithdrawl(self):
        withdrawledMoney = int(input("How much money would you like to withdrawl?: "))
        print(withdrawledMoney, "dollars have been withdrawled from your account.")

    def balanceInquiry(self):
        print("Your account's balance has been updated. Have a nice day!")

    
    

card=Atm(1234567890123456, 2743)
print("Card Number: ", card.cardNumber)
print("Pin: ", card.pinNumber)
print(card.cashWithdrawl())
print(card.balanceInquiry())
