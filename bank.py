def bank(acc_bal,withd_amt):
   acc_bal_f = acc_bal - withd_amt

   if acc_bal_f < 1000:
      print("insufficent balance")
   else:
      print("sufficient balance")

   return acc_bal_f

   if __name__ == "__main__":
      acc_bal = int(sys.argv[1])
      withd_amt = int(sys.argv[2])
      acc_bal_f = bank(acc_bal,withd_amt)
      print("final balance: ",acc_bal_f)

