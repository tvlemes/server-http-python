# Server HTTP Python



[![NPM](https://img.shields.io/github/license/tvlemes/project-web-scraping)](https://github.com/tvlemes/project-web-scraping/blob/main/LICENSE)

<!-- TABLE OF CONTENTS --> 
<details open="open">
  <summary>Indície</summary>
  <ol>
    <li>
      <a href="#objetivo">Objetivo</a>
    </li>
    <li>
      <a href="#bibliotecas">Bibliotecas utilizadas</a>
    </li>
    <li>
      <a href="#pastas-e-arquivos">Pastas e Arquivos</a>
    </li>
    <li>
      <a href="#configurações">Configurações</a>
    </li>
    <li>
      <a href="#rodar-o-server">Rodar o Server</a>
    </li>
    <li>
      <a href="#sobre">Sobre</a>
    </li>
  </ol>
</details>

## Objetivo
Este projeto é parte integrante do <b>Projeto ESP32 com PlatformIO no VSCode</b>.

Ele tem por finalidade servir as páginas <b>HTML</b> para o <b>ESP32</b> em um servidor <b>on-primesse</b>.

<!-- bibliotecas -->
## Bibliotecas
Foram utilizadas as seguintes bibliotecas:
* http.server
* socketserver

<!-- arquivos-e-pastas -->
## Pastas e Arquivos
A pasta que contém os arquivos <b>HTML</b> está localizado na variável <b>diretorio</b>:

```
...
# Defina o diretório onde os arquivos serão servidos
diretorio = "diretório_arquivos_html"  
...
```
Ex.: ```diretorio = "C:\\Users\\Usuário\\\Desktop\\html_esp32"```

O arquivo <b>server.py</b> é o arquivo principal que roda o Server.

<!-- configurações -->
## Configurações
As configurações do <b>IP</b> e <b>Porta</b> que o Server rodará está localizado nas variáveis <b>ip</b> e <b>porta</b>.

```
...
# Defina a porta e o IP que o servidor vai escutar
ip = "192.168.0.21"
porta = 8000
...
```

<!-- rodar-o-server -->
## Rodar o Server
Para rodar o Server execute o comando no terminal dentro da pasta do mesmo:
```
$ python server.py
```

<!-- sobre -->
## Sobre

Autor: Thiago Vilarinho Lemes <br>
LinkedIn <a href="https://www.linkedin.com/in/thiago-v-lemes-b1232727" target="_blank">Thiago Lemes</a><br>
Home <a href="http://thiagolemes.free.nf" target="_blank">Thiago Vilarinho Lemes</a><br>
e-mail: contatothiagolemes@gmail.com | lemes_vilarinho@yahoo.com.br