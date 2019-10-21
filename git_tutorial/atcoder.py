n,m = map(int,input().split(" "))
s = input()
friends_scissors = s.count("C")
friends_paper = s.count("P")
friends_rock = s.count("G")
tens = m // 10
if (m - tens*10) % 2 == 1:
    fives = (m - tens*10) // 5
    twos = (m - tens*10 - fives*5) // 2
else:
    twos = (m - tens*10 - fives*5) // 2
max_count = 0
for i in range(tens + 1):
    scissors = 5 * i + twos
    paper = 2 * (tens - i) + fives
    rock = n - scissors - paper
    if rock < 0:
        continue
    win_count = n - (abs(friends_scissors - rock) + abs(friends_paper - scissors) + abs(friends_rock - paper))//2
    if max_count < win_count:
        max_count = win_count
    print(rock*0+scissors*2+paper*5)
    print(tens,fives,twos)
