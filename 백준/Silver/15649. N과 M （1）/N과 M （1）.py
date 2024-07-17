def bt(n, lst, ans):
    if len(ans) == n:
        print(*ans)
    else:
        for i in lst:
            if i not in ans:
                ans.append(i)
                bt(n, lst, ans)
                ans.pop()


n, m = map(int, input().split())
lst = [x for x in range(1, n+1)]
bt(m, lst, [])
