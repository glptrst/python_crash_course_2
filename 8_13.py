def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Jane', 'Baffelli',
                             location='Barcelona',
                             field='Philosophy',
                             uni='UB')
print(user_profile)
