class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        A = B = C = D = 0
        r = t
        while r % 2 == 0: r //= 2; A += 1
        while r % 3 == 0: r //= 3; B += 1
        while r % 5 == 0: r //= 5; C += 1
        while r % 7 == 0: r //= 7; D += 1
        if r != 1:
            return "-1"

        EXP = {0:(0,0,0,0), 1:(0,0,0,0), 2:(1,0,0,0), 3:(0,1,0,0), 4:(2,0,0,0),
               5:(0,0,1,0), 6:(1,1,0,0), 7:(0,0,0,1), 8:(3,0,0,0), 9:(0,2,0,0)}

        INF = float('inf')
        dp = [[INF]*(B+1) for _ in range(A+1)]
        dp[0][0] = 0
        for i in range(A+1):
            for j in range(B+1):
                if i == 0 and j == 0:
                    continue
                best = INF
                for d in (2,3,4,6,8,9):
                    e2, e3, _, _ = EXP[d]
                    pi, pj = max(0, i-e2), max(0, j-e3)
                    best = min(best, dp[pi][pj] + 1)
                dp[i][j] = best

        def min_digits(a, b, c, d):
            a = min(max(a,0), A); b = min(max(b,0), B)
            return dp[a][b] + max(c,0) + max(d,0)

        n = len(num)
        digits = [int(ch) for ch in num]

        pre2=[0]*(n+1); pre3=[0]*(n+1); pre5=[0]*(n+1); pre7=[0]*(n+1)
        for i in range(n):
            e2,e3,e5,e7 = EXP[digits[i]]
            pre2[i+1]=pre2[i]+e2; pre3[i+1]=pre3[i]+e3
            pre5[i+1]=pre5[i]+e5; pre7[i+1]=pre7[i]+e7

        has_zero = 0 in digits
        if not has_zero and min_digits(A-pre2[n], B-pre3[n], C-pre5[n], D-pre7[n]) == 0:
            return num

        first_zero = digits.index(0) if has_zero else n

        def build_suffix(req2, req3, req5, req7, length):
            need = min_digits(req2, req3, req5, req7)
            res = ['1'] * (length - need)
            r2,r3,r5,r7 = max(req2,0), max(req3,0), max(req5,0), max(req7,0)
            remaining = need
            for _ in range(need):
                for dgt in range(2, 10):
                    e2,e3,e5,e7 = EXP[dgt]
                    nr2,nr3,nr5,nr7 = max(r2-e2,0), max(r3-e3,0), max(r5-e5,0), max(r7-e7,0)
                    if min_digits(nr2,nr3,nr5,nr7) <= remaining - 1:
                        res.append(str(dgt))
                        r2,r3,r5,r7 = nr2,nr3,nr5,nr7
                        remaining -= 1
                        break
            return ''.join(res)

        upper = min(first_zero, n-1)
        for i in range(upper, -1, -1):
            rem_len = n - 1 - i
            for d in range(digits[i]+1, 10):
                e2,e3,e5,e7 = EXP[d]
                req2, req3 = A-(pre2[i]+e2), B-(pre3[i]+e3)
                req5, req7 = C-(pre5[i]+e5), D-(pre7[i]+e7)
                if min_digits(req2, req3, req5, req7) <= rem_len:
                    return num[:i] + str(d) + build_suffix(req2, req3, req5, req7, rem_len)

        L = max(n+1, min_digits(A, B, C, D))
        return build_suffix(A, B, C, D, L)