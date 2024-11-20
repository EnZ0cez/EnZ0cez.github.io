# GRIMP

### 1. 导入包和类定义

```java
java复制代码package ESFinal;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;

/**
 *
 * @author DELL
 */
public class GRIMP {
```

这部分代码导入了所需的包，并定义了一个名为 `GRIMP` 的类。导入的包包括文件读取、集合操作和随机数生成等功能。

### 2. 全局变量和 `main` 函数定义

```java
	private static int Pat1Count = 0;
    private static int Pat2Count = 0;

    public static void main(String[] args) {
        int randPatterns = 8;
        int minimumItemValue = 0;
        int maximumItemValue = 0;
        int numberOfIterations = 5;
        int numberOfMutationPoints = 2; // used in Multi Point Mutation only

        String inpp = "irisVrekeen.txt";
        int patterns = 13;
        ArrayList<ArrayList<Integer>> sequence = readItemsetsFromFile(inpp);

        int AcS = 0; // minimum acceptable resultant pattern size
        String crossOverOperator = null, mutationOperator = null;
```

这一部分初始化了一些全局变量和 `main` 函数的初始参数。`Pat1Count` 和 `Pat2Count` 用于计数模式1和模式2出现的次数。`main` 函数初始化了遗传算法的一些参数，如随机模式数、迭代次数和变异点数等，并读取输入文件生成项集序列。

### 3. 迭代不同的交叉和变异操作

```java
        for (int i = 1; i <= 6; i++) {
            MemoryLogger logger = MemoryLogger.getInstance();
            logger.startRecordingMode("memory_logs.txt");
            switch (i) {
                case 1:
                    crossOverOperator = "single";
                    mutationOperator = "single";
                    break;
                case 2:
                    crossOverOperator = "multi";
                    mutationOperator = "single";
                    break;
                case 3:
                    crossOverOperator = "uniform";
                    mutationOperator = "single";
                    break;
                case 4:
                    crossOverOperator = "single";
                    mutationOperator = "multi";
                    break;
                case 5:
                    crossOverOperator = "multi";
                    mutationOperator = "multi";
                    break;
                case 6:
                    crossOverOperator = "uniform";
                    mutationOperator = "multi";
                    break;
                default:
                    break;
            }
            System.out.println(crossOverOperator + ", Mutation: " + mutationOperator);
```

这一部分定义了一个循环，通过六种不同的组合来测试交叉和变异操作，并开始记录内存使用情况。每个循环都会设置相应的交叉和变异操作类型，并打印当前的操作组合。

### 4. 主循环，直到找到所需的模式数

```java
            long startTime = System.currentTimeMillis();
            ArrayList<ArrayList<Integer>> subSequence = new ArrayList<>(sequence);
            ArrayList<ArrayList<Integer>> finalResult = new ArrayList<>();
            int sub = finalResult.size();

            for (int ol = 1; finalResult.size() <= patterns; ol++) {
                long startTimeLoop = System.currentTimeMillis();
                if (finalResult.size() % 5 == 0 && sub != finalResult.size()) {
                    sub = finalResult.size();
                }

                Map<Integer, Integer> itemFrequency = new HashMap<>();
                for (List<Integer> transaction : subSequence) {
                    for (Integer item : transaction) {
                        itemFrequency.put(item, itemFrequency.getOrDefault(item, 0) + 1);
                    }
                }

                Set<Integer> population = new HashSet<>();
                for (ArrayList<Integer> set : subSequence) {
                    population.addAll(set);
                }

                int longestItemSet = 0;
                for (ArrayList<Integer> set : subSequence) {
                    int max = !set.isEmpty() ? Collections.max(set) : 0;
                    int min = !set.isEmpty() ? Collections.min(set) : 0;
                    if (max > maximumItemValue) {
                        maximumItemValue = max;
                    }
                    if (minimumItemValue == 0) {
                        minimumItemValue = min;
                    } else if (min < maximumItemValue) {
                        minimumItemValue = min;
                    }
                    if (set.size() > longestItemSet) {
                        longestItemSet = set.size();
                    }
                }

                ArrayList<Integer> Pat1 = generateRandomItemset(longestItemSet, itemFrequency);
                ArrayList<Integer> Pat2 = generateRandomItemset(longestItemSet, itemFrequency);
```

