dataset = open("day2/input.txt").readlines()

dict = {}
for line in dataset: 
    number = line.find(":")
    dict[line[:number].strip()] = line[number+1:].strip()

dices = ["blue","green","red"]

def compare_to_threshold(color_counter):
    thresholds = {"blue":14,"green":13,"red":12}
    for key, data in color_counter.items():
        if thresholds[key] < int(data):
            return False
    return True

def check_falsehood(list):
    for item in list:
        if item == False:
            return False
    return True

games_results = {}        

for index , data in dict.items():
    division = data.split(";")
    correct_games = []
    for turn in division : 
        colors = turn.split(",")
        color_counter = dict.fromkeys(["blue","green","red"],0)
        
        for item in colors:
            item = item.replace(" ","")
            for dice in dices:
                results = item.find(dice)
                if results != -1:
                    color_counter[dice] = item[:results]
        #print(color_counter)
        correct_games.append(compare_to_threshold(color_counter))
    games_results[index.replace("Game","").strip()] = check_falsehood(correct_games)
            
filtered_dict = {k: v for k, v in games_results.items() if v != False}

total_sum = 0
print(filtered_dict)
for key in filtered_dict.keys():
    if key.isdigit():
        total_sum += int(key)

print(total_sum)
