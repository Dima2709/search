def search (arg, arg1):
    with open(arg+'.txt', 'r') as d:
        s = d.read()
        s = s.split(' ')
    b = [',', '.', '=', '-', '(', ')', '/', '_','—', '!','?','\n', ':','«','»']
    for i in range(len(s)):
        for j in s[i]:
            if j in b:
                s[i] = s[i].replace(j, "")
    o = []
    for i in s:
        if len (i) > 0:
            o.append(i.lower())
    arg1 = arg1.lower()
    c = []
    for i in range(len(o)):
        if o[i] == arg1:
            c.append(i)
    if len (c) > 0:
        print('Всего слов в тесте - ', len(o))
        for i in c:
            print(' Слово, которое вы ищете находится на ', i + 1, 'месте')
    else:
            print('Слово не найдено, попробуйте еще раз')

search('test','страшная')