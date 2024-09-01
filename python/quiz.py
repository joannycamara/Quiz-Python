#Componentes: Débora Alice de Oliveira, Joanny Câmara Maranhão, Maria Helen Moreno e Vitória de Oliveira Silva
#Disciplina: Introdução à Programação
#Turma: Informática, 1° ano matutino


def matematica_quiz():
    perguntas = [
        {"pergunta": "Qual é a razão entre 15 e 25?", 
         "respostas": ["a) 2:5", "b) 3:5", "c) 5:3", "d) 5:2"], "correta": "b"},
        
        {"pergunta": "Um produto que custa R$ 200,00 está com 20% de desconto. Qual será o preço do produto após o desconto?", 
         "respostas": ["a) R$ 150,00", "b) R$ 160,00",  "c) R$ 170,00", "d) R$ 180,00"], "correta": "b"},
        
        {"pergunta": "Qual é a razão simplificada entre 24 e 36?", 
         "respostas": ["a) 2:3", "b) 3:4", "c) 4:5", "d) 2:5"], "correta": "a"},
        
        {"pergunta": "Se um salário de R$ 1.200,00 for aumentado em 15%, qual será o novo salário?", 
         "respostas": ["a) R$ 1.300,00", "b) R$ 1.380,00", "c) R$ 1.500,00", "d) R$ 1.800,00"], "correta": "b"},
        
        {"pergunta": "Qual é a probabilidade de tirar um 4 ao lançar um dado de 6 faces?", 
         "respostas": ["a) 1/2", "b) 1/4", "c) 1/6", "d) 1/3"], "correta": "c"}
    ]
    return perguntas

def quimica_quiz():
    perguntas = [
        {"pergunta": "Qual é o símbolo químico para a água?", 
         "respostas": ["a) H2O", "b) CO2", "c) O2", "d) NaCl"], "correta": "a"},
        
        {"pergunta": "Qual é o número atômico do Carbono?", 
         "respostas": ["a) 8", "b) 12", "c) 6", "d) 14"], "correta": "c"},
        
        {"pergunta": "Qual é o elemento químico com símbolo 'Fe'?", 
         "respostas": ["a) Francio", "b) Flúor", "c) Fósforo", "d) Ferro"], "correta": "d"},
        
        {"pergunta": "Qual ácido é encontrado no suco gástrico?", "respostas": ["a) Ácido Nítrico", "b) Ácido Acético", "c) Ácido Sulfúrico", "d) Ácido Clorídrico"], "correta": "d"},
        
        {"pergunta": "O que é uma ligação covalente?", "respostas": ["a) Ligação entre dois átomos que compartilham elétrons", "b) Ligação entre dois átomos que trocam elétrons", "c) Ligação entre átomos metálicos", "d) Ligação entre íons"], "correta": "a"}
    ]
    return perguntas

def biologia_quiz():
    perguntas = [
        {"pergunta": "O ______ integra todos os estímulos recebidos pelo corpo, suas funções e ações. Marque a alternativa que na sua opinião, se encaixa no espaço em branco. ", 
         "respostas": ["a) Sistema cardiovascular", "b) Sistema muscular", "c) Sistema nervoso", "d) Sistema respiratório"], "correta": "c"},
        
        {"pergunta": "Qual é a principal forma de armazenamento de energia no corpo?", 
         "respostas": ["a) Corpos cetônicos", "b) Carboidratos", "c) Proteínas", "d) Lipídios"], "correta": "d"},
        
        {"pergunta": "O que é a fotossíntese?", 
         "respostas": ["a) Processo de respiração das plantas", "b) Processo de produção de energia pelas plantas", "c) Processo de divisão celular", "d) Processo de digestão das plantas"], "correta": "b"},
        
        {"pergunta": "Qual é o principal pigmento responsável pela cor verde das plantas?", 
         "respostas": ["a) Clorofila", "b) Caroteno", "c) Antocianina", "d) Xantofilina"], "correta": "a"},
        
        {"pergunta": "Qual é a função do sistema circulatório?", 
         "respostas": ["a) Transportar oxigênio e nutrientes pelo corpo", "b) Produzir hormônios", "c) Facilitar a digestão", "d) Proteger o corpo contra patógenos"], "correta": "a"}
    ]
    return perguntas

def realizar_quiz(perguntas):
    acertos = 0
    erros = 0
    
    for i, p in enumerate(perguntas):
        print(f"Pergunta {i+1}: {p['pergunta']}")
        for opcao in p['respostas']:
            print(opcao)
        
        resposta = input("Digite a letra da resposta correta (a, b, c, d): ").strip().lower()
        
        if resposta == p['correta']:
            print("Resposta correta!")
            acertos += 1
        else:
            print("Resposta errada!")
            erros += 1
        
        print()
    
    total_perguntas = len(perguntas)
    percentual_acertos = (acertos / total_perguntas) * 100
    percentual_erros = (erros / total_perguntas) * 100
    
    print(f"Você acertou {acertos} de {total_perguntas} perguntas.")
    print(f"Percentual de acertos: {percentual_acertos:.2f}%")
    print(f"Percentual de erros: {percentual_erros:.2f}%")
    print()

def menu():
    while True:
        print("Menu de Opções:")
        print("1. Quiz de Matemática")
        print("2. Quiz de Química")
        print("3. Quiz de Biologia")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1, 2, 3, 4): ").strip()
        
        if opcao == "1":
            perguntas = matematica_quiz()
            realizar_quiz(perguntas)
        elif opcao == "2":
            perguntas = quimica_quiz()
            realizar_quiz(perguntas)
        elif opcao == "3":
            perguntas = biologia_quiz()
            realizar_quiz(perguntas)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
        print()

# Exibe o menu inicial ao iniciar o programa
menu()

