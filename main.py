import csv
from datetime import datetime

time=datetime.now()


def get_suspended_details(suspended_file):
    with open(suspended_file, 'r') as file:
        reader = csv.reader(file)
        suspended_details = []
        for row in reader:
            suspended_details.append(row)
        return suspended_details

def save_details_customer(filename, customer_details):
    with open(filename, 'a', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(customer_details)

def get_customer_details(customer_file):
    with open(customer_file, 'r') as file:
        reader = csv.reader(file)
        customer_details = []
        for row in reader:
            customer_details.append(row)
        return customer_details

def update_customer_details(customer_file, password, updated_details):
    customer_details = get_customer_details(customer_file)
    for customer in customer_details:
        if customer[3] == str(password):
            customer_details.remove(customer)
            customer_details.append(updated_details)
            break
    with open(customer_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(customer_details)

def staff_update_customer_details(customer_file, customer_id, updated_details):
    customer_details = get_customer_details(customer_file)
    for customer in customer_details:
        if customer[0] == str(customer_id):
            customer_details.remove(customer)
            customer_details.append(updated_details)
            break
    with open(customer_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(customer_details)

def update_customer_transfer_details(customer_file, customer_id, updated_details):
    customer_details = get_customer_details(customer_file)
    for customer in customer_details:
        if customer[0] == str(customer_id):
            customer_details.remove(customer)
            customer_details.append(updated_details)
            break
    with open(customer_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(customer_details)

def get_admin_details(admin_file):
    with open(admin_file, 'r') as file:
        reader = csv.reader(file)
        admin_details = []
        for row in reader:
            admin_details.append(row)
        return admin_details

def save_details_staff(filename, staff_details):
    with open(filename, 'a', newline='') as file:
        writer=csv.writer(file)
        writer.writerow(staff_details)


def log_details(log_file, context):
    file = open(log_file, 'a')
    file.write(f'{context}\n')

def get_staff_details(staff_file):
    with open(staff_file, 'r') as file:
        reader = csv.reader(file)
        staff_details = []
        for row in reader:
            staff_details.append(row)
        return staff_details

shift=4

def new_user_functionalities():
    choice=input('Welcome, Enter 1 to create account')
    if choice=='1':
        customer_file = 'customer_details.csv'
        log_file = 'bank_log.txt'
        suspended_file = 'suspended.csv'
        customer_details = get_customer_details(customer_file)
        suspended_details = get_suspended_details(suspended_file)
        customer_id = (len(customer_details) + len(suspended_details)) + 1
        name = input("Enter your name: ")
        account_type = input("Enter your Account type ")
        balance = 0
        password = input("Enter your account password ")
        customer_details = [customer_id, name, balance,account_type, password]
        save_details_customer(customer_file, customer_details)
        print("Customer account created successfully.")
        log = f'{name} created a customer account at {time}'
        log_details(log_file, log)


def customers_functions():

    customer_file = 'customer_details.csv'
    log_file='bank_log.txt'
    suspended_file='suspended.csv'
    login_password = input('please login by Inputing your password password')
    customers_programmes=True
    while customers_programmes:
        print("\nPlease select an option:")
        print("1. Withdraw money")
        print("2. Transfer money")
        print("3. Check balance")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice =='1':
            amount=int(input('Enter the amount you want to withdraw'))
            customer_details = get_customer_details(customer_file)
            for customer in customer_details:
                if customer[3] == login_password:
                    customer_balance = customer[2]
                    customer_balance = float(customer_balance)
                    if customer_balance >= amount:
                        customer_balance -= amount
                        customer[2] = customer_balance
                        update_customer_details(customer_file,login_password, customer)
                        print('withdrawal successful balance:',customer_balance)
                        log=f'{customer[1]} withdraw {amount} at {time}'
                        log_details(log_file,log)

        elif choice=='2':
            amount = int(input('Enter the amount you want to transfer'))
            sender_password = login_password
            recipient_id = input('Enter the Bank ID of the recipient')
            sender_details = get_customer_details(customer_file)
            receipient_details = get_customer_details(customer_file)
            for customer in sender_details:
                if customer[3] == sender_password:
                    balance = float(customer[2])
                    print()
                    if balance >= amount:
                        balance -= amount
                        customer[2] = balance
                        update_customer_details(customer_file, sender_password, customer)
                        for recipient in receipient_details:
                            if recipient[0] == str(recipient_id):
                                balance = recipient[2]
                                balance = float(balance)
                                balance += amount
                                recipient[2] = balance
                                update_customer_transfer_details(customer_file, recipient_id, recipient)
                                print('Transfer successful, your new account balance', customer[2])
                                log = f'{customer[1]} transfer {amount} to {recipient[1]} at {time}'
                                log_details(log_file, log)

        elif choice =='3':
            customer_details = get_customer_details(customer_file)
            for customer in customer_details:
                if customer[3] == login_password:
                    print('Your account balance is',customer[2])
                    log = f'{customer[1]} checked his balance at {time}'
                    log_details(log_file, log)
        elif choice == '4':
            break

def staff_function():
    log_file = 'bank_log.txt'
    staff_file='staff_details.csv'
    customer_file='customer_details.csv'
    staff_password = input('please login by Inputing login your password')
    staff_function=True
    while staff_function:
        print("\nPlease select an option:")
        print("1. Withdraw for customer")
        print("2. Deposit for customer")
        print("3. Transfer for customer")
        print("4. Check customers balance")
        print("5. Edit your password")
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer_id = input('Enter the customers ID')
            amount = int(input('Enter the amount the customer wants to withdraw'))
            customer_details = get_customer_details(customer_file)
            staff_details = get_customer_details(staff_file)
            for staff in staff_details:
                if staff_password == staff[2]:
                    staffs=staff
                    for customer in customer_details:
                        if customer[0] == str(customer_id):
                            customer_balance = customer[2]
                            customer_balance = float(customer_balance)
                            if customer_balance >= amount:
                                customer_balance -= amount
                                customer[2] = customer_balance
                                staff_update_customer_details(customer_file, customer_id, customer)
                                print(f"{amount} was withdraw from {customer[1]}'s account his/her new account balance {customer_balance}")
                                log = f"{amount} was withdraw from {customer[1]}'s account by staff {staffs[1]} at {time}"
                                log_details(log_file, log)
                            else:
                                print('Insufficient fund')


        elif choice == '2':
            customer_id = input('Enter the customers ID')
            amount = int(input('Enter the amount the customer wants to deposit'))
            staff_details = get_customer_details(staff_file)
            customer_details = get_customer_details(customer_file)
            for staff in staff_details:
                if staff[2] == staff_password:
                    staffs=staff
                    for customer in customer_details:
                        if customer[0] == str(customer_id):
                            balance = float(customer[2])
                            if amount > 0:
                                customer[2] = balance + amount
                                staff_update_customer_details(customer_file, customer_id, customer)
                                print(f"{amount} was deposited to {customer[1]}'s account his/her new account balance {customer[2]}")
                                log = f"{amount} was deposited to {customer[1]}'s account by staff {staffs[1]} at {time}"
                                log_details(log_file, log)

        elif choice == '3':
            sender_id = input('Enter the customers ID')
            recipient_id = input('Enter the recievers ID')
            amount = int(input('Enter the amount the customer wants to transfer'))
            staff_details = get_customer_details(staff_file)
            sender_details = get_customer_details(customer_file)
            receipient_details = get_customer_details(customer_file)
            for staff in staff_details:
                if staff[2] == staff_password:
                    staffs=staff
                    for customer in sender_details:
                        if customer[0] == str(sender_id):
                            balance = float(customer[2])
                            if balance >= amount:
                                balance -= amount
                                customer[2] = balance
                                update_customer_transfer_details(customer_file, sender_id, customer)
                                for recipient in receipient_details:
                                    if recipient[0] == str(recipient_id):
                                        balance = recipient[2]
                                        balance = float(balance)
                                        balance += amount
                                        recipient[2] = balance
                                        update_customer_transfer_details(customer_file, recipient_id, recipient)
                                        print(f'{customer[1]} has sent {amount} to {recipient[1]}')
                                        log=f'{customer[1]} has sent {amount} to {recipient[1]}, by staff {staffs[1]} at {time}'
                                        log_details(log_file, log)

        elif choice == '4':
            customer_id = input('Enter customers ID')
            staff_details=get_staff_details(staff_file)
            customer_details = get_customer_details(customer_file)
            for staff in staff_details:
                if staff[2]==staff_password:
                    staffs=staff
                    for customer in customer_details:
                        if customer[0] == str(customer_id):
                            print(f' {customer[1]} account balance is', customer[2])
                            log = f'{customer[1]} checked his account balance, by staff {staffs[1]} at {time}'
                            log_details(log_file, log)

        elif choice == '5':
            new_password=input("Enter new password")
            staff=get_staff_details(staff_file)
            for my_staff in staff:
                if my_staff[2]==staff_password:
                    staff_index = staff.index(my_staff)
                    staff[staff_index][2]=new_password
                    with open(staff_file, 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerows(staff)
                        print('Password changed succesfully')
                        log=f'{my_staff[1]} changed his password at {time}'
                        log_details(log_file, log)
        elif choice == '6':
            break

#admin function
def admin_function():
    admin_function=True
    admin_file='admin_details.csv'
    staff_file='staff_details.csv'
    suspended_file='suspended.csv'
    customer_file='customer_details.csv'
    log_file='bank_log.txt'
    admin_password=input('Enter admin password')
    while admin_function:
        print("\nPlease select an option:")
        print("1. Create staff Account")
        print("2. View Bank customers")
        print("3. View bank staffs")
        print("4. suspend a bank staffs account")
        print("5. Activate a suspended account")
        print("6. View Bank logs")
        print("7. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            admin=get_admin_details(admin_file)
            if admin[0][1]==admin_password:
                staff_details = get_staff_details(staff_file)
                suspended_details=get_suspended_details(suspended_file)
                try:
                    staff_id = (len(staff_details) + len(suspended_details)) + 1
                except TypeError:
                    staff_id= 1
                name = input("Enter staff name: ")
                password = input("Enter staff password ")
                staff_details = [staff_id, name, password]
                save_details_staff(staff_file, staff_details)
                print("Staff account created successfully.")

        elif choice == '2':
            admin=get_admin_details(admin_file)
            if admin[0][1] == password:
                customer=get_customer_details(customer_file)
                print('number----account name----account balance')
                for i in range(len(customer)):

                    print(f'{customer[i][0]}-----------{customer[i][1]}----------{customer[i][2]}')
                    log = f'Admin viewed customers at {time}'
                    log_details(log_file, log)
        elif choice == '3':
            admin = get_admin_details(admin_file)

            staff = get_staff_details(staff_file)
            if len(staff)==0:
                print('No active staff in the database')
            else:
                print('number------staff name')
                for i in range(len(staff)):
                    print(f'{staff[i][0]}-----------{staff[i][1]}')
                    log = f'Admin viewed staffs at {time}'
                    log_details(log_file, log)
        elif choice == '4':
            staff_id=input('Enter the staff id for the staff you want to suspended ')
            staff=get_staff_details(staff_file)
            for staffs in staff:
                if staffs[0]==staff_id:
                    to_be_suspended=staffs
                    index1=staff.index(to_be_suspended)
                    with open('staff_details.csv', mode='r+') as staff_file, open('suspended.csv', mode='a',newline='') as suspended_file:
                        staff_reader = csv.reader(staff_file)
                        suspended_writer = csv.writer(suspended_file)
                        for row in staff_reader:
                            if row == to_be_suspended:
                                suspended_writer.writerow(row)
                                with open('staff_details.csv', 'r') as input_file:
                                    reader = csv.reader(input_file)
                                    rows = list(reader)
                                del rows[index1]
                                with open('staff_details.csv', 'w', newline='') as output_file:
                                    writer = csv.writer(output_file)
                                    writer.writerows(rows)
                                    print(f' staff, {to_be_suspended[1]} has been suspended')
                                    log = f'Admin suspended,staff {to_be_suspended[1]} at {time}'
                                    log_details(log_file, log)
                else:
                    print('invalid staff ID')
        elif choice=='5':
            staff_id = input('Enter the staff id for the staff you want to Re-activate ')
            suspended = get_suspended_details(suspended_file)
            print(suspended)
            for staffs in suspended:
                if staffs[0] == staff_id:
                    to_be_activated = staffs
                    print(to_be_activated)
                    index1 = suspended.index(to_be_activated)
                    with open('staff_details.csv', mode='a') as staff_file, open('suspended.csv', mode='r',newline='') as suspended_file:
                        suspended_reader = csv.reader(suspended_file)
                        staff_writer = csv.writer(staff_file)
                        for row in suspended_reader:
                            if row == to_be_activated:
                                staff_writer.writerow(row)
                                with open('suspended.csv', 'r') as input_file:
                                    reader = csv.reader(input_file)
                                    rows = list(reader)
                                del rows[index1]
                                with open('suspended.csv', 'w', newline='') as output_file:
                                    writer = csv.writer(output_file)
                                    writer.writerows(rows)
                                print(f'staff {to_be_activated[1]} has been reactivated ')
                                log = f'Admin reactivate, {to_be_activated[1]} at {time}'
                                log_details(log_file, log)

        elif choice == '6':
            with open(log_file, 'r') as file:
                contents = file.read()
                print(contents)
        elif choice == '7':
            break





print("\nPlease select an option:")
print("1. IF YOU ARE NEW CUSTOMER")
print("2. IF YOU ARE CUSTOMER")
print("3. IF YOU ARE STAFF")
print("4. IF YOU ARE THE ADMIN")

choice = input("Enter your choice: ")
if choice=='1':
    new_user_functionalities()
if choice=='2':
    customers_functions()
elif choice == '3':
    staff_function()
elif choice == '4':
    admin_function()







