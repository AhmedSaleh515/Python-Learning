# Email validator (string splitting)
def extract_username(email):
    if '@' in email:
        liist = email.split('@')
        print(f'username: {liist[0]}\ndomain: {liist[1]}')
extract_username('hamada@gmail.com')
#______________________________#
#
#Top 3 winners (list slicing & sorting)
scores = [45, 88, 12, 92, 55, 76, 99, 10]
scores.sort()
top_three = scores[-3:]
top_three = top_three[::-1]
print(f"the first place got {top_three[0]}")
print(f"the second place got {top_three[1]}")
print(f"the third place got {top_three[2]}")
#______________________________#
#
#sentence flipper (lists and strings)
def sentence_flipper(sentence):
    sentence = sentence.split()
    sentence = sentence[::-1]
    print(" ".join(sentence))
sentence_flipper('hi there')