# https://leetcode.com/problems/fruits-into-baskets-ii/?envType=daily-question&envId=2025-08-05
count = 0
for i in range(len(fruits)):
    for j in range(len(baskets)):
        if fruits[i]<=baskets[j]:
            count+=1
            baskets.pop(j)
            break
    print(baskets)
print(len(fruits)-count)