while True:
    try:
        A,B,C = list(map(int, input().split()))
        print(max(B-A, C-B)-1)
    except:
        break

    # cnt = 0
    # arr = [A,B,C]
    # while True:
    #     if arr[2]-arr[0] == 2:
    #         print(cnt)
    #         break
    #     elif arr[1]-arr[0] > arr[2]-arr[1]:
    #         cnt += 1
    #         arr[2] = arr[0]+1
    #         arr.sort()
    #     elif arr[1]-arr[0] <= arr[2]-arr[1]:
    #         cnt += 1
    #         arr[0] = arr[2]-1
    #         arr.sort()
