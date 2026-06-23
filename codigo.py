class Node:
    __slots__ = ("left", "right", "content")

    def __init__(self, content: str):
        self.left = None
        self.right = None
        self.content = content


class Tree:

    def __init__(self):
        self.root = None

    def add(self, content: str):
        if not self.root:
            self.root = Node(content)
            return

        cur = self.root
        while True:
            if content > cur.content:
                if not cur.right:
                    cur.right = Node(content)
                    return
                cur = cur.right
            else:
                if not cur.left:
                    cur.left = Node(content)
                    return
                cur = cur.left

    def search(self, protocol: str):
        cur = self.root
        while cur:
            if cur.content.startswith(protocol):
                return cur.content
            cur = cur.right if protocol > cur.content else cur.left
        return None

    def remove(self, content: str):
        self.root = self._remove_node(self.root, content)

    def _remove_node(self, root, content: str):
        if not root:
            return None

        if content < root.content:
            root.left = self._remove_node(root.left, content)
            return root
        if content > root.content:
            root.right = self._remove_node(root.right, content)
            return root

      
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        
        sub = root.right
        while sub.left:
            sub = sub.left
            
        root.content = sub.content
        root.right = self._remove_node(root.right, sub.content)
        return root

    def in_order(self):
        def walk(n):
            if n:
                yield from walk(n.left)
                yield n.content
                yield from walk(n.right)
        return walk(self.root)


def menu():
    airport_tree = Tree()

   
    for item in ["1024 - Celular iPhone", "0512 - Carteira de Couro", "2048 - Mochila Preta", "0256 - Chave de Carro"]:
        airport_tree.add(item)

    while True:
        print("\n" + "=" * 45)
        print("  AEROPORTO - SISTEMA DE ACHADOS E PERDIDOS  ")
        print("=" * 45)
        print("1. Registrar Novo Item Encontrado")
        print("2. Buscar Item por Protocolo")
        print("3. Dar Baixa (Devolver Item ao Dono)")
        print("4. Listar Todos os Itens Pendentes")
        print("0. Sair")
        print("=" * 45)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("\nEncerrando o sistema de Achados e Perdidos. Até logo!")
            break

        if opcao == "1":
            protocolo = input("Digite o protocolo (ex: 0500): ").strip()
            descricao = input("Descrição do item (ex: Notebook Dell): ").strip()
            airport_tree.add(f"{protocolo} - {descricao}")
            print("\n[Sucesso] Item registrado no sistema!")

        elif opcao in ("2", "3"):
            msg = "para busca" if opcao == "2" else "a ser retirado"
            protocolo = input(f"Digite o protocolo do item {msg}: ").strip()
            item_completo = airport_tree.search(protocolo)

            if item_completo:
                if opcao == "2":
                    print(f"\n[Item Localizado]: {item_completo}")
                else:
                    airport_tree.remove(item_completo)
                    print("\n[Sucesso] Item retirado/devolvido com sucesso!")
            else:
                print("\n[Aviso/Erro] Protocolo não encontrado ou inválido.")

        elif opcao == "4":
            print("\n--- ITENS PENDENTES NO DEPÓSITO (ORDEM DE PROTOCOLO) ---")
            itens = list(airport_tree.in_order())
            if not itens:
                print("O depósito está totalmente vazio.")
            else:
                for item in itens:
                    print(f" > {item}")
        else:
            print("\n[Erro] Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
