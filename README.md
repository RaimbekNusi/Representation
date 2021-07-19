# Representation (Simple file I/O and numpy array operations/ENGLISH)
## Description of the problem

In Canada, the federal government is made up of a number of seats. The seats are divided among the provinces; for example, Saskatchewan has 14 seats, while Ontario has 121. Using population data from the Canadian census the program is written to determine which provinces are over- or under- reprented in the federal government based on their populations.

The main purpose of this question is to practice data manipulation using numpy arrays. Therefore all of the signifcant calculations needs to be done by using numpy array operations. Array arithmetic, array relations, and logical array indexing are utilized in this program.

## Details of the problem
The file provincial_seats.txt is provided as an example of database. Each line consists of a province or territory’s name, its population (rounded to the nearest thousand) and
its number of seats in the government, all separated by commas:

![image](https://user-images.githubusercontent.com/86201781/126115182-6265ce09-018e-4323-87f1-1dd5470fd640.png)


## Step-by-step solution

Using array operations on the loaded data, an array created that contains, for each province, the expected number of seats that each province WOULD have if its seats were exactly proportional to its population. Then the values are rounded

If a province has more actual seats than the number of seats calculated based on its population above, we’ll call that province over-represented. If it has fewer actual seats than predicted seats, then it is underrepresented.

Using array relational operators and logical indexing to create three arrays for:
• the names of the over-represented provinces
• the expected seats of those provinces
• the actual seats of those provinces

Then the same will be done for the under-represented provinces.

Finally, printing the results to the console. 

## How to use

Here are the steps for how to open, use and utilize the program:

- First, download all of the files listed above;
- Put all the files in one folder;
- Open the file Project_k-means.py;
- The program will open a command console in which it will ask you to name a .txt file located in the same folder;
- Finally, the program will output a graph with results clusterized data.


*The program can use other .txt file that are in the same format as provided files.

# Репрезентация (простой файловый ввод-вывод и операции с массивом numpy / РУССКИЙ)

## Описание задачи

В Канаде федеральное правительство состоит из нескольких мест. Места разделены между провинциями; например, Саскачеван имеет 14 мест, а Онтарио - 121. Используя данные о населении из канадской переписи, программа написана для определения того, какие провинции чрезмерно или недостаточно представлены в федеральном правительстве в зависимости от их населения.

Основная цель этого вопроса - практика в манипулировании данными с использованием массивов numpy. Поэтому все важные вычисления должны выполняться с использованием операций с массивом numpy. В этой программе используются арифметика массивов, отношения массивов и логическая индексация массивов.

## Детали задачи

Файл provincial_seats.txt предоставляется в качестве примера базы данных. Каждая строка состоит из названия провинции или территории, ее населения (округляется до ближайшей тысячи) и количества мест в правительстве, разделенных запятыми:

![image](https://user-images.githubusercontent.com/86201781/126115182-6265ce09-018e-4323-87f1-1dd5470fd640.png)

## Пошаговое решение

Используя операции с массивом загруженных данных, создается массив, содержащий для каждой провинции ожидаемое количество мест, которое БУДЕТ иметь каждая провинция, если бы ее места были точно пропорциональны ее населению. Затем значения округляются.

Если в провинции имеется больше фактических мест, чем количество мест, рассчитанное на основе ее населения выше, мы будем называть эту провинцию перепредставленной. Если у него меньше фактических мест, чем прогнозировалось, значит, он недопредставлен.

Использование операторов отношения массивов и логической индексации для создания трех массивов для:
• названия перепредставленных провинций
• ожидаемые места в этих провинциях
• фактические центры этих провинций

Затем то же самое будет сделано для недостаточно представленных провинций.

Наконец, вывод результатов на консоль.



