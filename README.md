# Dissertação 

Esta dissertação apresenta uma solução de atenção domiciliar à saúde 
automatizada com recursos da TV Digital (*Set-top Box*) e tecnologia
de Internet das Coisas (IoT - *Internet of Things*)
## TODO

- [x] [baixa] ~~terminar seção 'estrutura da dissertação' @cap-1 :grin:~~ [10/06/2017]
- [x] [média] ~~incrementar seção de 'IoT' @cap-2 :cold_sweat:~~ [03/06/2017] 
- [ ] [alta] reformular seção de OpenIoT @cap-2 :cry: 
- [ ] [média] refazer imagem da seção 4.1 (descrição de cenários) @cap-4 :cold_sweat: 
- [x] [:cry: alta] ~~descrever simulações para os ambientes da seção 4.1 (descrição de cenários) @cap-4~~ [30/04/2017]
- [x] [:cry: alta] ~~descrever solução (seção 4.2) @cap-4~~ [03/06/2017]
- [x] [média] ~~realocar seção 4.4 (cenários de uso) @cap-4 :cold_sweat:~~ [30/04/2017]
- [x] [média] ~~especificar formalmente módulo notification @cap-5 :cold_sweat:~~ [09/05/2017]
- [x] [média] ~~especificar formalmente módulo dado @cap-5 :cold_sweat:~~ [09/05/2017]
- [x] [média] ~~especificar formalmente módulo panicbutton @cap-5 :cold_sweat:~~ [10/05/2017]
- [x] [média] ~~especificar formalmente módulo web @cap-5 :cold_sweat:~~ [03/06/2017]
- [ ] [baixa] desenvolver parte de IoT do sistema @cap-5 :grin: 
- [x] [baixa] ~~escrever capítulo 6 (conclusão) @cap-6 :grin:~~ [10/06/2017]
- [x] [baixa] ~~escrever capítulo 3 (trabalhos relacionados) @cap-3 :grin:~~ [03/06/2017]
- [x] [:cry: alta] ~~realizar comparativo entre arquiteturas (fazer tabela 
comparativa) @cap-4 ou @cap-3~~ [10/06/2017]

### sugestões - 11/06/2017

* o que tem de internet das coisas na proposta?!
* ~~colocar simulações dentro dos ambientes.~~
* falar de internet das coisas na descrição dos cenários.
* ~~colocar 2 ou 3 páginas de internet das coisas.~~
* ~~juntar plataforma openIoT da seção IoT~~
* colocar na conclusão 
* ~~na fundamentação teórica, aspectos de saúde trocar por assistência domiciliar~~
* na fundamentação teórica, aplicações sensíveis ao contexto
* ta faltando um 4.4? Como a IoT incluenciaria 
* eu coloquei internet das coisas pra fortalecer o ambiente, isso está faltando
na dissertação.
* o que a figura 4 está fazendo aí? O que ela significa pra sua proposta?
* qual seria a arquitetura para ADS baseada em internet das coisas

## Facilitadores

Facilitadores são comandos que facilitam o uso de outros comandos. Como por exemplo, a inclusão de imagens. Dois comandos foram criados para simplificar essa inclusão. Os comandos são
`\figurasimples` e `\figuradupla`.

O comando `\figurasimples` recebe 3 parâmetros. 

```latex
% sintaxe:
\figurasimples{nome-do-arquivo}{Legenda da imagem sem fonte}{tamanho}
ou
\figurasimples[chave-da-fonte]{nome-do-arquivo}{Legenda da imagem com fonte}{tamanho}

% exemplo: figura sem fonte:
\figurasimples{logo-ifce-sem-nome}{Logotipo do IFCE sem nome}{4cm}

% exemplo: figura com fonte:
\figurasimples[talbot2012]{logo-ifce-sem-nome}{Logotipo do IFCE sem nome}{4cm}
```

O comando `\figuradupla` recebe 4 parâmetros.
```
% sintaxe:
\figuradupla{nome-do-arquivo-1}{Legenda da imagem 1}
{nome-do-arquivo-2}{Legenda da imagem 2}

% exemplo:
\figuradupla{logo-ifce-sem-nome}{Logotipo do IFCE sem nome}
{logo-ifce-padrao}{Logotipo do IFCE padrão}
```

As tabelas devem ser salvas no diretório `tabelas` e para adicionar uma tabela, basta inserir o comando 
```latex
% sintaxe:
\tabela{nome-do-arquivo}{Título da tabela sem fonte}{escala-da-fonte}
ou
\tabela[chave-da-fonte]{nome-do-arquivo}{Título da tabela com fonte}{escala-da-fonte}

% exemplo: tabela sem fonte:
\tabela{tabela-exemplo}{Lista de bases de dados usados nesse trabalho}{1}

% exemplo: tabela com fonte:
\tabela[talbot2012]{funcoes-de-kernel}{Funções de kernel}{0.9}
```
O arquivo de tabela deve conter apenas o ambiente `tabular` (verificar o exemplo contido no modelo).
