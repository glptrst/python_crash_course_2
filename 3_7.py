guests = ['Gennarino', 'Manara', 'Bill']

print(f"{guests[0]}, you are invited to my party.")
print(f"{guests[1]}, you are invited to my party.")
print(f"{guests[2]}, you are invited to my party.")

print(f"{guests[1]} can't make it...")

guests[1] = 'Delio'
print(f"{guests[1]}, you are invited to my party.")

print(f"There's a bigger table!")

guests.insert(0, 'Piermatteo')
guests.insert(2, 'Pierangela')
guests.append('Dionigi')

print(f"You are the invited: {guests[0]}, {guests[1]}, {guests[2]}, {guests[3]}, {guests[4]}, {guests[5]}")


print(f"I can invite only two people!")
guests.pop();
guests.pop();
guests.pop();
guests.pop();

print(f"the invited are {guests[0]} and {guests[1]}")

guests.remove('Piermatteo');
guests.remove('Gennarino');

print(guests)


