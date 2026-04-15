def isHappy(n: int) -> bool:
    visited = set()

    #Outer loop: Continue until n reaches 1 (happy condition)
    # or until n alls into a cycle (unhappy condition)
    while n != 1 and n not in visited:
        visited.add(n)

        #---- INNER LOOP GOES HERE----
        current_sum = 0
        while n > 0:
            #Etrathe the rightmost digit
            digit = n % 10
            #square it and add to the total
            current_sum += digit ** 2
            #remove the rightmost digit from n
            n //= 10
        
        # new assignmetn to n
        n = current_sum
        # Calculate the sum of the squares of the digits of n
        # and assign that new value back to 'n'
        pass

    return n == 1