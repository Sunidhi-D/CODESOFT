class Contact:
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

    def __str__(self):
        return f"{self.name}-{self.phone}-{self.email}-{self.address}"
    

class ContactManager:
    def __init__(self):
        self.contacts=[]
    
    def add_contact(self,name,phone,email,address):
        new_contact=Contact(name,phone,email,address)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added succesfully.")

    def view_contact(self):
        if not self.contacts:
            print("No contact available.")
            return
        print("Contact List:")
        for contact in self.contacts:
            print(contact)


    def search_contact(self, search_term):
        found_contact=[contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if found_contact:
            print("Search Results: ")
            for contact in found_contact:
                print(contact)
            else:
                print("No contact found.")


    def update(self,name,new_phone=None,new_mail=None,new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone=new_phone
                if new_mail:
                    contact.email=new_mail
                if new_address:
                    contact.address=new_address
                print(f"Conatct '{name}' updated successfully.")
                return
        print(f"Contact '{name}' not found.")  


    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower()==name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")

def main():
    manager=ContactManager()

    while True:
        print("\n Contact Manager System")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice=input("Choose an option (1-6): ")

        if(choice=='1'):
            name=input("Enter name: ")
            phone=input("Enter phone number: ")
            email=input("Enter email: ")
            address=input("Enter Address: ")
            manager.add_contact(name,phone,email,address)

        elif choice=='2':
            manager.view_contact()

        elif choice=='3':
            search=input("Enter name or phone number to search contact: ")
            manager.search_contact(search)
        
        elif(choice=='4'):
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            new_address = input("Enter new address (leave blank to keep current): ")
            manager.update_contact(name, new_phone if new_phone else None, new_email if new_email else None, new_address if new_address else None)
        
        elif(choice =='5'):
            name=input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)

        elif(choice=='6'):
            print("Exiting the program.")
            break

        else:
            print("Enter a valid choice..")

if __name__ == "__main__":
    main()