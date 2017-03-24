# Customer object with limited QBO fields to simplify this sample
class Customer:
    def __init__(self, f_name, l_name, m_name, phone, email):
        self.GivenName = f_name
        self.MiddleName = m_name
        self.FamilyName = l_name
        self.PrimaryPhone = phone
        self.PrimaryEmailAddr = email

    def print_customer(self):
        print self.GivenName, self.MiddleName, self.FamilyName, self.PrimaryPhone, self.PrimaryEmailAddr
