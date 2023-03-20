# python3

def parallel_processing(n, m, data):
    output = []
    threads = [0] * n
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    for i in range(m):
        min_t = min(enumerate(threads), key=lambda x:x[1])
        output.append((min_t[0], threads[min_t[0]]))
        threads[min_t[0]] += data[i]

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, time in result:
        print(i, time)

if __name__ == "__main__":
    main()
