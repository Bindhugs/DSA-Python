#BRUTE FORCE PATTERN MATCHING
def brute_force_match(s,p):
    n = len(s)
    m = len(p)
    for i in range(n-m+1):
        match = True
        for j in range(m):
            if s[i+j] != p[j]:
                match = False
                break
        if match:
            print("Pattern found at index: ",i)

s = 'hello world'
p = 'world'

brute_force_match(s,p)