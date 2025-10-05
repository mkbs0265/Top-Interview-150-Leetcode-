class Solution:
    def minOperations(self, s: str) -> int:
        # c=0
        # k=s[0]
        # for i in range(1,len(s)):
        #     if s[i]!=k[-1]:
        #         k+=s[i]
        #     else:
        #         c+=1
        #         if s[i]=='0':
        #             k+='1'
        #         else:
        #             k+='0'
        # return c
        k1=""
        k2=""
        for i in range(len(s)):
            if i%2==0:
                k1+='1'
                k2+='0'
            else:
                k1+='0'
                k2+='1'
        c1=0
        c2=0
        for i in range(len(s)):
            if s[i]!=k1[i]:
                c1+=1
            if s[i]!=k2[i]:
                c2+=1
        return min(c1,c2)