在这一部分，程序开始主循环，直到找到所需数量的模式。首先，记录当前时间，并将输入序列复制到 `subSequence` 中。然后，计算每个项目的频率，并获取集合中的所有独特项目。此外，还找到了序列中最长的项集。最后，生成两个随机模式 `Pat1` 和 `Pat2`。

### 5. 模式的迭代过程

```java
                for (int pat = 1; pat <= numberOfIterations; pat++) {
                    ArrayList<Integer> tPat1 = new ArrayList<>(Pat1);
                    ArrayList<Integer> tPat2 = new ArrayList<>(Pat2);
                    ArrayList<ArrayList<Integer>> crossoverResult;

                    switch (crossOverOperator) {
                        case "multi":
                            crossoverResult = MPCrossoverOperator(tPat1, tPat2);
                            break;
                        case "uniform":
                            crossoverResult = uniformCrossoverAdaptiveSwap(tPat1, tPat2, 0.5);
                            break;
                        case "single":
                            crossoverResult = SPcrossoverOperator(tPat1, tPat2);
                            break;
                        default:
                            System.out.print("Wrong crossover operator!");
                            return;
                    }
                    tPat1 = crossoverResult.get(0);
                    tPat2 = crossoverResult.get(1);

                    switch (mutationOperator) {
                        case "single":
                            tPat1 = standardMutationOperator(tPat1, population);
                            tPat2 = standardMutationOperator(tPat2, population);
                            break;
                        case "multi":
                            tPat1 = multiPointMutation(tPat1, numberOfMutationPoints, itemFrequency);
                            tPat2 = multiPointMutation(tPat2, numberOfMutationPoints, itemFrequency);
                            break;
                        default:
                            System.out.print("Wrong mutation operator!");
                            return;
                    }

                    ArrayList<ArrayList<Integer>> remainingSequence = deleteItemset(subSequence, tPat1, tPat2);

                    if (Pat1Count > GP1C) {
                        GP1C = Pat1Count;
                        FPat1 = tPat1;
                    }
                    if (Pat2Count > GP2C) {
                        GP2C = Pat2Count;
                        FPat2 = tPat2;
                    }
                    int compressDatabaseSize = calculateSizeInBits(remainingSequence);
                    compressDatabaseSize = compressDatabaseSize + (tPat1.size() * Integer.SIZE) + (tPat2.size() * Integer.SIZE);
                }

                ArrayList<ArrayList<Integer>> remainingSequence = deleteItemset(sequence, FPat1, FPat2);
                subSequence = remainingSequence;
                if (FPat1.size() > AcS) {
                    finalResult.add(FPat1);
                }
                if (FPat2.size() > AcS) {
                    finalResult.add(FPat2);
                }
                long endTimeLoop = System.currentTimeMillis();
                long elapsedTimeLoop = endTimeLoop - startTimeLoop;
            }

            int originalDatabaseSize = calculateSizeInBits(sequence);
            int compressSizeInBits2 = deleteAndCalculateSizeInBits2(sequence, finalResult);
            System.out.println("Compression with code table: " + (float) compressSizeInBits2 / originalDatabaseSize * 100);

            long endTime = System.currentTimeMillis();
            long elapsedTime = endTime - startTime;
            double currentMemoryUsage = logger.checkMemory();
            logger.stopRecordingMode();
            logger.reset();
            System.out.println((float) compressSizeInBits2 / originalDatabaseSize * 100 + " " + (double) (elapsedTime) / 1000 + " " + currentMemoryUsage + " " + finalResult.size());
        }
    }
}
```

