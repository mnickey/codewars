# Evil or Odious
# Python

def evil(n):
    status = (bin(n)[2:])
    if status.count('1') % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
