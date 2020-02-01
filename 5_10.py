current_users = ['gp', 'pg', 'Admin', 'suca', 'casu']

new_usernames = ['Matt', 'gp', 'tamm', 'Suca', 'suh']

current_users_lower_case = []
for u in current_users:
    current_users_lower_case.append(u.lower())
    
for nu in new_usernames:
    if nu.lower() in current_users_lower_case:
        print(f"{nu} already in use!")
    else:
        print(f"Username '{nu}' available!")
    
