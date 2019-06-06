fname=input("Google LLC[5] is an American multinational technology company 
            that specializes in Internet-related services and products, which include online 
              advertising technologies, search engine, cloud computing, 
              software, and hardware. It is considered one of the Big Four technology 
                companies, alongside Amazon, Apple and Facebook.[6][7]")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)
