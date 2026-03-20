import json
import os

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            return []
    return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)


def adicionar_tarefa(tarefas):
    titulo = input("Digite o nome da tarefa: ").strip()
    if not titulo:
        print("Título inválido.")
        return

    prioridade = input("Digite a prioridade (baixa/média/alta): ").strip().lower()
    if prioridade not in ["baixa", "média", "media", "alta"]:
        prioridade = "baixa"

    tarefa = {
        "titulo": titulo,
        "prioridade": prioridade,
        "concluida": False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n===== LISTA DE TAREFAS =====")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔" if tarefa["concluida"] else "✘"
        print(f"{i}. [{status}] {tarefa['titulo']} | Prioridade: {tarefa['prioridade']}")
    print()


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        indice = int(input("Digite o número da tarefa concluída: "))
        if 1 <= indice <= len(tarefas):
            tarefas[indice - 1]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        indice = int(input("Digite o número da tarefa que deseja remover: "))
        if 1 <= indice <= len(tarefas):
            removida = tarefas.pop(indice - 1)
            salvar_tarefas(tarefas)
            print(f"Tarefa '{removida['titulo']}' removida com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")


def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\n====== GERENCIADOR DE TAREFAS ======")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()