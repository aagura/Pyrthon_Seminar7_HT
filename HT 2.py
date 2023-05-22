# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: 
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам
def check_poem(string):
    loud_char= set('аиеёоуыэяю')
    list_poem = string.split ()
    list_syl=[]
    
    for i in range (0,len(list_poem)):
        list_syl.append(sum(map(lambda x : 1 if x in loud_char else 0, list_poem[i])))
        if i!=0 and list_syl[i]!=list_syl[i-1]:
            return 'Пам парам'
    return 'Парам пам-пам'

string ='пара-ра-рам рам-пам-папам па-ра-па-дам'

print(check_poem(string))