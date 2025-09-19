# Lista de exercícios 2

## 1 - Diferencie NFV e SDN, destacando suas origens e objetivos principais
NFV (Network Function Visualization) é a redefinição da arquitetura de equipamentos de rede. Nasceu para atender às necessidades dos provedores de internet. Seu objetivo é reduzir custos com hardware, aumentar flexibilidade e acelerar a implantação de serviços de rede.
SDN (Software Defined Network) é uma redefiniçãoao da arquitetura de rede, vindo do mundo da TI, separando o plano de controle do plano de dados. Seu objetivo é automatizar, orquestrar e dar visibilidade/controle programável à rede.

## 2 - Cite dois benefícios da NFV para provedores de serviços
Redução dos custos operacionais e despesas de capital. Reduzir a escala, a diversidade e o custo do hardware apenas para o necessário.

## 3 - Quais são as três camadas principais da arquitetura NFV? Explique brevemente cada uma
NFVI - A infraestrutura física e virtual onde as funções de rede rodam.
VNFs - As funções de rede implementadas em software que antes rodavam em hardware dedicado.
MANO - O conjunto de blocos responsáveis por gerenciar todo o ciclo de vida das VNFs e da infraestrutura.

## 4 - Aponte duas dificuldades enfrentadas pela rede tradicional que o SDN busca superar
Em redes tradicionais, cada switch e roteador precisa ser configurado individualmente. O SND centraliza o controle em um controlador programável, que aplica políticas automaticamente em toda a rede.
A rede tradicional depende fortemente do plano de controle distribuído embutido nos dispositivos, dificultando mudanças dinâmicas. O SDN separa plano de controle e plano de dados, permitindo reprogramar rotas e políticas em tempo real conforme aplicações e serviços demandam.

## 5 - Como o NFV pode reduzir custos para pequenas empresas que precisam de funções de rede sob demanda? 
Elimina hardware proprietário caro.
O consumo depende do uso. As funções de redes são ativadas apenas quando necessário.
Escalabilidade e flexibilidade sem troca de hardware

## 6 - Faça uma pesquisa pequena de um exemplo real de empresas ou operadoras que utilizam NFV e descreva seus benefícios.
A Vodafone implantou a infraestrutura virtual de rede da VMware (telco cloud) em seus 21 mercados europeus. Como benefícios:
Redução de custos das funções de rede de núcleo em, aproximadamente, 50%;
Aumento na velocidade de lançamento de novas funções/políticas;
Padronização da arquitetura de rede na Europa, o que facilita manutenção, automação e interoperabilidade;
