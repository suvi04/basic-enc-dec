while True:
    wt_todo=input("Encrypt(e) or Decrypt(d) ? ")
    if wt_todo=="e":
        numbr=int(input("Enter number "))
        nw_numbr=(numbr*4)-21
        print("The encrypted number is ",nw_numbr)
    if wt_todo=="d":
        nmbr=int(input("Enter number "))
        nw_nmbr=(nmbr+21)/4
        print("The decrypted number is ",nw_nmbr)
