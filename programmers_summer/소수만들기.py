def isPrime(num):
    # even number
    if num % 2 == 0 :
        return False
    
    odds = set([i for i in range(3, num, 2)]) # odd nums from 3 to num-1
    for odd in odds:
        if num%odd == 0:
            return False
    return True

def solution(nums):
    count = 0
    
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                if isPrime(num):
                    count += 1
    return count