
alphabets = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

print('Hey welcome!!!😊😊')

name1 = input('ENTER YOUR NAME :\n').lower()
name1 = name1.replace(" ","")
name2 = input('ENTER THEIR NAME :\n').lower()
name2 = name2.replace(" ","")

name1_score = 0
name2_score = 0


def calc_name1_score(name,alphabets):
    global name1_score
    for letter in name:
        value = alphabets[letter]
        name1_score = name1_score + value

def calc_name2_score(name,alphabets):
    global name2_score
    for letter in name:
        value = alphabets[letter]
        name2_score = name2_score + value

calc_name1_score(name1,alphabets)

calc_name2_score(name2,alphabets)

score1 = name1_score + name2_score

if score1 == 11:
    print('your love score is 11 .')
    print('A love score of 11 suggests a deep, spiritual connection between two individuals. It is a highly intuitive and sensitive number, associated with spiritual enlightenment, mysticism, and creativity. Individuals with a love score of 11 are often very emotionally sensitive and empathetic, and they may feel an intense connection with their partner that goes beyond the physical realm.')
    

elif score1 == 22:
    print('your love score is 22 .')
    print('A love score of 22 is associated with great potential for success and achievement in the material world. It is often considered the "Master Builder" number, representing the ability to manifest ones dreams and create something truly remarkable. Individuals with a love score of 22 are often highly ambitious and driven, and they may be focused on building a life of financial security and material success with their partner.')

final_score1 = 0

def add_score(digit_score):
    global final_score1
    value_len = len(str(digit_score))
    for i in range(value_len):
        ad_val = str(digit_score)[i:i+1]
        final_score1 = final_score1 + int(ad_val)

add_score(score1)

final_score2 = 0

def add_score1(score):
    global final_score2
    value_len = len(str(score))
    for i in range(value_len):
        ad_val = str(score)[i:i+1]
        final_score2 = final_score2 + int(ad_val)

is_len = len(str(final_score1))

if is_len > 1:
    add_score1(final_score1)


real =0
if len(str(final_score1))>1:
    real=final_score2
else:
    real=final_score1
        
if len(str(real)) > 1:
    real = 1

if real == 1:
    print(f'your love score is {real} .')
    print(' Independence, individuality, leadership, self-confidence, and self-reliance. A love score of 1 suggests a relationship that is driven by strong personalities who are not afraid to take charge and lead.')
    print('a love score of 1 may indicate a potential for conflict or power struggles, as both individuals may be highly independent and have strong personalities. Similarly, a love score of 5 may suggest a relationship that is prone to change and unpredictability, which may be exciting but could also be destabilizing for some individuals.')
elif real == 2:
    print(f'your love score is {real} .')
    print(' Partnership, balance, harmony, diplomacy, and sensitivity. A love score of 2 suggests a relationship that is based on mutual understanding and respect, and where both partners value cooperation and compromise.')
elif real == 3:
    print(f'your love score is {real} .')
    print('Creativity, self-expression, optimism, and socialization. A love score of 3 suggests a relationship that is likely to be fun, lively, and full of laughter and creative expression.')
elif real == 4:
    print(f'your love score is {real} .')
    print('Stability, structure, organization, and practicality. A love score of 4 suggests a relationship that is likely to be grounded, reliable, and focused on building a stable foundation for the future.')
elif real == 5:
    print(f'your love score is {real} .')
    print('Freedom, change, adaptability, and exploration. A love score of 5 suggests a relationship that is likely to be exciting, unpredictable, and full of adventure and new experiences.')
elif real == 6:
    print(f'your love score is {real} .')
    print('Love, harmony, family, responsibility, and nurturing. A love score of 6 suggests a relationship that is likely to be warm, loving, and focused on building a strong family unit.')
elif real == 7:
    print(f'your love score is {real} .')
    print('Spirituality, introspection, intuition, and mysticism. A love score of 7 suggests a relationship that is likely to be deep, meaningful, and focused on personal growth and spiritual development.')
elif real == 8:
    print(f'your love score is {real} .')
    print('Ambition, power, success, and material abundance. A love score of 8 suggests a relationship that is likely to be focused on achieving financial stability and material success.')
elif real == 9:
    print(f'your love score is {real} .')
    print('Compassion, generosity, forgiveness, and humanitarianism. A love score of 9 suggests a relationship that is likely to be focused on helping others and making a positive impact in the world.')

print()
print(' The true meaning of a love score will depend on the individuals involved and the unique dynamics of their relationship.')
print('💝💝💝💝💝')




