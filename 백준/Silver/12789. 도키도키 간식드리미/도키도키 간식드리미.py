def can_pass_in_order(queue):
    stack = []
    expected = 1
    
    while queue:
        if queue[0] == expected:
            queue.pop(0)
            expected += 1
        elif stack and stack[-1] == expected:
            stack.pop()
            expected += 1
        else:
            stack.append(queue.pop(0))
            
    while stack:
        if stack.pop() != expected:
            return "Sad"
        expected += 1
    
    return "Nice"
    
if __name__ == "__main__":
    n = int(input().strip())
    queue = list(map(int, input().strip().split()))
    print(can_pass_in_order(queue))