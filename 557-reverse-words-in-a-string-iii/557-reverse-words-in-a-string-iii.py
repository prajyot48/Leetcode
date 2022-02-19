class Solution:
    def reverseWords(self, s: str) -> str:
        x =s.split(' ')
        strg=""
        for i in x:
            y=i[::-1]
            # print(i[::-1],type(i))
            strg=strg+y+" "
        
        return(strg[:-1])
        # print(len(x))