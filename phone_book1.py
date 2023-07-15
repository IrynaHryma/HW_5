from collections import UserDict

class Field:
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return self.value
    
    def __repr__(self) -> str:
        return str(self)

class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name:Name,phone:Phone = None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    
    def add_phone(self, phone:Phone):
        if phone.value not in (p.value for p in self.phones):
           self.phones.append(phone)
           return f"Phone {phone} added to contact {self.name}."
        return f"{phone} is in contact {self.name}."
    
    
    # def remove_phone(self, phone):
    #     self.phones.remove(phone)

    
    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate (self.phones):
            if old_phone.value == phone.value:
                self.phones[index] = new_phone
            return f"Old phone {old_phone} is changed to new phone {new_phone}."
        
        return f"{old_phone} is not present in contact {self.name}."

    
    def __str__(self) -> str:
        return f"{self.name}: {', '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data[str(record.name)] = record
        return f'Contact {record} add success.'
    
    
    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())
    
        

if __name__ == "__main__":
    
    ab = AddressBook()
    name = Name("Bill Gates")
    name.value = "Bill Gates"
    record = Record(name)
    phone1=Phone("+2617627334")
    phone1.value = "+2617627334"
    print (name.value)
    print(phone1.value)
    ab.add_record(record)
    record.add_phone(phone1)
    print(record)
    
    
    
    