# Author: Jonathan Nunez
# Date: 9/19/24
# Purpose: Module for managing Tuffy Titan contacts

def add_contact(contacts, id, first_name, last_name):
    if id in contacts:
        return "error"
    contacts[id] = [first_name, last_name]
    return {id: contacts[id]}

def modify_contact(contacts, id, first_name, last_name):
    if id not in contacts:
        return "error"
    contacts[id] = [first_name, last_name]
    return {id: contacts[id]}

def delete_contact(contacts, id):
    if id not in contacts:
        return "error"
    removed_contact = {id: contacts[id]}
    del contacts[id]
    return removed_contact

def sort_contacts(contacts):
    sorted_contacts = dict(sorted(contacts.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
    return sorted_contacts

def find_contact(c, find):
    result = {}
    if find.isdigit() and int(find) in c:
        result[int(find)] = c[int(find)]
    else:
        for id, names in c.items():
            if find.lower() in (name.lower() for name in names):
                result[id] = names
    return result

