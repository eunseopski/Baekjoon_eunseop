import sys
input = sys.stdin.readline

save = []
stan = ["(", "[", ")", "]"]

while True:
    S = input().rstrip()
    save = []

    if S == ".":
        break

    for s in S:
        if s in stan[:2]:
            save.append(s)
        elif s in stan[2:]:
            if save:
                if stan[stan.index(save[-1]) + 2] == s:
                    save.pop()
                else:
                    save.append(s)
                    break
            else:
                save.append(s)
                break

    if save:
        print("no")
    else:
        print("yes")
