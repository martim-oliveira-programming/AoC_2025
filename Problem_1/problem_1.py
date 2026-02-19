def read_file(file_name: str, mode: str) -> list[str]:
    with open(file_name, mode) as file:
        lines = file.readlines()
    return [line.strip() for line in lines]  # removes trailing '\n'


def command_to_int(command: str)->int:
    if command == "R":
        return 1
    elif command == "L":
        return -1
    else:
        raise ValueError("Invalid command")

def parser()->list[int]:
    lines = read_file("rotations.txt","r")
    rotations = []
    for i in lines:
        command = i[0]
        command = command_to_int(command) 
        number = int(i[1:])
        rotation = command * number
        rotations.append(rotation)
    
    return rotations

def next_dial(dial:int,rotation:int)->int:
    dial = (dial + rotation) % 100
    return dial

def part_1_calculation(dial:int,rotation:int)->int:
    if dial == 0:
        return 1
    return 0

def main(problem_number: int = 1) -> int:
    dial = 50 #Dial starts set to 50 and goes 0-99 in a circular way
    password = 0
    rotation_list = parser()
    
    for rotation in rotation_list:
        if problem_number == 1:
            dial = next_dial(dial,rotation)
            password += part_1_calculation(dial,rotation)
        else:
            step = 1 if rotation > 0 else -1
            for _ in range(abs(rotation)):
                dial = (dial + step) % 100
                if dial == 0:
                    password += 1

    return password

print(main(1))
print(main(2))