这一部分是模式迭代过程的核心部分。在每次迭代中，程序生成两个模式 `Pat1` 和 `Pat2` 的副本，并根据选择的交叉操作和变异操作更新这些模式。然后，程序计算删除模式后的剩余序列，并记录最优的模式。最后，程序更新序列并计算压缩后的大小，记录压缩比、运行时间和内存使用情况。

### 6. 辅助函数

下面是一些辅助函数，用于执行特定的操作：

#### 读取项集文件

```java
public static ArrayList<ArrayList<Integer>> readItemsetsFromFile(String fileName) {
    ArrayList<ArrayList<Integer>> sequence = new ArrayList<>();

    try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
        String line;
        while ((line = reader.readLine()) != null) {
            ArrayList<Integer> transaction = new ArrayList<>();
            String[] items = line.split("\\s+");
            for (String item : items) {
                transaction.add(Integer.valueOf(item.trim()));
            }
            sequence.add(transaction);
        }
    } catch (IOException e) {
        System.err.println("Error reading file: " + e.getMessage());
    } catch (NumberFormatException e) {
        System.err.println("Error parsing integer: " + e.getMessage());
    }

    return sequence;
}
```

这个函数从文件中读取项集，并将其转换为 `ArrayList<ArrayList<Integer>>` 形式。

#### 生成随机项集

```java
public static ArrayList<Integer> generateRandomItemset(int longestItemSet, Map<Integer, Integer> itemFrequency) {
    ArrayList<Integer> randomSet = new ArrayList<>();
    Random random = new Random();
    int randomItemsetSize = 2 + random.nextInt(longestItemSet - 1);
    while (randomSet.size() < randomItemsetSize) {
        Integer randomNumber = getWeightedRandomItem(itemFrequency);
        if (!randomSet.contains(randomNumber)) {
            randomSet.add(randomNumber);
        }
    }
    return randomSet;
}

public static Integer getWeightedRandomItem(Map<Integer, Integer> itemFrequency) {
    int totalWeight = 0;
    for (int weight : itemFrequency.values()) {
        totalWeight += weight;
    }

    if (totalWeight == 0) {
        throw new IllegalArgumentException("Total weight must be greater than zero.");
    }

    Random random = new Random();
    int randomNumber = random.nextInt(totalWeight);

    int cumulativeWeight = 0;
    for (Map.Entry<Integer, Integer> entry : itemFrequency.entrySet()) {
        cumulativeWeight += entry.getValue();
        if (randomNumber < cumulativeWeight) {
            return entry.getKey();
        }
    }

    throw new IllegalStateException("No item selected. Check the input data.");
}
```

这两个函数用于生成随机项集。`generateRandomItemset` 函数生成一个随机大小的项集，而 `getWeightedRandomItem` 函数根据项的频率加权随机选择一个项。

#### 删除项集并计算大小

```java
public static ArrayList<ArrayList<Integer>> deleteItemset(ArrayList<ArrayList<Integer>> sequence, List<Integer> Pat1, List<Integer> Pat2) {
    ArrayList<ArrayList<Integer>> modifiedSequence = new ArrayList<>();
    int pat1Count = 0;
    int pat2Count = 0;

    for (ArrayList<Integer> transaction : sequence) {
        ArrayList<Integer> modifiedTransaction = new ArrayList<>(transaction);

        if (modifiedTransaction.containsAll(Pat1)) {
            pat1Count++;
            modifiedTransaction.removeAll(Pat1);
        }

        if (modifiedTransaction.containsAll(Pat2)) {
            pat2Count++;
            modifiedTransaction.removeAll(Pat2);
        }

        modifiedSequence.add(modifiedTransaction);
    }
    Pat1Count = pat1Count;
    Pat2Count = pat2Count;

    return modifiedSequence;
}
```

这个函数从序列中删除给定的模式，并返回删除后的新序列。

#### 单点变异和多点变异操作

