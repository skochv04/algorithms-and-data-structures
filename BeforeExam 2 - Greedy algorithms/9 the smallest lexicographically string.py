# We are given a string with some letters that are repeated in it. Find algorithm that will remove from
# string duplicates so that the resulting string will be lexicographically the smallest.
# Example: cbacdcbc, the answer is acdb

def smallest(s):
    CMT = [0 for _ in range(26)]
    taken = [False for _ in range(26)]
    stack = []
    for letter in s:
        CMT[ord(letter) - 97] += 1
    for letter in s:
        l = ord(letter) - 97
        if not taken[l]:
            if len(stack) != 0 and l < stack[-1] and CMT[stack[-1]] > 0:
                taken[stack[-1]] = False
                stack.pop()
            stack.append(l)
            CMT[l] -= 1
            taken[l] = True
    new_string = ""
    for el in stack:
        new_string += chr(97 + el)
    return new_string

s = "cbacdcbc"
print(smallest(s))