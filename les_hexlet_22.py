def filter_string(my_string, element):
    result = ''
    for char in my_string:
      if char.lower() != element.lower():
        result = result + char
      else:
        result = result
    result = result.strip()
    while '  ' in result:
      result = result.replace('  ', ' ')
    return result
