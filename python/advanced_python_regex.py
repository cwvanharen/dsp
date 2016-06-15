import csv
import re
from collections import Counter


def read_data(filename):
    """Open csv and return rows as nested lists."""
    lists = []
    with open(filename, 'rb') as csvfile:
        faculty = csv.reader(csvfile)
        for row in faculty:
            lists.append(row)
    return lists

def get_elem(lists, index):
    """Return a list of all the different elements at position 'index'"""
    elements = []
    for x in lists[1:]:
        elements.append(x[index])
    return elements
    
def parse_deg(degrees):
    """Give list consistent spacing"""
    return (' '.join(degrees)).split()
    
def clean(data):
    """Return a cleaned list."""
    clean_list = []
    for item in data:
        if item != '0':
            clean_list.append(re.sub('[.]', '', item))
    return clean_list
    
def count(data):
    """Count repeats in list and return dictionary with element count"""
    freq_dict = Counter(data)
    count = len(freq_dict)
    return freq_dict, count
    
def email_machete(emails):
    """Return list of just the domains"""
    domains = []
    for x in emails:
        cleave = x.find('@')
        domains.append(x[cleave+1:])
    return domains


filename = 'faculty.csv'
lists = read_data(filename)

# Q1
deg_list = get_elem(lists, 1)
parsed_list = parse_deg(deg_list)
cleaned = clean(parsed_list)
q1 = count(cleaned)
print 'Q1: ', q1

# Q2
# To do: deal with "Assistant Professor is Biostatics"
title_list = get_elem(lists, 2)
q2 = count(title_list)
print 'Q2: ', q2

# Q3
email_list = get_elem(lists, 3)
print 'Email list: ', email_list
domains = email_machete(email_list)
q3 = count(domains)
print 'Q3: ', q3[0].keys()


