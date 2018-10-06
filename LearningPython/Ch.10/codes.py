#IF文
if 1 < 2:
    print("1 < 2")

if 1 != 2:
    print("1 is not equal 2")

'''
##stopと入力するまでは処理が終わらない
while True:
    reply = input("Enter text:")
    if reply == 'stop':
        break #stopと表示しない
    print(reply.upper())
'''

reply = '20'
print(int(reply) ** 2) #明示的な型変換

'''
文字列だったら数字を入れるようにリクエストを出す。
数字を入れてくれたら2乗して返却する。
while True:
    reply = input('Enter text:')
    if reply.isdecimal():
        print("Now, I calculate number^2:")
        reply = float(reply)
        print(reply ** 2)
        break
    else:
        print("you must enter a number")
print("Bye")
'''

'''
while True:
    reply = input('Enter text:')
    if reply == 'stop': #stopと入力されたらbreak
        break
    elif not reply.isdigit(): #数値以外を入力してきたらBadを10回返却し、処理は継続
        print('Bad! ' * 10)
        continue
    else:
        print(int(reply) ** 2) #数値で入力してきたら2乗して返却してbreak
        break
print('Bye')
'''

'''
#例外処理を使用した場合のコーディング
while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    try:
        num = int(reply) #try文でint型へと変換を試みる
    except:
        print('Bad! ' *10) #try文中で失敗した場合、Bad!と10回表示する
    else:
        print(int(reply) ** 2) #int型で問題なければ、2乗して出力する
        break
print('Bye')
'''




















