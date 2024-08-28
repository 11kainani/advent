
source = ["467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."]

def numberInLine(current: str):
    ""
    index = 0
    number = {}
    while index < len(current):
        element = current[index] 
        offset = 0
        if element.isnumeric():
            while current[index+offset].isnumeric(): 
                offset =offset + 1
            number[index] = offset
        index = index + offset + 1

    return (number)

       
def surroundings(index_start: int,offset: int,line: str): 
    """_summary_

    Args:
         index_start (int): start of the number
        offset (int): [O:+inf] number of digits in the int
        line (str): string to analyze

    Returns:
        _type_: _description_
    """
    
    if index_start == 0:
        index = index_start
    else: 
        index = index_start -1
        
    if index_start >= len(line) -1 or index_start == 0:
        index_end = offset
    else: 
        index_end = 1 + offset

    # +1 because --> string[start:end]: Get all characters from start to end - 1
    total_offset = index + index_end + 1

    return(line[index:total_offset])
       

def isPart(line:str):
    ""
    for c in line:
        if c.isnumeric() == False and c != ".":
            return True
    return False

def exam_line(previous:str, current:str,next:str) -> bool:
    ""
    return any(isPart(part) for part in [previous, current, next] if part)

def solve(source:list):
    ""
    for index in range(len(source)):
         current = source[index]
        
        # Check if the current element contains a numeric character
         if any(c.isnumeric() for c in current):
            previous = source[index - 1] if index > 0 else ""  # Edge case for the first line
            next_item = source[index + 1] if index < len(source) - 1 else ""  # Edge case for the last line

            dict_numbers = (numberInLine(current))
            for dict_index, number_offset in dict_numbers.items():
                ""
                
                
            print(current)
            print(exam_line(previous, current, next_item))

        
        
    
numberInLine("..35..633.")
surroundings(9,1,"..35..633.")
solve(source)