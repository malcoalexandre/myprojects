
def contato_inicial():
	rows, cols = int(input("Por favor digite o número de contatos que deseja adicionar: ")), 5
	
	contatos = []
	print(contatos)
	for i in range(rows):
		print("\nDigite os detalhes do contato %d na seguinte ordem:" % (i+1))
		print("NOTA: * indica campos obrigatórios")
		print("....................................................................")
		temp = []
		for j in range(cols):
					
			if j == 0:
				temp.append(str(input("Digite o nome*: ")))
				if temp[j] == '' or temp[j] == ' ':
					print("Nome é um campo obrigatório. Processo existe pela falta de resposta...")
					
			if j == 1:
				temp.append(int(input("Digite o número*: ")))

			if j == 2:
				temp.append(str(input("Digite o e-mail: ")))
				if temp[j] == '' or temp[j] == ' ':
					temp[j] = None
					
			if j == 3:
				temp.append(str(input("Digite a data de nascimento(DIA/MÊS/ANO): ")))
				if temp[j] == '' or temp[j] == ' ':
					temp[j] = None

			if j == 4:
				temp.append(
					str(input("Escolha o grupo de interesse(Familia/Amigos/Trabalho/Outros): ")))

				if temp[j] == "" or temp[j] == ' ':
					temp[j] = None
					
		contatos.append(temp)

	print sorted(contatos)
	return sorted(contatos)

def menu():
	print("********************************************************************")
	print("\tAgora você pode realizar as seguintes operações do programa\n")
	print("1. Adcionar um novo contato")
	print("3. Deletar todos os contatos")
	print("4. Buscar um contato")
	print("5. Mostrar todos os contatos")
	print("6. Encerrar o programa")

	choice = int(input("Por favor escolha a sua opção: "))
	
	return choice

def adicionar_contato(pb):
	dip = []
	for i in range(len(pb[0])):
		if i == 0:
			dip.append(str(input("Digite o nome: ")))
		if i == 1:
			dip.append(int(input("Digite o número: ")))
		if i == 2:
			dip.append(str(input("Digite o e-mail: ")))
		if i == 3:
			dip.append(str(input("Digite a data de nascimento(DIA/MÊS/ANO): ")))
		if i == 4:
			dip.append(
				str(input("Escolha o grupo de interesse(Familia/Amigos/Trabalho/Outros): ")))
	pb.append(dip)
	return sorted(pb)


def deletar_tudo(pb):
	return pb.clear()

def buscar_existente(pb):
	choice = int(input("Digite seu critério de busca\n\n\
	1. Nome\n2. Número\n3. Email\n4. DDN\n5. Grupos de interesse(Familia/Amigos/Trabalho/Outros)\
	\nPlease enter: "))
	
	temp = []
	check = -1
	
	if choice == 1:
		query = str(
			input("Digite o nome do contato que deseja buscar: "))
		for i in range(len(pb)):
			if query == pb[i][0]:
				check = i
				temp.append(pb[i])
				
	elif choice == 2:
		query = int(
			input("Digite o número do contato que deseja buscar "))
		for i in range(len(pb)):
			if query == pb[i][1]:
				check = i
				temp.append(pb[i])
				
	elif choice == 3:
		query = str(input("Digite o e-mail\
		do contato que deseja buscar: "))
		for i in range(len(pb)):
			if query == pb[i][2]:
				check = i
				temp.append(pb[i])
				
	elif choice == 4:
		query = str(input("Digite a data de nascimento do contato (DIA/MÊS/ANO)\
			do contato que deseja buscar: "))
		for i in range(len(pb)):
			if query == pb[i][3]:
				check = i
				temp.append(pb[i])
				
	elif choice == 5:
		query = str(
			input("Digite o grupo de interesse do contato que deseja buscar: "))
		for i in range(len(pb)):
			if query == pb[i][4]:
				check = i
				temp.append(pb[i])
	else:
		print("Inválido")
		return -1

	if check == -1:
		return -1
	else:
		mostrar_tudo(temp)
		return check

def mostrar_tudo(pb):
	if not pb:
		print("Lista está vazia: []")
	else:
		for i in range(len(pb)):
			print sorted(pb[i])

def obrigado():
	print("********************************************************************")
	print("Obrigado por usar este programa.")
	print("********************************************************************")

print("....................................................................")
print("Bem-vindo ao programa de organização e gerenciamento de contatos")
print("Explore o diretório e suas opções")
print("....................................................................")

ch = 1
pb = contato_inicial()
while ch in (1, 2, 3, 4, 5):
	ch = menu()
	if ch == 1:
		pb = adicionar_contato(pb)
	elif ch == 3:
		pb = deletar_tudo(pb)
	elif ch == 4:
		d = buscar_existente(pb)
		if d == -1:
			print("O contato não existe, tente novamente")
	elif ch == 5:
		mostrar_tudo(pb)
	else:
		obrigado()
