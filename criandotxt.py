arquivo = open("arquivo.txt", "w")

arquivo.write("Essa é a primeira linha escrita por nós. \n")
arquivo.write("Essa é a nossa segunda linha.")
arquivo.write("Essa deveria ser a terceira linha porém ainda é a segunda. \n")
arquivo.write("Essa sim é a terceira. \n")
arquivo.write("ultima linha")

arquivo.close()


nome = "lucas"

arquivo = open("teste.txt" , "w")
arquivo.write(nome)

arquivo.close()