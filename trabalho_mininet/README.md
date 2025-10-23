# Trabalho Mininet
1. Com uso de linha de comando padrão do Mininet, crie a
topologia considerando o endereçoo MAC padronizado, larguras
de banda bw de 25Mbps e controlador do Mininet (não 
precisa especificar):

```
sudo mn -c
sudo mn --topo=linear,6 --link tc,bw=25 --mac
```

sudo mn -c:
> limpa a última conexão, limpando o cache junto

sudo mn --topo=linear,6 --link tc,bw25 --mac:
> cria uma topologia com 6 switches e largura de banda de 25Mb, além de fixar os endereços MAC
 
Inspecione informa¸c˜oes das interfaces, endere¸cos MAC, IP e
portas atrav´es de linhas de comando:
dump
nodes
net
h1 ifconfig -a
h2 ifconfig -a
h3 ifconfig -a
h4 ifconfig -a
h5 ifconfig -a
h6 ifconfig -a

Execute testes de ping entre os diferentes nós:
h1 ping h6
pingall

Especifique que o host 1 na porta 5555 vai ser um servidor
TCP e o host 2 um cliente e execute testes de iperf, considere
um relat´orio por segundo com teste de 15 segundos.
xterm h1 h2
Em h1 (servidor):
	iperf -s -p 5555
Em h2 (cliente):
	iperf -c 10.0.0.1 -p 5555 -i 1 -t 15
