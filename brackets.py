def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    opens  = [ '(','{','[' ]
    closes = [ ')','}',']' ]

    if s[0] in closes:
      return False

    # openBracket = s[0]

    for char in s:
      if char in opens:
        openBracket = char
      else:
        if openBracket == '{' and char == '}':
          openBracket = ''
          continue
        elif openBracket == '(' and char == ')':
          openBracket = ''
          continue
        elif openBracket == '[' and char == ']':
          openBracket = ''
          continue
        else:
          return False

    return True

print(isValid('(){}}{'))
    