```java
public static ArrayList<Integer> standardMutationOperator(ArrayList<Integer> C, Set<Integer> allItems) {
    if (C.isEmpty() || allItems.isEmpty()) {
        return C;
    }

    int randomIndex = new Random().nextInt(C.size());
    int itemToReplace = C.get(randomIndex);

    ArrayList<Integer> allItemsList = new ArrayList<>(allItems);
    int newItem;
    do {
        newItem = allItemsList.get(new Random().nextInt(allItemsList.size()));
    } while (newItem == itemToReplace);

    C.set(randomIndex, newItem);

    return C;
}

public static ArrayList<Integer> multiPointMutation(ArrayList<Integer> C, int mutationPoints, Map<Integer, Integer> itemFrequency) {
    if (mutationPoints <= 0 || C.isEmpty() || C.size() < mutationPoints) {
        return C;
    }

    Random random = new Random();
    Set<Integer> usedIndices = new HashSet<>();

    for (int i = 0; i < mutationPoints; i++) {
        int randomIndex;
        do {
            randomIndex = random.nextInt(C.size());
        } while (usedIndices.contains(randomIndex));

        usedIndices.add(randomIndex);

        int itemToReplace = C.get(randomIndex);

        int newItem;
        do {
            newItem = getWeightedRandomItem(itemFrequency);
        } while (newItem == itemToReplace);

        C.set(randomIndex, newItem);
    }

    return C;
}
```

这两个函数分别实现了单点变异和多点变异操作，通过替换项集中的随机项来实现变异。

#### 单点交叉和多点交叉操作

```java
public static ArrayList<ArrayList<Integer>> SPcrossoverOperator(ArrayList<Integer> P1Sol, ArrayList<Integer> P2Sol) {
    int smallestSize = Math.min(P1Sol.size(), P2Sol.size());
    Random random = new Random();
    int cutoffPoint = random.nextInt(smallestSize - 1) + 2;

    ArrayList<ArrayList<Integer>> crossoverResult = performSPCrossover(P1Sol, P2Sol, cutoffPoint);

    return crossoverResult;
}

public static ArrayList<ArrayList<Integer>> performSPCrossover(ArrayList<Integer> P1Sol, ArrayList<Integer> P2Sol, int cutoffPoint) {
    ArrayList<Integer> child1 = new ArrayList<>(P1Sol.subList(0, cutoffPoint));
    child1.addAll(P2Sol.subList(cutoffPoint, P2Sol.size()));

    ArrayList<Integer> child2 = new ArrayList<>(P2Sol.subList(0, cutoffPoint));
    child2.addAll(P1Sol.subList(cutoffPoint, P1Sol.size()));

    ArrayList<ArrayList<Integer>> crossoverResult = new ArrayList<>();
    crossoverResult.add(child1);
    crossoverResult.add(child2);

    return crossoverResult;
}

public static ArrayList<ArrayList<Integer>> MPCrossoverOperator(ArrayList<Integer> P1Sol, ArrayList<Integer> P2Sol) {
    int smallestSize = Math.min(P1Sol.size(), P2Sol.size());
    if (smallestSize <= 3) {
        ArrayList<ArrayList<Integer>> crossoverResult = new ArrayList<>();
        crossoverResult.add(P1Sol);
        crossoverResult.add(P2Sol);
        return crossoverResult;
    }
    ArrayList<Integer> crossoverPoints = generateCrossoverPoints2(smallestSize);
    ArrayList<ArrayList<Integer>> crossoverResult = performMPCrossover2(P1Sol, P2Sol, crossoverPoints);
    return crossoverResult;
}
```

这两个函数分别实现了单点交叉和多点交叉操作，通过在项集中选择交叉点并交换部分项集来实现交叉。

#### 均匀交叉操作

