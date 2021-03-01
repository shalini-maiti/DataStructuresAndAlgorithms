'''
Notes:

  1) Always check for early exit strategies for optimzation.
  2) DONT ranndomly initialise to 0. Especially when maintaining
  a running counter because sometimes it would have to be intialised
  to 1 when counting while replacing current elements.

'''

# 1 a)Is Unique: Implement an algorithm to
# determine if a string has all unique characters.
# b)What if you cannot use additional data structures?

# Input: asafopacb Output: False
# Input: asdfghjkl Output: True
# Check for spaces, commas, non-alphabets?
# If the string > total number in the alphabet, return false

# Early exit: If len(str) > total #alphabets

def is_unique(word):
  counter_map = set()
  for element in word:
    if element in counter_map:
      return False
    else:
      counter_map.add(element)

  return True

def is_unique_wout_ds(word):
  for elem1_ind in range(len(word) - 1):
    for elem2_ind in range(elem1_ind+1, len(word)):
      #print(elem1_ind, elem2_ind, word[elem1_ind], word[elem2_ind])
      if word[elem1_ind] == word[elem2_ind]:
        return False
  return True

def is_unique_wout_ds_faster(word):
  #binary sort
  #Counter?
  pass

# 2. Check Permutation: Given two strings, write
# a method to decide if one is a permutation
# of the other.
# Input : asdfgh, hgfdsa Output: True
# Input : asdfgl, plkijd Output: False
def check_permutation(str1, str2):
  if len(str1) != len(str2):
    return False
  str3 = ''.join(sorted(str1.replace(" ", "")))
  str4 = ''.join(sorted(str2.replace(" ", "")))

  return str3 == str4

# 3. URLify: Write a method to replace all spaces in
# a string with '%20'. You may assume that the
# string has sufficient space at the end to hold
# the additional characters, and that you are given
# the "true" length of the string.

def urlify(str1):
  return str1.replace(" ", "%20")

# 4. Palindrome Permutation: Given a string, write a function
# to check if it is a permutation of a palindrome.
# Remove al space?
# Input: 'qweqwe' Output: True ('qweewq')
# Inpu: 'asdlkj' Output: False
# Check if counter is %2==0 for all the characters,
# except for just 1 which can be an odd number
# Early exit? len(%2) !=0 exit. WRONG
# Either Sort or use Counter class.

def palindrome_permutation(str1):
  '''
  BAD EARLY EXIT. Practice with more examples in the beginning
  if len(str1)%2 != 0:
    return False
  '''
  str2 = sorted(str1.replace(" ", ""))
  curr_char = str2[0]
  curr_char_ind = 1
  num_of_odd_chars = 0
  # DONT randomly initialise to 0.
  # Especially when maintaining a running counter

  for ind in range(1, len(str2)):
    elem = str2[ind]
    if curr_char == elem:
      curr_char_ind += 1
    else:
      if curr_char_ind%2 != 0:
        if num_of_odd_chars > 1:
        #print(curr_char, ind, elem, curr_char_ind)
          return False
        else:
          num_of_odd_chars += 1
          curr_char_ind = 1 # Same init problem as above
          curr_char = elem
      else:
        curr_char_ind = 1 # Same init problem as above
        curr_char = elem

  return True

# One Away: There are three types of edits that can
# be performed on strings: insert a character,
# remove a character, or replace a character.
# Given two strings, write a function to check if
# they are one edit (or zero edits) away.
# Input (askl, asl) (alplsk, alplsj) (alplsk, alplza)
def one_edit_away(str1, str2):
  # if len(1) - len(2) > 1, exit
  # sort both strings
  # keep a counter of differences
  # intialize diff = len(1) - len(2)
  # Iterate through the string and if something is different
  # add to counter
  # if counter > 1,
  len1 = len(str1)
  len2 = len(str2)
  diff_counter = abs(len1 - len2)
  if diff_counter > 1:
    return False
  max_len = max(len1, len2)

  #sort_1 = sorted(str1.replace(" ", ""))
  #sort_2 = sorted(str2.replace(" ", ""))
  i = 0
  while diff_counter < 2:
    if i < len1 and i < len2:
      if str1[i] != str2[i]:
        diff_counter += 1
    i += 1
    return False
  return True


if __name__ == "__main__":
  word = "asdfghjkl"
  #print(is_unique(word))
  #print(is_unique_wout_ds(word))

  str1 = "asdf gh"
  str2 = "hgfdsa"
  str3 = "asdfgl"
  str4 = "plkijd"
  #print(check_permutation(str1, str2))
  #print(check_permutation(str3, str4))

  urli = "shalini maiti"
  #print(urlify(urli))

  palin1 = "qweqweqweqwep"
  palin2 = "palinpol"
  #print(palindrome_permutation(palin1))
  #print(palindrome_permutation(palin2))


  one_e_a1 = "askl"
  one_e_a2 = "asl"
  one_e_a3 = "alplsk"
  one_e_a4 = "alplsj"
  one_e_a5 = "alplsk"
  one_e_a6 = "alplza"

  print(one_edit_away(one_e_a1, one_e_a2))
  print(one_edit_away(one_e_a3, one_e_a4))
  print(one_edit_away(one_e_a5, one_e_a6))