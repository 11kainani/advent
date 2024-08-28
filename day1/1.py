
p = open("day1/input.txt")
lines = p.readlines()

def first_solution(lines):
    
    summation = 0
    for line in lines:
        #print(line)
        line = replace_word_with_number(line)
        #print(line)
        numbers = []
        for value in line:
            if value.isdigit():
                numbers.append(value)
        results_number = numbers[0] + numbers[-1]
        #print(results_number)
        summation += int(results_number)
    return summation


numbers = {
    "five" :"5", 
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
    "zero" : "0",
    "one" : "1", 
    "two" : "2",
    "three" : "3",
    "four" : "4",
    
}

example = 'one'
def replace_word_with_number(line :str ):
    line_length = len(line)
    transformed_str = ""
    for i in range(line_length):
        transformed_str += line[i]
        for key, value in numbers.items(): 
            transformed_str = transformed_str.replace(key,value)
    return transformed_str

other_example = [
    "two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"
]


other = [
    "1abc2",
"pqr3stu8vwx",
"a1b2c3d4e5f",
"treb7uchet",
]



assert first_solution(other_example) == 281, "Algo failed"
assert first_solution(other) == 142, "Algo failed 1"
print(first_solution(lines))
