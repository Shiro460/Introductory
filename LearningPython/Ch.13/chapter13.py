'''
＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
        第13章　whileループとforループ
＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
'''
#import packages
import random

#13.1.2 whileステートメントの例
#while 1:
#    print('Type Ctrl-C to stop me!')

x = 'spam'
while x:
    print(x)
    x = x[1:] #xから１文字目を取り除く

a = 0
b = 10
while a < b: #カウンタループの例
    print(a)
    a += 1 #aに１加える

#13.2.2 break、continue、pasステートメントやelseブロックを含むwhileループの使用例
print("＊＊＊＊13.2.2＊＊＊＊")
print("＊＊＊＊continue＊＊＊＊")
x = 10
while x >= 0:
    x -= 1
    if x % 2 != 0: #偶数ならば出力
        continue
    print(x)

'''
print("＊＊＊＊break＊＊＊＊")
while 1:
    name = input('Enter name: ')
    if name == 'stop':
        break
    age = input("Enter age: ")
    print('Hello', name, '=>', int(age)**2)
'''

print("＊＊＊＊else＊＊＊＊")
y = random.randint(-5, 5)
print(y)
x = y / 2
while x > 1:
    if y % x == 0:
        print(y, "has factor", x)
        break   #elseブロックは実行しない
    x -= 1
else:   #breakが実行されなければelseブロックを実行
    print(y, "is prime")

#13.3.2 forループの使用例
for x in ("spam", "eggs", "ham"):
    print(x)

sum = 0
for x in (1, 2, 3, 4):
    sum += x
print(sum)

prod = 1
for item in (1, 2, 3, 4):
    prod *= item
print(prod)

S = "lumberjack"
T = ("and", "I'm", "okay")

for x in S: #文字列のfor文
    print(x)

for x in T: #タプルのfor文
    print(x)

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)

items = ["aaa", 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    for item in items:
        if item==key:
            print(key, "was found")
            break
    else:
        print(key, "not found")

for key in tests:
    if key in items: #要素の一致確認
        print(key, "was found")
    else: #一致していなかった場合の処理
        print(key, "not found")

seq1 = "spam"
seq2 = "scam"

res = ["hogehoge", "foo", "", "bar"]

for x in seq1:
    if x in seq2:
        res.append(x)

print(res)

#13.4 反復処理
for x in [1, 2, 3, 4]:
    print(x**2)

for x in (1, 2, 3, 4):
    print(x**3)

for x in 'spam':
    print(x*2)

#13.4.1 ファイルを対象とした反復処理
f = open('test.txt')
'''
print(f.readline())
print(f.readline())
'''

for line in f:
    print(line)

def rangeForRoup(x):
    for x in range(5):
        print(x, 'Pythons')
        x += 1

rangeForRoup(1)

L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 1
    i += 1
    #print(i)

print(L)






