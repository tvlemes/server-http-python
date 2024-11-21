import http.server
import socketserver
import os

# Defina o diretório onde os arquivos serão servidos
diretorio = "C:\\Users\\Thiago\\Desktop\\html_esp32"  # Substitua pelo diretório que você quer
if not os.path.exists(diretorio):
    raise FileNotFoundError(f"O diretório especificado não existe: {diretorio}")

# Mude para o diretório especificado
os.chdir(diretorio)

# Defina a porta e o IP que o servidor vai escutar
ip = "192.168.0.21"
porta = 8000

# Crie o manipulador de requisições HTTP
Handler = http.server.SimpleHTTPRequestHandler
Handler.directory = diretorio

# Crie o servidor
with socketserver.TCPServer((ip, porta), Handler) as httpd:
    print(f"Servidor iniciado em http://{ip}:{porta}")
    httpd.serve_forever()
