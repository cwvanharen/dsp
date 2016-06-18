import csv


def read_data(filename):
    """Open csv and return rows as nested lists."""
    lists = []
    with open(filename, 'rb') as csvfile:
        faculty = csv.reader(csvfile)
        for row in faculty:
            lists.append(row)
    return lists

def get_elem(lists, index):
    """Return a list of all the elements at position 'index'"""
    elements = []
    for x in lists[1:]:
        elements.append(x[index])
    return elements
    
def write_data(data, email_file):
    """Write elements to file, one per line."""
    target = open(email_file, 'w')
    for email in data:
        target.write(email)
        target.write('\n')

filename = 'faculty.csv'
email_file = 'emails.csv'

lists = read_data(filename)
email_list = get_elem(lists, 3)
write_data(email_list, email_file)


