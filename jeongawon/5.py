print("2~50사이의 소수:")

for n in range ( 2, 51 ) : # 2부터 50까지 검사
    for x in range(2, n):  # 2부터 n-1까지 나누기
        if n % x == 0: 
            break          # 약수일 때 -> 소수가 아님
    else:
        print(n , " " ) # break없이 끝나면 -> 소수
       
            

