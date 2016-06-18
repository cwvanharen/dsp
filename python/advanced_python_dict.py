import csv
from collections import defaultdict
    
def read_data(filename):
    """Open csv and return rows as nested lists."""
    lists = []
    with open(filename, 'rb') as csvfile:
        faculty = csv.reader(csvfile)
        for row in faculty:
            lists.append(row)
    return lists
   
def q6_dict(lists):
    """Return dictionary with last names as keys"""
    d = defaultdict(list)
    for x in lists[1:]:
        lastname = x[0].split()[-1]
        d[lastname].append(x[1:])
    return d

def q7_dict(lists):
    """Return dictionary with name tuple as key"""
    d = defaultdict()
    for x in lists[1:]:
        a = x[0].split()
        last = a[-1]
        rest = ' '.join(a[:-1])
        name = rest, last
        d[name] = (x[1:])
    return d
    
def q8_dict(q7):
    """Return key, value pairs alphabetized by last name"""
    alist = []
    for x in sorted(q7.items(), key=lambda x: x[0][-1]):
        alist.append(x)
    return alist

filename = 'faculty.csv'
lists = read_data(filename)

# Q6
faculty_dict = q6_dict(lists)
#print faculty_dict

# Q7
professor_dict = q7_dict(lists)
#print professor_dict

# Q8
alpha_list = q8_dict(professor_dict)
#print alpha_list
