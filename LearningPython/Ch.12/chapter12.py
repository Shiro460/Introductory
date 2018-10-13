'''
＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
              第12章　ifステートメント
＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
'''

#12.1.2 ifステートメントの例
if 1:
    print('true')

if not 1:
    print('true')
else:
    print('false')

#12.1.3 多分岐
x = 'killer rabbit'
if x == 'roger':
    print("how's jessica?")
elif x == 'bugs':
    print("what's up doc?")
else:
    print("Run away! Run away!")

