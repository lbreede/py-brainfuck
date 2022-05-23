def increment_val(array, ptr):
    array[ptr] = min(array[ptr] + 1, 255)

def decrement_val(array, ptr):
    array[ptr] = max(array[ptr] - 1, 0)

def loop_end(array, ptr, start, i):
    if array[ptr] == 0:
        return -1, i
    return start, start

def unfuck(cmd, array_length=4):
    i = 0
    ptr = 0
    array = [0] * array_length
    start = None
    output = ""

    while i < len(cmd):
        match cmd[i]:
            case ">": ptr += 1
            case "<": ptr -= 1
            case "+": increment_val(array, ptr)
            case "-": decrement_val(array, ptr)
            case "[": start = i
            case "]": start, i = loop_end(array, ptr, start, i)
            case ".": output += str(chr(array[ptr]))
            case ",": pass
            case _: pass
        i += 1
    return output


def main():

    with open("hello_world.bf") as f:
        brainfuck = f.read()

    output = unfuck(brainfuck)
    print(output)

if __name__ == '__main__':
    main()
    
