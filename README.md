# Map-Reduce

*Studying to deal with data using Hadoop*

How to start:

1. mapper.py читает из ratings.dat, выводит <<пользователь + поставленный им рейтинг>>
2. reducer.py читает данные с маппера, далее для каждого пользователя считает средний его рейтинг, выводит: <<пользователь + средний рейтинг>>
3. mapper_1.py читает вывод с редьюсера и сохраняет для каждого пользователя его рейтинг, а также формирует пары фильмов и всех пользователей, котоые смотрели эту пару: выводит <<фильм1 + фильм2 + рейтинг_1 + рейтинг пользователя + рейтинг_2>>
4. reducer_1.py считает матрицу sim (для каждой пары полученных фильмов из маппера)  
*между данными шагами файл run.py записывается в словарь-файл*
5. mapper_2.py читает из ratings.dat данные о пользователях и возвращает <<пользователь + фильм + оценка>>
6. reducer_2.py получает данные, кроме того использует матрицу sim, выдает рекомендации (финальные).

ЗАПУСК:
        * task/src - здесь хранится код функции mapper*.py, reducer*.py  
        * task/data/input - здесь ratings.dat  
        * task/data - здесь all_films_big.txt (содержит все названия фильмов), movies.dat  
        * task - здесь run.py (который создает file_big - словарь, словарь нужно переместить далее в папку data командой: mv file_big data - из task), скрипты run_big.sh, run_big_1.sh, run_big_2.sh  
Команды: *все из task*
	* sh run_big.sh # первая м-р задача
	* Выход в data/output_big
	* sh run_big_1.sh # вторая м-р задача
	* Выход в data/output_big_1
	* cat data/output_big_1/* | python3 run.py # создание файла file_big
	* sh run_big_2.sh # третья м-р задача
	* Выход в data/output_big_2
