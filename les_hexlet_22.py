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
#Решение учителя
def filter_string(text, char):
    result = ''
    lowered_char = char.lower()
    for current_char in text:
        if current_char.lower() != lowered_char:
            result += current_char
    return result.strip().replace('  ', ' ')
