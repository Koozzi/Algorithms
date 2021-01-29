if __name__=="__main__":
    N = int(input())

    books = {}
    for i in range(N):
        book = input()

        if book in books:
            books[book] += 1
        else:
            books[book] = 1

    l = []
    for key in books.keys():
        item = books[key]
        l.append([key, item])
    
    sorted_list = sorted(l, key=lambda x:(-x[1], x[0]))

    print(sorted_list[0][0])