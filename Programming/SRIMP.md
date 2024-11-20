# SRIMP

SA-KRIMP

## Algorithm

Input: A transaction database D ,Temp, Min_Temp, 𝛼

Output: CT that best compresses the dataset

1. Initialization: population ← items from D;𝑇 ← 𝑇 𝑒𝑚𝑝; 𝑀𝑇 ← 𝑀𝑖𝑛_𝑇 𝑒𝑚𝑝;

2. Generate a initial patternset 

3. while 𝑇 > 𝑀𝑇 do

  ​	for each pattern $P_i$ in patternset

  1. $CT_i$ ← (CT ∪ $P_i$)
  3. if L(D, $CT_i$)<L(D, CT ) then
  	1. CT ←$CT_i$
  4. else j becomes the current solution with probability  $ e^{\frac{L(D, CT_i)-L(D, CT )}{Temp}} $

​		end for

​		GenerateNeighbor();

​		Randomly replace some patterns in current PatternSet with patterns from codetable

​		Temp = Temp * 𝛼

return codetable;



### Notices

So the pattern_set_size parameter is important, the bigger pattern_set_size is, the average compression ration get better. Meanwhile, the bigger pattern_set_size is, the time it takes to run get longer
