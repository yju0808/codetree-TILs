n = int(input())

nums = ['4', '5', '6']


def is_possible(sequence):
    
    for idx in range(len(sequence)):
        
        length = 1
        while True:
      
            start1, end1 = idx, idx + length - 1
            start2, end2 = end1 + 1, (end1 + 1) + length - 1
  
            if end2 >= len(sequence):
                break
      
            if sequence[start1:end1 + 1] == sequence[start2:end2 + 1]:
                return False
            
            length += 1

    return True


candi = []

ans = ['9']


def solve():

    global ans

    if not is_possible(candi):
        return

    if len(candi) == n:
        ans = min(ans, candi[:])
        return


    for i in range(3):
        candi.append(nums[i])
        solve()
        candi.pop()


solve()
print("".join(ans))