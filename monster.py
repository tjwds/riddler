# monster.py:  solving this week's riddler in python 3
# joe woods, @tjwds
# see http://fivethirtyeight.com/features/can-you-slay-the-puzzle-of-the-monsters-gems/

import random

hackyGemArray = ["Common"] * 3 + ["Uncommon"] * 2 + ["Rare"]
numCommon = []

for x in range(0, 1000000):
    resultsArray = []
    while not ( ('Common' in resultsArray) and ('Uncommon' in resultsArray) and ('Rare' in resultsArray) ): 
        number = random.randint(0, 5)
        resultsArray += [hackyGemArray[number]]
    numCommon += [resultsArray.count("Common")]

print('Average number of common gems: ' + str(sum(numCommon) / float(len(numCommon))))

# Average number of common gems: 3.652736
# Average number of common gems: 3.65038
# Average number of common gems: 3.648415
# Average number of common gems: 3.649607
# Average number of common gems: 3.643267 <- outlier?
# eh, let's just call it 3.65.


