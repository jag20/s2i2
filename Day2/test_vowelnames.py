import vowelnames

def test_empty_list():
    result = vowelnames.find_vowel_names([])
    assert(result == 0 )

def test_one_name():
    #test a non-matching line
    result = vowelnames.find_vowel_names(["E8798mma,F,201"])
    assert(result == 0) 

#def test_two_name():
    #test two names

