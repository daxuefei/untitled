ln_path = 'C:/Users/Administrator/Desktop/last_name.txt'
fn_path = 'C:/users/Administrator/Desktop/first_name.txt'

fn = []
ln1 = [] #单字名
ln2 = [] #双字名

with open(fn_path,'r') as f:
    for line in f.readlines():
        fn.append(line.split('\n')[0])

print(fn)
with open(ln_path,'r') as f:
    for line in f.readlines():
        if len(line.split('\n')[0]) == 1:
            ln1.append(line.split('\n')[0])
        else:
            ln2.append(line.split('\n')[0])

print(ln1)
print('='*70)#分割线
print(ln2)

import random
class FakeUser():
    def fake_name(self,one_word=False,tow_words=False):
        n = 0
        while n <= amount:
            if one_word:
                full_name = random.choice(fn) + random.choice(ln1)
            elif tow_words:
                full_name = random.choice(fn) + random.choice(ln2)
            else:
                full_name = random.choice(fn) + random.choice(ln1+ln2)

            yield(full_name)
            n+=1
    def fake_gender(self,amount=1):
        n=0
        while n <= amount:
            gender = random.choice(['男','女','未知'])
            yield(gender)
            n+=1




class SnsUsers(FakeUser):
    def get_followers(self,amount=1,few=True,a_lot=False):
        n=0
        while n <=amount:
            if few:
                followers = random.randrange(1,50)
            elif a_lot:
                followers = random.randrange(200,10000)
            yield followers
            n+=1
users_a = FakeUser()
users_b = SnsUsers()
for name in users_a.fake_name(30):
    print(name)
for name in users_a.fake_gender(30):
    print(gender)