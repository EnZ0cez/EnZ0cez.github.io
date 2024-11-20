# Pre-SA_KRIMP

The basic framework for mining compressing patterns was defined in Krimp. The aim is to discover the model M (a set of patterns) that best describes the database. The quality of a model is evaluated using the Minimum Description Length (MDL) principle on the basis that a model that is small and compresses well the database will capture the key information that the database contains.

Where should I init the pattern set , if I do it before 

Too many        

        Initialize constants:
        INITIAL_TEMPERATURE = 1000
        MIN_TEMPERATURE = 0.5
        COOLING_RATE = 0.95
        MAX_ITERATIONS = 1000
        pattern_set_size = 30
    
    Initialize data structures:
        codetable = empty list of patterns
        database = read itemsets from input file
        minimumItemValue = 0
        maximumItemValue = 0
        itemFrequency = calculate frequency of each item in the database
        longestItemSet = find the size of the largest itemset in the database
        percentage = calculate roulette wheel percentages based on item frequencies
    
    Generate initial random pattern set:
        currentPatternSet = generate pattern_set_size random itemsets
    
    Calculate initial compression size using MDL:
        initialCompressionSize = calculateMDL(database, codetable)
        currentCompressionSize = initialCompressionSize
    
    Initialize temperature and iteration counter:
        temperature = INITIAL_TEMPERATURE
        iterations = 0
    
    Start Simulated Annealing loop:
        WHILE temperature > MIN_TEMPERATURE AND iterations < MAX_ITERATIONS:
            FOR each pattern in currentPatternSet:
                IF pattern exists in the database:
                    Create a temporary codetable = codetable
                    IF pattern is not in codetable:
                        Add pattern to the temporary codetable
                        newCompressionSize = calculateMDL(database, temp_codetable)
                        IF acceptanceProbability(currentCompressionSize, newCompressionSize, temperature) > random value:
                            Accept new pattern set:
                                currentPatternSet = newPatternSet
                                currentCompressionSize = newCompressionSize
                                codetable = temp_codetable
        Generate neighboring pattern set:
            newPatternSet = empty list
            FOR each pattern in currentPatternSet:
                newPattern = generateNeighborPattern(currentPatternSet, database)
                Add newPattern to newPatternSet
            currentPatternSet = newPatternSet
    
        Randomly replace patterns in currentPatternSet with those from codetable:
            numberOfReplacements = random value between 1 and size of codetable
            FOR i = 1 to numberOfReplacements:
                replaceIndex = random index in currentPatternSet
                patternFromCodetable = random pattern from codetable
                Replace pattern at replaceIndex in currentPatternSet with patternFromCodetable
    
        Decrease temperature:
            temperature = temperature * COOLING_RATE
        Increment iteration counter:
            iterations = iterations + 1
    
    Output results:
        Sort codetable by itemset length
        Print final pattern set, final codetable, final compression size, and compression ratio

**Slide 1: Introduction**
*Presented by Chen Enze*

Hello everyone, today I will be talking about *SA-KRIMP*, a powerful pattern mining algorithm that leverages the principles of data compression. Our presentation will cover the following key areas:

1. Introduction to pattern mining and the role of compression.
2. The SA-KRIMP algorithm and how it works.
3. Some results of our experiments using this approach.

------

**Slide 2: Content Overview**
Here’s what we’ll cover today:

- **Introduction**: A quick dive into the concept of pattern mining and the goal of our study.
- **Algorithm**: Explanation of SA-KRIMP and how it improves upon traditional techniques.
- **Experiment**: Results from applying the algorithm in various scenarios.

------

**Slide 3: Introduction**
Let’s begin by talking about *Pattern Mining*. The goal of pattern mining in data is either to predict future trends or understand past behaviors. A frequent pattern is a set of items frequently occurring together in a dataset, such as customer transactions. The purpose of our study is to discover patterns that are both useful and interpretable for humans. Here is a example of Frequent Itemset Mining ,FIM, which it to find patterns in the transaction database

------

**Slide 4: Introduction to MDL**
We are also using the principle of *Minimum Description Length* or MDL in pattern mining. This says that the best set of patterns, , is the one that compresses the dataset most effectively. This leads us to a key idea: the more a pattern helps reduce the amount of data required to represent the database, the more valuable that pattern is. Here is the definition of the MDL. We try to minimize the length of the  patterns and the description length of the database when encoded with these patterns.

------

**Slide 5: KRIMP for Pattern Mining**

Then lets see how mdl is combined with pattern mining. KRIMP is an algorithm that seeks to discover itemsets that help compress the data. In our case, this approach allows us to identify and retain patterns that are highly efficient in terms of compression. The smaller the resulting dataset after applying the patterns, the better the pattern set is at explaining the data. Basically the process of KRIMP is : Generate a candidate list, for each candidate pattern in the list ,Try to see if this pattern improves the compression, and in the end return a Code Tabel that contains the result patterns.

------

**Slide 6: Transition to Algorithm**
Now, let’s look at how SA-KRIMP works. We’ve improved upon the KRIMP method by introducing simulated annealing. This is an optimization technique inspired by metallurgy, where the idea is to gradually reduce the "temperature" of a system, allowing it to reach a state of minimal energy, or in our case, minimal data redundancy.

------

**Slide 7: The SA-KRIMP Algorithm**
The core of SA-KRIMP lies in selecting patterns that yield the highest compression ratio over a series of iterations. Simulated annealing helps us avoid getting stuck in local minima, and instead, explore various combinations to find the best possible compression.

------

**Slide 8: Experiment Design**
We conducted experiments using datasets such as *irisVrekeen.txt* and *chessFInal.txt*. These experiments varied in the number of iterations, ranging from 100 to 1000 iterations. The goal was to see how well SA-KRIMP performed in terms of both time efficiency and compression quality.

------

**Slide 9: Experiment Results**
One of the key challenges we observed was balancing the number of iterations with the results. More iterations led to better compression sizes but required more computational time. For example:

- With 100 iterations, we achieved an average compression rate of 13.12%, with an elapsed time of 0.093 seconds.
- With 1000 iterations, the compression improved to 8.35%, but the time taken increased significantly.

This led us to question whether we should introduce an *ACCEPTANCE_THRESHOLD* to filter out less significant patterns earlier, to save time.

------

**Slide 10: Conclusion**
In conclusion, SA-KRIMP offers a significant improvement in pattern mining, especially when we aim to balance compression efficiency and time. Our results show that this algorithm holds great promise for applications requiring data compression or efficient pattern discovery.

Thank you for your attention, and I welcome any questions you may have!



# Question1

So we mentioned that bitmap can save time, but for now I haven’t use it in the whole algorithm

count the occurance of 
