import sys 

if __name__ == '__main__':
    input = sys.stdin.readline
    k = int(input())
    stack = []
    for _ in range(k):
        num = int(input())
        if num:
            stack.append(num)
        else:
            stack.pop()
    print(sum(stack))
