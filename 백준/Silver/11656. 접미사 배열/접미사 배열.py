s = input()
lst = [s[i:] for i in range(len(s))]
for ele in sorted(lst):
    print(ele)