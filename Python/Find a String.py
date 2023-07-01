def count_substring(string, sub_string):
    i = len(sub_string)
    count = 0
    while i !=len(string)+1:
        # print(string[i-len(sub_string):i])
        if sub_string == string[i-len(sub_string):i]:
            count+=1
        i+=1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
