# Lista de exercícios 1

## 1 - Explique o conceito de Web Service segundo a definição da Gartner.
Web Services são componentes de software com baixo fator de acoplamento, utilizados por meio de padrões de tecnologia Internet. Eles são projetados para
suportar a interação de máquina a máquina interoperável por meio de uma rede utilizando protocolos de internet (HTTP, por exemplo). Um Web Service representa uma função de negócio ou um serviço que pode ser acessado por uma outra aplicação.

## 2 - Explique a função do protocolo SOAP e descreva a composição de seu envelope.
O Simple Object Access Protocol (SOAP) é um padrão da indústria para troca de informações entre serviços distribuídos e serviços web utilizando o formato XML para transmitir mensagens.
O envelope SOAP é descrito em duas partes: header (cabeçalho) e body (corpo). O primeiro contém os metadados, ou seja, parâmetros de controle, como autenticação e roteamento. O segundo é a mensagem em si, contendo os dados que serão transmitidos.

## 3 - Quais são os três elementos principais de uma arquitetura de Web Service?
A arquitetura de um Web Service é composta de três elementos essenciais: Registro de Serviço, Fornecedor de Serviço e Solicitação do Serviço.

## 4 - O que é WSDL e quais são os elementos básicos que o compõem? 
WSDL é um padrão baseado em XML que descreve um serviço web. Ele funciona como um contrato, detalhando as operações disponíveis, quais os parâmetros e tipo de dados de cada parâmetro são esperados, e qual o tipo de dado do retorno será enviado como resposta.
Os elementos básicos que compões um são: types, message, portType, binding, operation e definitions.

## 5 - Qual é a função do UDDI em Web Services?
O Universal Discovery Description and Integration são identificadores utilizados para identificação de recursos e serviços de um Web Service, facilitando o processo de integração de serviços antigos quanto na busca de recursos.

## 6 - O que é REST e quem o criou?
Representational State Transfer é um conjunto de regras que permitem a criação de um projeto com interfaces bem definidas. Permite também que diferentes protocolos sejam utilizados para troca de mensagens. Utiliza as funções padrão do HTTP. Criado por Roy Fielding em 2000.

## 7 - Qual é a função de um recurso (Resource) no REST e como ele é identificado?
Um recurso é qualquer coisa importante o suficiente para ser referenciado com um nome. Um URI (Universal Resource Identifier) é utilizado para identificar o recurso. Sendo assim, um recurso é qualquer coisa que possa ter uma URI.

## 8 - O que é virtualização e quais são seus principais tipos de recursos virtualizados?
A virtualização de software é a criação de versões virtuais de recursos de hardware físico (servidores, redes, armazenamento) através de um software, permitindo que várias máquinas virtuais (VMs) funcionem sobre um único sistema físico. Os principais tipos de recursos virtualizados são: aplicativos virtuais, servidores, armazenamento, redes.

## 9 - O que é um container Docker e o que ele empacota?
Um contêiner é uma unidade padrão de software que empacota o código e todas as suas dependências para que o aplicativo seja executado de forma rápida e confiável de um ambiente de computação para outro.
     
