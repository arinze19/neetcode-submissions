def astroidCollision(asteroids):
    stack = []

    def can_collide(node1, node2):
        return node1 >= 0 and node2 < 0

    for asteroid in asteroids:
        if not stack:
            stack.append(asteroid)
        else:
            # handle popping smaller asteroids off the stack
            while stack and stack[-1] >= 0 and \
            can_collide(stack[-1], asteroid) and \
            stack[-1] < abs(asteroid):
                stack.pop()

            # handles cases where the top asteroid is the same
            if stack and \
            can_collide(stack[-1], asteroid) and \
            stack[-1] >= 0 and \
            stack[-1] == abs(asteroid):
                stack.pop()
            # handles final case
            elif not stack or not can_collide(stack[-1], asteroid):
                stack.append(asteroid)

    return stack