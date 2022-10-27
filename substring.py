import textwrap

def wrap(string, max_width):
    if len(string) > 0 and len(string) < 1000 and max_width < len(string) and max_width > 0:
        vresult = ''
        while len(string)  > 0:
            if len(string) > max_width:
                vresult = vresult + string[0:max_width] + '\n'
                string = string[max_width:]
            else:
                vresult = vresult + string
                string = ''
        return(vresult)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)