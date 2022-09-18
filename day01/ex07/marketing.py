import sys


def format_email(contact_list, del_list):
    new_list = [x for x in contact_list if x not in del_list]
    return new_list


def del_duplicate(clients, participants, recipients):

    contact_list = clients + participants + recipients
    contact_list = list(set(contact_list))
    return contact_list


def marketing():
    if len(sys.argv) != 2 or (
            sys.argv[1] != 'call_center' and sys.argv[1] != 'potential_clients' and sys.argv[1] != 'loyalty_program'):
        raise Exception("Error argument")
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com',
               'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    new_list = del_duplicate(clients, participants, recipients)

    if sys.argv[1] == 'call_center':
        print(format_email(new_list, recipients))
    if sys.argv[1] == 'potential_clients':
        print(format_email(new_list, clients))
    if sys.argv[1] == 'loyalty_program':
        print(format_email(new_list, participants))


if __name__ == '__main__':
    marketing()

