### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  def check_for_ace(self, card):
  # `if` statements evaluate an expression as their condition, in python assignments are statements and not expressions so they're not valid in the condition of an `if` statement.  It looks like this should use `==` not `=` to test for equality
    if card.value = 1:
      return True
    # missing `:` after else
    else
      return False
   
  # `dif` should be `def`
  # missing comma between `card1` and `card2`
  dif highest_card(self, card1 card2):
  # incorrect indentation on next four lines: all should be indented one more level
  if card1.value > card2.value:
    # there's no such variable defined in scope as `card`, `card1` would make sense in context
    return card
  else:
    return card2
  

# although `total` is a valid expression and so is a valid statement, python won't create the variable without an assignment to it.  In context, this should be something like `total = 0` to create the local variable and initialise it
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    # total is storing an integer, but python doesn't allow the catenation of strings and integers, so the integer would need to be explicitly converted to a string with `str(...)` for this to work
    return "You have a total of" + total
  
```
