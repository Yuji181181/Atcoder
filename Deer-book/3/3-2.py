# while文を使った場合

H, A = map(int, input().split())
counter = 0
while H > 0:  # Hが0より大きい間、HからAを引き続け、カウンターを1増やす
    H -= A
    counter += 1
print(counter)
