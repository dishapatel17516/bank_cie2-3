def bank(acc_bal,withd_amt):
    acc_bal = int(sys.argv[1])
    withd_amt = int(sys.argv[2])

    acc_bal_f = acc_bal + withd_amt
    print("Account balance: ",acc_bal)
    print("Withdrawal amount: ",withd_amt)

    if acc_bal_f < 1000:
       print("insufficent balance")
    else
       print("sufficient balance")