def search (arg, arg1):
    try:
      with open(arg+'.txt', 'r') as d:
        s = d.read()
      b = [',', '.', '=', '-', '(', ')', '/', '_', '—', '!', '?', '\n', ':', '«', '»', ';', "''"]
      c = []
      c.append(s)
      for i in range(len(c)):
          for j in c[i]:
              if j in b:
                 c[i] = c[i].replace(j, " ")
      c = [i.split( ) for i in c]
      o = []
      for i in c:
          for j in i:
             if len(j) > 0:
                o.append(j.lower())
      arg1 = arg1.lower()
      for i in arg1:
          if i in b:
              arg1 = arg1.replace(i, "")
      c = []
      for i in range(len(o)):
          if o[i] == arg1:
              c.append(i)
      if len (c) == 1:
          print('Всего слов в тесте - ', len(o))
          print('Найдено 1 совпадение')
          print(' Слово, которое вы ищете, находится на:')
          for i in c:
              print (i + 1, 'месте')
      elif len (c) > 1:
          print('Всего слов в тесте - ', len(o))
          print('Найдено совпадений: ', len(c))
          print(' Слова, которые вы ищете, находится на:')
          for i in c:
              print(i + 1, 'месте')
      else:
              print('Слово не найдено, попробуйте еще раз')
    except:
        print('Файл не найден, положите файл в папку с проектом! В формате .txt')

search('тест1','пушкин')
