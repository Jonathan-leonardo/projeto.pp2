contacts = []
cid = 1

def find_contact(id_):
    return next((c for c in contacts if c['id'] == id_), None)

def menu():
    print('''\n1 - Inserir Contato
2 - Alterar Contato
3 - Consultar Contatos
4 - Excluir Contato
0 - Sair\n''')

while True:
    menu()
    op = input("Opção: ")

    if op == '0':
        break

    elif op == '1':
        nome = input("Nome: ").strip()
        iphone = input("Telefone: ").strip()
        email = input("Email: ").strip()
        contacts.append({'id': cid, 'nome': nome, 'iphone': iphone, 'email': email})
        cid += 1
        print("Contato inserido.")

    elif op == '2':
        i = input("ID do contato para alterar: ").strip()
        if not i.isdigit():
            print("ID inválido.")
            continue
        i = int(i)
        c = find_contact(i)
        if c:
            n = input(f"Novo nome ({c['nome']}): ").strip()
            p = input(f"Novo telefone ({c['iphone']}): ").strip()
            e = input(f"Novo email ({c['email']}): ").strip()
            if n: c['nome'] = n
            if p: c['iphone'] = p
            if e: c['email'] = e
            print("Contato alterado.")
        else:
            print("Contato não encontrado.")

    elif op == '3':
        if not contacts:
            print("Nenhum contato cadastrado.")
            continue
        for c in contacts:
            print(f"{c['id']}: {c['nome']} | Tel: {c['iphone']} | Email: {c['email']}")

    elif op == '4':
        i = input("ID do contato para excluir: ").strip()
        if not i.isdigit():
            print("ID inválido.")
            continue
        i = int(i)
        c = find_contact(i)
        if c:
            contacts = [x for x in contacts if x['id'] != i]
            print("Contato excluído.")
        else:
            print("Contato não encontrado.")

    else:
        print("Opção inválida!")
