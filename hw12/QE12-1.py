import sys

file = open("TBG_records.csv")
table = file.read()
file.close()

table = table.split("\n")
#print(table)

team = input("Which team would you like to check (Brothers, Guardians, Lamigo, Unilions)?") 
#print("team : ",team)
if team != "Brothers" and team != "Guardians" and team != "Lamigo" and team != "Unilions" :
    print()
    print("Error: invalid team name.")
    quit()
ID = int(input("Game ID = ?"))
#print("ID : ",ID)
if ID < 1 or ID >334 :
    print()
    print("Error: invalid game id.")
    quit()
#print(len(table))
for i in range(1 , 335) :
    race = table[i].split(",")
    #race = i
    if int(race[0]) == ID:
        #print(race)
        if race[4] == team :
            opponent = race[5]
            if int(race[1]) > 0 :
                won = True
            else:
                won = False
        elif race[5] == team :
            opponent = race[4]
            print("test")
            if int(race[1]) > 0 :
                won = False
            else:
                won = True
        else:
            print("Team '", team,"' did not participate in game ", ID)
            #stop()
            quit()
        
        print("Game", "\t", "Opponent", "\t", "Won")
        print("================================")
        print(ID, "\t", opponent, "\t", won)
        print()
        print("----------- History -----------")
        count = 0
        for j in range(int(ID) - 1, 0 ,-1):
            if count == 3:
                break
            other_race = table[j].split(",")
            if other_race[4] == team :
                count = count + 1
                opponent_other = other_race[5]
                if int(other_race[1]) > 0 :
                    won_other = True
                else:
                    won_other = False
                print(j, "\t", opponent_other, "\t", won_other)
            elif other_race[5] == team :
                count = count + 1
                opponent_other = other_race[4]
                if int(other_race[1]) > 0 :
                    won_other = False
                else:
                    won_other = True
                print(j, "\t", opponent_other, "\t", won_other)
        print()
        print("End.")
            



    #print()
    #print(race[0])
