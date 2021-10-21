a = 'likes this'
b = ['Alex', 'Tanya', 'Sveta', 'Nastya']
c = 'No like this, put a like :'
i = 2
likes = []

if len(likes) == 0:
    print(c)
    likes.append(input())
for user in likes:
    if len(likes) == 1:
       print(b[0], a, sep=' ')
       likes.append(input())
    elif len(likes) == 2:
        print(b[0], 'and', b[1], a, sep=' ')
        likes.append(input())
    elif len(likes) == 3:
        print(b[0], ',', b[1], 'and', b[2], a, sep=' ')
        likes.append(input())
    elif len(likes) >= 4:
        print(b[0], ',', b[1], 'and', i, 'others', a, sep=' ')
        i += 1
        likes.append(input())