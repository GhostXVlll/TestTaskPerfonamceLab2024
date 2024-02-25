import sys

def circular_array_path(n, m):
    array = list(range(1, n+1))
    path = []

    start_idx = 0
    while len(path) < n:
        end_idx = (start_idx + m - 1) % n
        #print(end_idx)
        interval = []

        if end_idx >= start_idx:
            interval = array[start_idx:end_idx+1]
        else:
            interval = array[start_idx:] + array[:end_idx+1]

        path.append(interval[0])
        start_idx = end_idx
        if end_idx == 0:
            break

    return path

if __name__ == '__main__':
    n, m = map(int, sys.argv[1:])
    result = circular_array_path(n, m)
    print(result)