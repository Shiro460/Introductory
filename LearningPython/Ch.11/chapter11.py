# 11.1.4 拡張代入ステートメント
#加算
x = 1
x = x + 1
print(x)

y = 1
y += 1
print(y)

y += x
print(y)

#乗算
x *= 3
print(x)

print(type(x), "+", type(y))

#除算
'''
除算を実行すると、int型からfloat型に変わります。
'''
x /= 6
print(x)

y /= 2
print(y)

print(type(x), "+", type(y))

print("＊＊＊リストに要素を追加する場合＊＊＊")
#リストの拡張ステートメント
#可読性が高いコーディング
L = [1, 2]
L = L + [3]
print(L)

#処理スピードを重視したコーディング
L.append(4)
print(L)

print("＊＊＊複数の要素を追加する場合＊＊＊")
#複数の要素をリストに追加する場合
#可読性が高いコーディング
L2 = [1, 2]
L2 = L2 + [3]
print(L2)

#処理スピードを重視したコーディング
#（複数の時はextendコマンドを使うことに留意）
L2.extend([4, 5])
print(L2)

#または数値の拡張ステートメントを使う
L2 += [6, 7]
print(L2)

