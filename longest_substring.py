# longest_substring.py
import time

def solution(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if len(set(s)) == len(s):
        return len(s)
    # res = list()
    # temp = list()
    # for w in s:
    #     if w not in temp:
    #         temp.append(w)
    #     else:
    #         res.append(temp)
    #         temp = list()
    #         temp.append(w)
    # res.append(temp)
    # print(res)
    # longest = list()
    # for n in res:
    #     if len(n) > len(longest) and set(n) != set(longest):
    #         longest = n
    # return len(longest)
    
    res = dict()
    ans = 0
    m = 0
    for n in range(0, len(s)):
        try:
            if res[s[n]]:
                m = max(res[s[n]], m)
        except KeyError:
            pass
        ans = max(ans, n-m+1)
        res[s[n]] = n+1
    return ans
    # if len(res) < 3:
    #     return len(res)
    # else:
    #     count = 0
    #     for k,v in res.items():
    #         if v > 0:
    #             count +=1
    #     return count
    

def main():
    tester = "abcabcbb"
    print(solution(tester))

    tester = "bbbbb"
    print(solution(tester))

    tester = "pwwkew"
    print(solution(tester))

    tester = " "
    print(solution(tester))

    tester = "c"
    print(solution(tester))

    tester = "au"
    print(solution(tester))

    tester = "dvdf"
    print(solution(tester))

    tester = "bwf"
    print(solution(tester))

    tester = "abcb"
    print(solution(tester))

start = time.time()
main()
print("{} seconds".format(time.time()-start))