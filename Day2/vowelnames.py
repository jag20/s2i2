import re

def find_vowel_names(input_list):
    """
    Given an iterable, return number of lines that
    match "name,gender,count", where name starts and ends
    with a vowel. 
    """    
    vowels = re.compile(r"^[aeiouAEIOU][a-zA-Z]*[aeiouAEIOU],[FM],\d+$")
    vowel_names = []
    for line in input_list:
        line = line.strip()
        result = vowels.search(line)
        if result:
            vowel_names.append(line) 
    return len(vowel_names)
  
