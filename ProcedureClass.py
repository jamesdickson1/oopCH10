
class Procedure:

    def __init__(self,proname,date,pracname,charge,iD):
        self.__proname = proname
        self.__date = date
        self.__pracname = pracname
        self.__charge = charge
        self.__iD = iD
    
    def set_proname(self,proname):
        self.__proname = proname
    
    def set_date(self,date):
        self.__date = date
    
    def set_pracname(self,pracname):
        self.__pracname = pracname
    
    def set_charge(self,charge):
        self.__charge = charge

    def set_iD(self,iD):
        self.__iD = iD
    
    def get_proname(self):
        return self.__proname

    def get_date(self):
        return self.__date

    def get_pracname(self):
        return self.__pracname

    def get_charge(self):
        return self.__charge

    def get_iD(self):
        return self.__iD    