import sys

def fizzbuzz(arg_arr):
    result = []
    
    run_len = int(arg_arr[1])
    
    argdict = dict()
    
    for i in range(2, len(arg_arr), 2):
        argdict.update({int(arg_arr[i]): arg_arr[i + 1]})
        
    for i in range(1, run_len + 1):
        bleh = str(i)
        
        for a in argdict:
            if i % a == 0:
                bleh += " " + argdict[a]
        result.append(bleh)
    return result

if __name__ == "__main__":
    args = sys.argv
    while len(args) <= 1:
        print("Not enough arguments.")
        args = sys.argv

    ans = fizzbuzz(args)
    for a in ans:
        print(a + " ")