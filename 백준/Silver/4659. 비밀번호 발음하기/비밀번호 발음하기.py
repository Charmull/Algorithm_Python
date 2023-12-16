import sys

input = sys.stdin.readline
vowel = ['a', 'e', 'i', 'o', 'u']

def check(pw):
    ch1 = False
    prev = ''
    prev_vowel = pw[0] in vowel
    ch2_num = 0
    for i in range(len(pw)):
        if pw[i] in vowel:
            ch1 = True
            if prev_vowel:
                ch2_num += 1
            else:
                ch2_num = 1
            prev_vowel = True
        else:
            if not prev_vowel:
                ch2_num += 1
            else:
                ch2_num = 1
            prev_vowel = False
        if ch2_num >= 3:
            return False
        if prev == pw[i] and pw[i] not in ['e', 'o']:
            return False
        prev = pw[i]
    return True if ch1 else False

while True:
    pw = input().strip()
    if pw == 'end':
        break
    print(f'<{pw}> is acceptable.' if check(pw) else f'<{pw}> is not acceptable.')