#reverse word 
def reverse_word(word):
    if not isinstance(word, str):
        return None

    return word[::-1]        
    #words = word.split()
    #reversed_words = words[::-1]

    #return " ".join(reversed_words)

#count vowels in a string
def count_vowels(s):    
    if not isinstance(s, str):
        return None

    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

#palindrome checker     
def is_palindrome(s):
    if not isinstance(s, str):
        return None
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]