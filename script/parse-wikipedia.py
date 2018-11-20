def parse_wikipedia():
    words = ""
    result = ""
    with open("data.txt") as f:
        for line in f:
            words = line.rstrip().split('||')
            result += '<word src="'+ words[1].lstrip().rstrip() + '">'+ words[0].rstrip() +'</word>\n'

    print(result)
    file = open("hasil.xml","w")
    file.write(result)
    file.close()

parse_wikipedia()
