
def dts(decimal):
    if decimal:
        rem = (decimal+2) % 5
        div = (decimal+2) // 5
        return dts(div) + '=-012'[rem]
    else:
        return ''
        

def sum_snafu(d):
    summ = 0
    for number in d:
        decimal = 0
        for power, digit in enumerate(reversed(number)):
            match digit:
                case "=": val = -2
                case "-": val = -1
                case "0": val =  0
                case "1": val =  1
                case "2": val =  2
            decimal += 5**power * val
        summ += decimal
    return summ

d = open("25").read().split("\n")

print(dts(sum_snafu(d)))
