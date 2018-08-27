import time

def findSubstring(s, words):
        import re
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        length = len(s)
        size = len(words)
        if size == 0 or length == 0 or (len(words[0])*size)> length:
            return res

        if size == 1:
            return s.find(words[0])
        elif size == 2:
            w1 = words[0] + words[1]
            w2 = words[1] + words[0]
            w1 = s.find(w1)
            w2 = s.find(w2)
            if w1 == -1 and w2 == -1:
                res = []
            elif w1 == -1:
                res = [w2]
            elif w2 == -1:
                res = [w1]
            else:
                res = [w1, w2]
        else:
            container = dict()
            low = None
            for n in range(0, len(words)):
                r = [k.start() for k in re.finditer(words[n], s)]
                if r != []:
                    try:
                        if container[words[n]]:
                            container[words[n]+str(n)] = r
                    except:
                        container[words[n]] = r
                    if low == None:
                        low = len(r)
                        low_word = (words[n],r)
                    elif low > len(r):
                        low = len(r)
                        low_word = (words[n], r)
                else:
                    return []
            if len(low_word[0]) != len(words[0]):
                return []
            print(low_word)
            print(container)
            n = 0
            string = ""

        return res


def main():

    string = "barfoothefoobarman"
    word_list = ["foo","bar"]

    result = findSubstring(string, word_list)
    print(result)

    string = "wordgoodstudentgoodword"
    word_list = ["word","student"]

    result = findSubstring(string, word_list)
    print(result)

    string = "barfoofoobarthefoobarman"
    word_list = ["bar","foo","the"]

    result = findSubstring(string, word_list)
    print(result)

    string = "bbabbbab"
    word_list = ["ab","bb","bc","ac"]

    result = findSubstring(string, word_list)
    print(result)

    string = "wordgoodgoodgoodbestword"
    word_list = ["word","good","best","word"]

    result = findSubstring(string, word_list)
    print(result)
    

start = time.time()
main()
print("{}s".format(time.time() - start))