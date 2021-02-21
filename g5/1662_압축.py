string = input()
count, stack = [0] * 50, []
depth = 0

for ch in string:
    if ch != ')':
        if ch == '(':
            depth += 1
            count[depth] = 0
        stack += [ch] 
    else:
        i = len(stack) - [*reversed(stack)].index('(') - 1
        num = count[depth] + len(stack[i+1:])
        depth -= 1
        count[depth] += num * int(stack[i-1])
        del stack[i-1:]
print(count[0] + len(stack))