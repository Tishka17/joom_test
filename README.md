## Задание
Необходимо реализовать построчную сортировку большого текстового файла, не влезающего в память. 

Для проверки работоспособности нужен генератор таких файлов, принимающий в качестве параметров максимальное количество строк и их длину.
 
## Решение

Для сортировки большого файла необходимо разбить его на части, каждая из которых может быть отсортирована независимо.

После сортировки части объединяются. 

Промежуточные результаты хранятся на диске.

Количество одновременно хранящихся частей и размер части указываются при запуске скрипта сортировки


### Пример запуска

Генерация:
```sh
./generate.py -c 5000000 -l 100 -C > in.txt
```

Сортировка:
```sh
./sort.py -i in.txt -s 100000 -c 10
```