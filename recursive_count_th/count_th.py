'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  count = 0
  if len(word) == 0:
    return 0

  def helper(word): 
    nonlocal count

    if len(word) == 1:
      return 

    if word[0:2] == 'th':
      count += 1
      helper(word[1:])
    else:
      helper(word[1:])
  
  helper(word)
  return count
