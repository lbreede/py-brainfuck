def increment_val(array: list[int], ptr: int) -> None:
    array[ptr] = min(array[ptr] + 1, 255)

def decrement_val(array: list[int], ptr: int) -> None:
    array[ptr] = max(array[ptr] - 1, 0)

def loop_end(array: list[int], ptr: int, start: list[int], i: int) -> int:
    if array[ptr] == 0:
        start.pop()
        return i
    return start[-1]

def unfuck(cmd: str, array_length: int = 4) -> str:
    i = 0
    ptr = 0
    array = [0] * array_length
    start = []
    output = ""

    while i < len(cmd):
        match cmd[i]:
            case ">": ptr += 1
            case "<": ptr -= 1
            case "+": increment_val(array, ptr)
            case "-": decrement_val(array, ptr)
            case "[": start.append(i)
            case "]": i = loop_end(array, ptr, start, i)
            case ".": output += str(chr(array[ptr]))
            case ",": pass
            case _: pass
        i += 1
    return output


def main():

    with open("hello_world.bf") as f:
        brainfuck = f.read()

    output = unfuck(brainfuck, array_length=8)
    print(output)

if __name__ == '__main__':
    main()
    
