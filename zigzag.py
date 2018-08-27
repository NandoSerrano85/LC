import time 
# simple solution is O(n^2)
# example:
#   "PAYPALISHIRING" 3
#   P   A   H   N
#   A P L S I I G
#   Y   I   R
def convert(s, numRows):
    if numRows == 1:
        return s
    elif numRows >= len(s):
        return s
    res = ""
    size = len(s)
    for i in range(0, numRows):
        hop = i
        shift =  True
        while hop < size:
            res += s[hop]
            if i == numRows-1:
                hop = 2 * (numRows-1) + hop 
                shift = False
            elif shift or i == 0:
                hop = 2 * (numRows-(1+i)) + hop 
                shift = False
            else:
                hop = 2 * i + hop
                shift = True

    return res




def main():
    tester = "PAYPALISHIRING"
    num = 3
    print("Your answer: {}".format(convert(tester, num)))
    print("correct: PAHNAPLSIIGYIR")

    num = 4
    print("Your answer: {}".format(convert(tester, num)))
    print("correct: PINALSIGYAHRPI")

    tester = "AB"
    num = 2
    print("Your answer: {}".format(convert(tester, num)))

    tester = "ABCD"
    num = 2
    print("Your answer: {}".format(convert(tester, num)))

    tester = "ABCD"
    num = 3
    print("Your answer: {}".format(convert(tester, num)))

    tester = "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."
    num = 10
    print("Your answer: {}".format(convert(tester, num)))

    tester = "svcpwdausevrqrsjstjwxffkaltvrbulyyaudcqvglowdggxbpvzwalxogufhotioteryvoeicbnljkoahnxibwwhqdrhwzxsfp"
    num = 10
    print("Your answer: {}".format(convert(tester, num)))

    tester = "ABCDE"
    num = 3
    print("Your answer: {}".format(convert(tester, num)))
    print("correct: AEBDC")

    tester = "ABCDE"
    num = 4
    print("Your answer: {}".format(convert(tester, num)))
    print("correct: ABCED")

start = time.time()
main()
print("{} seconds".format(time.time() - start))






# res = ""
#     sp = s
#     length = numRows + abs(numRows-2)
#     i = 0
#     hop = 0
#     back = 0
#     size = len(sp)
#     if len(s) <= (length) and numRows > 2:
#         while size != 0:
#             if res == "":
#                 res += sp[0]
#                 sp = sp[1:]
#             elif size == 1:
#                 res += sp[0]
#                 sp = sp[1:len(sp)-1]
#             else:
#                 res = res + sp[0] + sp[-1]
#                 sp = sp[1:len(sp)-1]

#             size = len(sp)
#     elif length == len(s)+1:
#         while size != 0:
#             if res == "":
#                 res += sp[0]
#                 sp = sp[1:]
#             elif size == 1:
#                 res += sp[0]
#                 sp = sp[1:len(sp)-1]
#             else:
#                 res = res + sp[0] + sp[-1]
#                 sp = sp[1:len(sp)-1]

#             size = len(sp)
#     else:
#         while i != numRows:
#             while hop <= size-1 :
#                 if i == 0 or hop == 0:
#                     res += sp[hop]
#                 elif i == (numRows-1):
#                     try:
#                         res += sp[hop]
#                     except IndexError:
#                         break
#                 elif abs(hop-back) < size:
#                     res += sp[hop-back]
#                     res += sp[hop]
#                 else:
#                     res += sp[hop]
#                 hop += length

#             if hop == size and len(s) != len(res) and i > 0 and abs(hop-back) < size:
#                 res += sp[hop-back]
                
#             i += 1
#             back = 2 ** i
#             hop = 0
#             sp = sp[1:]
#             size = len(sp)
