"""                                                                               Pragathiswaar AK 12th Computer Science Project                                                                               """
import cryptocode
plain_pass_list = []
enc_pass_list = []

print("**********Encrypted Password Locker**********")
print("Functions Available:\n 1.Encrypt And Upload Your Passwords\n 2.Access Your Encrypted Passwords")
opt = int(input("Which Function Do You Want To Use(1/2):"))
if opt == 1:
    while True:
        choice = input("Do You Want To Upload Your Password To Our Database(y/n):")
        while choice == "y" or choice == "Y":
                plain_pass = input("Enter Your Password:")
                name_pass = input("What Do You Want To Name This Password:")
                llist = [name_pass,plain_pass]
                plain_pass_list.append(llist)
                again = input("Do You Want To Upload Another Password(y/n):")
                if again == "n" or again == "N":
                        break
        key = input("Please Enter A Key Which You Will Need To Access All Your Passwords:")
        database_name = input("What Do You Want Us To Name Your Database:")
        for i in plain_pass_list:
                plain_pwd = i[1]
                name_pass = i[0]
                enc_pwd = cryptocode.encrypt(plain_pwd,key)
                llist = [name_pass,enc_pwd]
                enc_pass_list.append(llist)
        break
elif opt == 2:
else:
    
                
        
        


        
print("\n**********Thank You For Using Our App**********")
