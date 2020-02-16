def format_city(city_name, country_name, population=''):
    if population:
        result = f"{city_name.title()}, {country_name.title()} -- population {population}"
    else:
        result = f"{city_name.title()}, {country_name.title()}"
    return result
        
