with open('./learning_python.py') as py_file:
    py_file = py_file.read()

print(py_file)

with open('./learning_python.py') as py_file:
    s = []
    for l in py_file:
        s.append(l)

for l in s:
    print(l)
