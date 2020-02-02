rivers = {
    'nile': 'egypt',
    'piovego': 'italy',
    'ciane': 'italy'
}

for k, v in rivers.items():
    print(f"The {k.title()} runs through {v}")

for k in rivers.keys():
    print(k.title())

for v in rivers.values():
    print(v.title())
