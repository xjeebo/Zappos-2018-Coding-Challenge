# find two teams of chefs that provide fastest and highest quality foods
# K(chefs) fill Red and Blue teams with N team members
# every chef in the K pool must cook..qualities are: MPM,Q,Z,F
# every night of week provided M meals needs to be cooked by each time
# T amount of time chefs to cook and GQ; goal quality
# eliminate one chef from the lowest scoring team
# K and F MPM is MPM++ and Q + Q*20; increased 20%
# team score: (Sum(MPM)*AVG(Q)*BonusMultiplier)
# chef eliminated with lowest MPM*Q value,
# once a chef is elminated, chefs go back to pool until 1 left
# in event all chefs cannot cook all meals in time T, no winner
# Overall winner output the two teams R and B followed by Z---------------
# last line is Z chef who won hells kitchen -----------------

# when K with F MPM is increased by 1 Q is increased 20%. 
# split schefs in two teams of size N
# highest score sum(mpm)*avg(q)*bonus
# for k - 1 nights, chefs are given M meals to cook in T time and GQ
# if M cooked within T => eliminate lowest chef else eliminate all
# lowest scoring team by MIN(MPM*Q)
# if no winner print(no winner) else output three 3 lines 
# highest scoring Zs , second highest Z, Z that eliminated, Z that won last line


class chef(object):
    def __init__(self,z,mpm,q,f):
        if f == '*':
            self.friend = False 
            self.score = (q+q*0.20)*(mpm+1)
        else:
            self.score = mpm*q

        self.name = z  # name are in int values
        self.mpm = mpm  # meals per minute
        self.quality = q # quality of the chefs meal
        self.friend = f   # K and F MPM is MPM++ and Q + Q*20; increased 20%

# Acquire Data - Read from input file
# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
f = open("input.txt", "r")

chefName = []
MPM = []
quality = []
friend = []
nMeals = []
goalQuality = []
time = []

n = int(f.readline().strip())
for i in range(0,n):
    a,b,c,d = f.readline().strip().split(' ') # attain input after a space
    chefName.append(a)
    MPM.append(b)
    quality.append(c)
    friend.append(d)
for i in range(0,n-1):
    a,b,c = f.readline().strip().split(' ')
    nMeals.append(a)
    goalQuality.append(b)
    time.append(c)
f.close()
# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
 






