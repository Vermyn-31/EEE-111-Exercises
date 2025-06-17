
def democker(in_text):
      # TODO: Write the expression inside the return statement below.
    #       Note that you are _required_ to only use one expression
    #       to parse the whole paragraph in `in_text`.
    return ('. '.join(list(a.lower().capitalize() for a in in_text.rstrip().lstrip().replace('. ','.').split('.'))))

def main():
    testcases = int(input().strip())

    for t in range(testcases):
        in_text = input()

        out_text = democker(in_text)

        print(f'Case #{t + 1}: {out_text}')

if __name__ == '__main__':
    main()

