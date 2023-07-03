def merge_the_tools(string, k):
    temp = []
    for i in range(0,len(string)-k+1,k):
        temp.append(([j for j in string[i:i+k]]))
    for i in temp:
        print(*(list(dict.fromkeys(i))),sep = '')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
