student = {
    'id1': {'name': 'abc', 'age': 12, 'city': 'london', 'subject': ['phy', 'chem', 'bio']},
    'id2': {'name': 'abc', 'age': 12, 'city': 'london', 'subject': ['phy', 'chem', 'bio']},
    'id3': {'name': 'xyz', 'age': 12, 'city': 'london', 'subject': ['phy', 'chem', 'bio']},
    'id4': {'name': 'xyz', 'age': 12, 'city': 'london', 'subject': ['phy', 'chem', 'bio']},
    'id5': {'name': 'xyz', 'age': 12, 'city': 'jersey', 'subject': ['phy', 'chem', 'bio']},
    'id6': {'name': 'abc', 'age': 12, 'city': 'london', 'subject': ['phy', 'chem', 'bio']}
}

result = {}


for c, d in student.items():
    if d not in result.values():  
        result[c] = d

print(result)
