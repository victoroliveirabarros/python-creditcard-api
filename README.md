
# Python Credit Card API
Projeto desenvolvido como desafio técnico para a MAISTODOS.

## Rodando o projeto localmente
#### Dependências para rodar o projeto local

- docker
- docker compose

Para iniciar o projeto em modo desenvolvimento, execute:

```console
$ make dev-build
```
A primeira vez que o projeto for executado levará um tempo adicional para realizar o **pull** e **build** das imagens, nas execuções posteriores o tempo será menor. O projeto é iniciado em modo desenvolvimento, portanto, toda alteração no código resultará em um reload automático da aplicação.

Caso instale ou altere alguma dependência no `requirements.txt`, será necessário rebuildar o projeto, utilize:

```console
$ make dev-build
```

Ao executar o comando, você pode ver se o projeto está rodando com sucesso através da URL

```
http://localhost/docs
```

## Estilização do Projeto e checagem de erros
O projeto segue o padrão de estilização **PEP8** e **isort**, portanto, antes de qualquer commit, rode o comando: ```$ make format```

para ajustar a estilização.
```console
$ make format
```
para verificar se o projeto possui errors de sintaxe, executar:
```console
$ make check_errors
```
Você pode verificar se o código-fonte está de acordo com o padrão PEP8 através do comando:
```console
$ make check_format
```

## Testes Unitários

Para rodar os testes execute o comando:

```console
$ make test
```
A pasta de cobertura será criada com o nome ```htmlcov```.



## Estrutura de pastas e arquitetura

- A pasta ```development``` contém tudo que é necessário para rodar o projeto localmente, incluindo suas dependências locais.
- Na pasta ```app``` está contido o código-fonte da aplicação.

O projeto atual utilizada uma arquitetura baseada na Clean Architeture, do livro escrito por Uncle Bob.

![Alt text](docs/arquitetura-limpa.jpg "Clean Architeture")


### Main Layer
A camada main é a mais suja da aplicação. Para todas as camadas serem limpas e desaclopadas, alguma tem que pagar o pato e conhecer todo mundo.
Na camada Main são definidas todas as rotas da aplicação (utilizando o [Framework FastAPI](https://fastapi.tiangolo.com/)). Além disso, são utilizados os padrões de projeto [*composite*](https://en.wikipedia.org/wiki/Composite_pattern) e [*factory*](https://en.wikipedia.org/wiki/Factory_method_pattern#:~:text=In%20class%2Dbased%20programming%2C%20the,object%20that%20will%20be%20created.) para instanciar todos os objetos (objetos só são instanciados na camada main) da aplicação, injetando em seus construtures suas dependências, contemplando assim por tabela o padrão [*dependency injection*](https://en.wikipedia.org/wiki/Dependency_injection#:~:text=In%20software%20engineering%2C%20dependency%20injection,it%20depends%20on%2C%20called%20dependencies.&text=The%20intent%20behind%20dependency%20injection,increase%20readability%20and%20code%20reuse.).

Portanto, cada rota cria o conjunto de objetos necessários para execução do caso de uso e o chama utilizando o padrão [*adapter*](https://en.wikipedia.org/wiki/Adapter_pattern#:~:text=In%20software%20engineering%2C%20the%20adapter,be%20used%20as%20another%20interface.).

### Domain Layer
A camada de domínio não possui implementações lógicas. Nesta camada, estão presentes os **Models** da aplicação e as interfaces que representam cada caso de uso da aplicação. Se uma pessoa perguntar para o DEV: O que esse *software* faz? Basta olhar a camada de domínio, que conterá um arquivo com uma interface para cada caso de uso da aplicação, informando suas entradas e suas saídas. Essa interface então será implementada posteriormente na camada de serviço.

### Service Layer
A camada de serviço é onde está toda regra de negócio da aplicação. Aqui serão implementados os casos de uso, além de helpers enums e afins. Essa camada contém somente código Python puro, sem a utilização de bibliotecas externas. Caso necessidade acessar algo externo eg. um banco de dados, a implementação ocorrerá na camada de infra.

### Infra Layer
Aqui será implementado todo o código da aplicação que faz uso de alguma biblioteca. Por exemplo, utilizamos a biblioteca google-cloud-tasks para criar uma Task no Google. A implementação da função add_to_queue, que faz uso dessa biblioteca, será implementada na camada de infra e poderá ser acessada pela camada de serviço posteriormente.
