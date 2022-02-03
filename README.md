# Docker  
## Comandos Básicos  
***
```
docker run IMAGEM = cria um container rodando a imagem local ou do HUB
docker run IMAGEM npm start = cria um container rodando a imagem local ou do HUB e já o starta
docker run IMAGEM -w "PASTA DO CONTAINER" npm start = cria um container rodando a imagem local ou do HUB e já o starta dentro da pasta especificada
docker run -it IMAGEM = criar container e entra nele
docker run -d IMAGEM = criar container e roda sem travar o cmd
docker run -d -P IMAGEM = criar container, roda sem travar o cmd e atribi portas para falar com o host
docker run -d -P --name NOME_QUE_EU_QUERO IMAGEM = criar container, roda sem travar o cmd e atribi portas para falar com o host
docker run -d -p PORTA:80 IMAGEM = criar container, roda sem travar o cmd e atribi a uma porta específica
docker ps = containers ativo
docker ps -a = containers inativos
docker ps -q = somente o ID do containers ativos
docker start NOME = starta container parado
docker stop -t 0 NOME = para o container
docker stop -t 0 $(docker ps -q) = ele para os nomes que retornam do "docker ps -q"
docker start -a -i NOME = starta container parado e entra nele
docker container prune = encerra todos os container parados
docker rmi IMAGEM = apaga a imagem
docker port NOME = verificar a que porta ele ta ligada
docker run -d -it -v "C:\Users\De Lucca\Desktop:/var/www" IMAGEM = Informação do \www vai pro meu Desktop
docker inspect NOME = informações do docker
```

## Imagens

dockersamples/static-site  
hello-world  
ubuntu  