```java
public static ArrayList<ArrayList<Integer>> uniformCrossoverAdaptiveSwap(ArrayList<Integer> parent1, ArrayList<Integer> parent2, double crossoverRate) {
    ArrayList<Integer> shorter = parent1.size() <= parent2.size() ? parent1 : parent2;
    ArrayList<Integer> longer = parent1.size() > parent2.size() ? parent1 : parent2;

    Random random = new Random();

    List<Integer> indices = new ArrayList<>();
    for (int i = 0; i < longer.size(); i++) {
        indices.add(i);
    }
    Collections.shuffle(indices, random);

    for (int i = 0; i < shorter.size(); i++) {
        if (random.nextDouble() < crossoverRate) {
            int indexFromLonger = indices.get(i);
            Integer temp = shorter.get(i);
            shorter.set(i, longer.get(indexFromLonger));
            longer.set(indexFromLonger, temp);
        }
    }

    ArrayList<ArrayList<Integer>> crossoverResult = new ArrayList<>();
    crossoverResult.add(new ArrayList<>(parent1));
    crossoverResult.add(new ArrayList<>(parent2));

    return crossoverResult;
}
```

这个函数实现了均匀交叉操作，通过在父项之间交换项来实现交叉。

#### 删除项集并计算大小

```java
public static int deleteAndCalculateSizeInBits(ArrayList<ArrayList<Integer>> sequence, ArrayList<ArrayList<Integer>> finalResult) {
    ArrayList<ArrayList<Integer>> modifiedSequence = new ArrayList<>();

    for (ArrayList<Integer> transaction : sequence) {
        ArrayList<Integer> modifiedTransaction = new ArrayList<>(transaction);

        for (ArrayList<Integer> finalTransaction : finalResult) {
            if (modifiedTransaction.containsAll(finalTransaction)) {
                modifiedTransaction.removeAll(finalTransaction);
            }
        }

        modifiedSequence.add(modifiedTransaction);
    }

    int totalSizeInBits = 0;
    for (ArrayList<Integer> transaction : modifiedSequence) {
        totalSizeInBits += transaction.size() * Integer.SIZE;
    }

    return totalSizeInBits;
}

public static int deleteAndCalculateSizeInBits2(ArrayList<ArrayList<Integer>> sequence, ArrayList<ArrayList<Integer>> finalResult) {
    ArrayList<ArrayList<Integer>> modifiedSequence = new ArrayList<>();
    Map<List<Integer>, Integer> patternCount = new HashMap<>();

    for (ArrayList<Integer> pattern : finalResult) {
        patternCount.put(pattern, 0);
    }

    for (ArrayList<Integer> transaction : sequence) {
        ArrayList<Integer> modifiedTransaction = new ArrayList<>(transaction);

        for (ArrayList<Integer> finalTransaction : finalResult) {
            if (modifiedTransaction.containsAll(finalTransaction)) {
                patternCount.put(finalTransaction, patternCount.get(finalTransaction) + 1);
                modifiedTransaction.removeAll(finalTransaction);
            }
        }

        modifiedSequence.add(modifiedTransaction);
    }

    int totalSizeInBits = 0;

    for (ArrayList<Integer> transaction : modifiedSequence) {
        totalSizeInBits += transaction.size() * Integer.SIZE;
    }

    for (Map.Entry<List<Integer>, Integer> entry : patternCount.entrySet()) {
        int patternSize = 0;
        if (entry.getValue() != 0) {
            int keySize = entry.getKey().size();
            int valueBitSize = (int) Math.ceil(Math.log(keySize + 1) / Math.log(2));
            patternSize = valueBitSize + keySize * Integer.SIZE;
        }

        totalSizeInBits += patternSize;
    }

    return totalSizeInBits;
}
```

这两个函数计算删除模式后的序列大小，并返回压缩后的大小（以位为单位）。第一个函数直接计算大小，第二个函数同时记录模式的出现次数并考虑模式的编码大小。

通过这些详细的分段分析，我们可以更好地理解这段代码实现了一个基于遗传算法的模式发现过程，并通过多种交叉和变异操作来寻找最优模式，并最终计算压缩比率。





Init()

sequence = database;

chooseOperators

tPat1,2 = crossoverResult

tPat1,2 mutate

```java
remainingSequence = deleteItemset(subSequence, tPat1, tPat2)
    
```

deleteItemset中计算Patcount

