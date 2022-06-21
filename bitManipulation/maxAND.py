def maxAND(L, R):

    if (L == R):
        return L;

    elif ((R - L) == 1):
        return (R & L);
    else:
        if (((R - 1) & R) >
            ((R - 2) & (R - 1))):
            return ((R - 1) & R);
        else:
            return ((R - 2) & (R - 1));

for _ in range(int(input())):
  a,b=map(int,input().split())
  print(maxAND(a,b))
  