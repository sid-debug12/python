from bank_accounts import *

Dave = bankaccount(1000, "Dave")
Sara = bankaccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(100)

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)

Jim = interestrewardacct(1000, "Jim")
Jim.deposit
Jim.getBalance()
Jim.transfer(100, Dave)

Blaze = savingacct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(1000, Sara)
