ans =input("Type the result of quiz please: ").split("x")

score =0
for n in ans:
    for j in range(0, len(n)+1):
        score =score + j

print(score)
