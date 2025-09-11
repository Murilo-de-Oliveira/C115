import socket
import json

# Questões no formato: { "pergunta": str, "opcoes": [str], "resposta": int (índice correto) }
questoes = [
    {
        "pergunta": "Qual é a capital da Itália?",
        "opcoes": ["Roma", "Paris", "Lisboa", "Londres"],
        "resposta": 0
    },
    {
        "pergunta": "Qual é o resultado de 7 * 8?",
        "opcoes": ["54", "56", "64", "72"],
        "resposta": 1
    }
]

HOST = "127.0.0.1"  # localhost
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((HOST, PORT)) #associação de socket com endereço e porta
        servidor.listen() #coloca o socket em modo espera
        print(f"Servidor aguardando conexões em {HOST}:{PORT}...")

        conn, addr = servidor.accept() #socket e endereço do cliente que se conectar
        with conn:
            print(f"Conectado por {addr}")

            try:
                conn.sendall(json.dumps(questoes).encode()) #envia as questões para o cliente

                data = conn.recv(1024).decode() #recebe respostas do cliente na forma de bytes
                respostas_cliente = json.loads(data) #converte para strings

                resultado = []
                acertos = 0
                for i, resp in enumerate(respostas_cliente):
                    correta = questoes[i]["resposta"]
                    if (resp-1) == correta:
                        resultado.append(f"Questão {i+1}: Correto")
                        acertos += 1
                    else:
                        resultado.append(f"Questão {i+1}: Errado (resposta correta: {questoes[i]['opcoes'][correta]})")

                resultado.append(f"Total de acertos: {acertos}/{len(questoes)}")

                conn.sendall(json.dumps(resultado).encode()) #envia resultado para o cliente
            
            except (ConnectionResetError, BrokenPipeError):
                    print(f"Cliente {addr} desconectou inesperadamente.")

if __name__ == "__main__":
    main()
