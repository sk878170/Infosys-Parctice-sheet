# While playing an RPG game, you were assigned to complete one of the hardest quests in this game. There are n monsters
# you'll need to defeat in this quest. Each monster i is described with two integer numbers - poweri and bonusi. To defeat this
# monster, you'll need at least poweri experience points. If you try fighting this monster without having enough experience
# points, you lose immediately. You will also gain bonusi experience points if you defeat this monster. You can defeat monsters in
# any order.

# The quest turned out to be very hard - you try to defeat the monsters but keep losing repeatedly. Your friend told you that this
# quest is impossible to complete. Knowing that, you're interested, what is the maximum possible number of monsters you can
# defeat?

no_of_monsters=int(input("No of monsters: "))
initial_exp=int(input("initial hp: "))
poweri=[]
bonusi=[]
for i in range(no_of_monsters):
  p=int(input("power of moster"))
  poweri.append(p)
for i in range(no_of_monsters):
  q=int(input("bonus"))
  bonusi.append(q)

level={}
count=0
for i in range(len(poweri)):
  level[poweri[i]]=bonusi[i]

sorted_array=sorted(poweri)

for i in sorted_array:
  if i<=initial_exp:
    initial_exp+=level[i]
    count+=1
    
  else:
    break

print(count)
    

# print(poweri)
# print(sorted_array)
# print(level)

  