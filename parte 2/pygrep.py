import sys
import io
import os

def search_file(filePath):
    with io.open(filePath) as file:
        if searchString in file.read():
            print("Texto encontrado no arquivo localizado em:", filePath)

def search_folder(folderPath):
    with os.scandir(folderPath) as entries:
        for entry in entries:
            if entry.is_file():
                search_file(entry.path)
            if entry.is_dir():
                search_folder(entry.path)

argv_len = len(sys.argv)

if argv_len > 3:
    searchString = sys.argv[1]
    searchType = sys.argv[2]
    path = sys.argv[3]
else:
	sys.exit("Argumentos inválidos. Utilize string_de_busca tipo_de_busca(arquivo/pasta) caminho.")

if searchType == 'arquivo':
    search_file(path)
elif searchType == 'pasta':
    search_folder(path)
else:
    sys.exit("Tipo de busca não reconhecido pelo sistema, utilize arquivo ou pasta.")