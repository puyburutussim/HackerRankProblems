def alternatingCharacters(s):
  curr = s[0]
  dels = 0
  for i in range(1, len(s)):
    if s[i] == curr:
      dels += 1
    else:
      curr = s[i]
  return dels
