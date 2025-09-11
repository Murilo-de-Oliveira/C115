import socket
import json

HOST = "127.0.0.1"
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        try:
            cliente.connect((HOST, PORT)) #conecta cliente ao servidor

            data = cliente.recv(4096).decode() #recebe questões do servidor na forma de bytes e converte
            questoes = json.loads(data) #monta o json para exibir as perguntas

            respostas = []
            for i, q in enumerate(questoes):
                print(f"\nQuestão {i+1}: {q['pergunta']}")
                for j, opcao in enumerate(q["opcoes"]):
                    print(f"  {j + 1} - {opcao}")
                
                resp = int(input("Sua resposta (número): "))
                respostas.append(resp)

            cliente.sendall(json.dumps(respostas).encode())  #envia respostas para o servidor

            resultado = json.loads(cliente.recv(4096).decode()) #recebe resultado do servidor
            print("\n--- Resultado ---")
            for linha in resultado:
                print(linha)
        except (ConnectionError, BrokenPipeError):
            print(f"Servidor não respondeu.")

if __name__ == "__main__":
    main()
