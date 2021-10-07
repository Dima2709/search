def search (arg, arg1):
    try:
      with open(arg+'.txt', 'r') as d:
        s = d.read()
      b = [',', '.', '=', '-', '(', ')', '/', '_', '—', '!', '?', '\n', ':', '«', '»', ';', "''", ' ', '>', '<', '\t', '›', '·', '|']
      for i in s:
          if i in b:
              s = s.replace(i, " ")
      s = s.split(' ')
      o = []
      for i in s:
         if len(i) > 0:
                o.append(i.lower())
      arg1 = arg1.lower()
      c = []
      for i in range(len(o)):
          if o[i] == arg1:
              c.append(i)
      if len (c) > 0:
          print('Всего слов в тесте - ', len(o))
          print('Найдено совпадений: ', len(c))
          print(' Слово, которое вы ищете, находится на:')
          for i in c:
              print(i + 1, 'месте')
      else:
              print('Слово не найдено, попробуйте еще раз')
    except:
        print('Файл не найден, положите файл в папку с проектом! В формате .txt')

search('тест1','всадник')
