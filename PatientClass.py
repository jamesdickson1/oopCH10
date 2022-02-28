
class Patient:

    def __init__(self,iD,name,address,phone,veteran_status):
        self.__iD = iD
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__veteran_status = veteran_status
    
    def set_iD(self,iD):
        self.__iD = iD
    
    def set_name(self,name):
        self.__name = name
    
    def set_address(self,address):
        self.__address = address
    
    def set_phone(self,phone):
        self.__phone = phone
    
    def set_vet(self,veteran_status):
        self.__veteran_status = veteran_status
    
    def get_iD(self):
        return self.__iD
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phone(self):
        return self.__phone
    
    def get_veteran_status(self):
        return self.__veteran_status
    






