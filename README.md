# Representation

In Canada, the federal government is made up of a number of seats. The seats are divided among the provinces; for example, Saskatchewan has 14 seats, while Ontario has 121. Using population data from the Canadian census the program is written to determine which provinces are over- or under- reprented in the federal government based on their populations.

The main purpose of this question is to practice data manipulation using numpy arrays. Therefore all of the signifcant calculations needs to be done by using numpy array operations. Array arithmetic, array relations, and logical array indexing are utilized in this program.

The file provincial_seats.txt is provided as an example of database. Each line consists of a province or territory’s name, its population (rounded to the nearest thousand) and
its number of seats in the government, all separated by commas.

Using array operations on the loaded data, an array created that contains, for each province, the expected number of seats that each province WOULD have if its seats were exactly proportional to its population. Then the values are rounded

If a province has more actual seats than the number of seats you calculated based on its population above, we’ll call that province over-represented. If it has fewer actual seats than predicted seats, then it is underrepresented.

Using array relational operators and logical indexing to create three arrays for:
• the names of the over-represented provinces
• the expected seats of those provinces
• the actual seats of those provinces

Then we do the same thing for the under-represented provinces.
Finally, print your results to the console. You can use loops for this final task.
