'''
public methods
'''

class Acount:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass 

s1 = Acount("1234","xyz@123")

print(s1.acc_no,s1.acc_pass) # in this case account password is the sencitive things so , out of the scope i dont need this value 's1.acc_pass' 


