Discord Dota
============

## 📝 Description

Bot do Discord para exibir informações dos heróis

## 📂 Hierarquia de diretórios

- **/code** diretório onde esta os arquivos do projeto;
  - **./requirements.txt** arquivo de dependências;
  - **/app** diretório onde os arquivos do desenvolvimento ficam localizados;
     - **/configuration** diretório onde centraliza configurações importantes ficam localizadas;
    - **/spiders** diretório onde os crawlers estão localizados;
    - **./Bot.py** aquivo principal do Bot;
    - **./__init__.py** arquivo inicial para executar o Bot;
    - **./runner.py** arquivo configurado para executar um crawler;

## 📄 Pré-requisitos

- [Python 3.7](https://www.python.org/)
- [pip](https://pypi.org/)

## 👨‍💻 Usando
Configure a variavel de ambiente **DISCORD_BOT_KEY** com a chave do bot ou diretamente no arquivo *./code/app/configuration/configuration.py* na variável **self.DISCORD_BOT_KEY**

### 💻 Sem Docker
No diretorio code, instale as dependências
```bash
pip3 install -r requirements.txt
```
Na pasta code/app, execute
```bash
python3 __init__.py
```

### 🐋 Com Docker
Na pasta /code, gere a build da imagem Docker
```bash
# docker image build -t <IMAGE_NAME> <DOCKERFILE_DIRECTORY>
docker image build -t <IMAGE_NAME> .
```
Agora execute o container utilizando a imagem
```bash
#  docker run <IMAGE_NAME>
docker run <IMAGE_NAME>
```

### 🐳 Com Docker Compose
Na raiz do projeto adicione o arquivo .env com a variável **DISCORD_BOT_KEY**   
Execute docker-compose
```bash
docker-compose up --build
````

## 💬  Variáveis de Ambiente
- **DISCORD_BOT_KEY** variável com a chave do bot

## 🛠 Criado com

- [Discord.py](https://discordpy.readthedocs.io/en/latest/)
- [Scrapy](https://scrapy.org/)

## 👥 Autores
- [Wesley Adriann](https://github.com/WesleyAdriann/discord_bot_dota/commits?author=WesleyAdriann)
  - Github: [wesleyadriann](https://github.com/WesleyAdriann)
  - LinkedIn: [in/wesleyadriann](https://www.linkedin.com/in/wesleyadriann/)

## ↪ Status do projeto

- **Em Desenvolvimento**

## 📍 URL do Projeto

- [https://github.com/WesleyAdriann/discord_bot_dota](https://github.com/WesleyAdriann/discord_bot_dota)
