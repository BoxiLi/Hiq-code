mapper = '3\n1,2\n2,3'

def read_mapper(mapper):
        mapper0 = mapper.split('\n')
        connection = []
        for i in range(len(mapper0)):
                print(mapper0[i].split(','))
                mapper1 = mapper0[i].split(',')
                List = []
                for j in range(len(mapper1)):
                        print(len(mapper1))
                        List.append(int(mapper1[j]))
                        print(List)
                print('')
                if len(List) == 1:
                        n = List[0]
                if len(List) == 2:
                        connection.append((List[0],List[1]))
        return n,connection

mapper = "5\n0,1\n1,2\n1,3\n2,3\n2,4\n3,4"
print(read_mapper(mapper))