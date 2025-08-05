def counting_sort(input_arr, k): # 입력 리스트, 가장 큰 값 + 1
    counts = [0] * (k)
    sorted_arr = [_ for _ in range(len(input_arr))]

    # counts 만들기
    for i in range(len(input_arr)):
        counts[input_arr[i]] += 1 # 해당하는 숫자 인덱스를 1 늘리기
    #print(counts)

    # counts 누적
    for i in range(1, k):
        counts[i] += counts[i-1] # 자기자신 + 이전 인덱스
    #print(counts)

    # sorted_arr 만들기
    for i in range(len(input_arr)-1, -1, -1): # input_arr의 길이 -1번 인덱스부터 0번까지 1씩 감소
        # counts의 해당 인덱스에 해당하는 값 -1, -1한 값에 해당하는 인덱스에 counts의 인덱스 넣기
        counts[input_arr[i]] -= 1
        sorted_arr[counts[input_arr[i]]] = input_arr[i]

    return sorted_arr

arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]