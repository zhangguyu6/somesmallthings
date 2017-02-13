'''
一个自解析字符串的计算器
'''


def isnum(word):
    return word in '0123456789'

def issyb(word):
    return word in '+-*/()'

def parse(words):
    wordsl=[]
    conn=0
    if len(words)<=1:
        return words
    for i in range(len(words)):
        if isnum(words[i]):
            if i ==0 or issyb(words[i-1]):
                conn=i
            if i==len(words)-1 or issyb(words[i+1]):
                wordsl.append(int(words[conn:i+1]))

        if  words[i]=='-' and issyb(words[i-1]):
            wordsl.append(words[i])

        elif issyb(words[i]):
            wordsl.append(words[i])
    return wordsl

def calculator(wordsl):
    #整数直接返回
    if len(wordsl)==1:
        return wordsl[0]

    # 去括号
    for i in range(len(wordsl)):
        if wordsl[i]=='(':
            for j in range(len(wordsl)-1,0,-1):
                if wordsl[j]==')':
                    wordsl[i:j+1]=[calculator(wordsl[i+1:j])]
                    return calculator(wordsl)
    # 取负
    for i in range(len(wordsl)):
        if i==0 and wordsl[i]=='-' or issyb(str(wordsl[i-1])) and wordsl[i]=='-':
            wordsl[i:i+2]=[-wordsl[i+1]]
            return calculator(wordsl)


    #4则运算
    if wordsl[1] == '+':
        return wordsl[0]+calculator(wordsl[2:])
    elif wordsl[1] == '-':
        return wordsl[0]-calculator(wordsl[2:])
    elif wordsl[1] == '/':
        wordsl[:3]=[wordsl[0]/wordsl[2]]
        return calculator(wordsl)
    elif wordsl[1]=='*':
        wordsl[:3]=[wordsl[0]*wordsl[2]]
        return calculator(wordsl)

wordsl=parse('((2+2)/4)/-2')
print(wordsl)

print(calculator(wordsl))

