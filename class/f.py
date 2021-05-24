class Phone:
    name = 'Anna' #public variable
    _skolko_raz_telephone_vkl = 0 #protected
    def call(self):
        print("Ding-Dong")
    def _vkl(self): #protected
        self._skolko_raz_telephone_vkl+=1
        print('Telephone vkl: ', self._skolko_raz_telephone_vkl)

a = Phone()
a.call()
print("Eto telephone ", a.name)
