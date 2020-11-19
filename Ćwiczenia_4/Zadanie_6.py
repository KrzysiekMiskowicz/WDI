MAX = 4
MAX_VALUE = 10
t1 = [[1, 3, 5, 7], [2, 3, 4, 5], [1, 2, 4, 5], [4, 5, 7, 8]]
#'''

def sort(in_array):
    out_array = [0 for _ in range(MAX*MAX)]
    in_array_pos = [0 for _ in range(MAX)]
    out_array_pos = 0
    while True:
        min_pos = [False for _ in range(MAX)]
        min = MAX_VALUE+1
        for i in range(MAX):
            if in_array_pos[i] < MAX:
                if in_array[i][in_array_pos[i]] < min:
                    min = in_array[i][in_array_pos[i]]
                    min_pos = [False for _ in range(MAX)]
                    min_pos[i] = True
                elif t1[i][in_array_pos[i]] == min and min <= MAX_VALUE:
                    min_pos[i] = True
        
        if min_pos == [False for _ in range(MAX)]:
            return out_array

        out_array[out_array_pos] = min
        out_array_pos += 1
        for i in range(MAX):
            if min_pos[i]:
                in_array_pos[i] += 1


print(sort(t1))
#'''
