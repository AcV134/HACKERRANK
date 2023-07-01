def minion_game(word):
    n = len(word)
    count_t = n*(n+1)//2
    count_v = sum([(n-i) for i in range(len(word)) if word[i] in 'AEIOU'])
    print(*('Stuart ',count_t - count_v) if count_t//2 > count_v else (('Kevin ',count_v) if count_v>count_t//2 else ('Draw')),sep ='')

if __name__ == '__main__':
    s = input()
    minion_game(s)
