import time
import random
import matplotlib.pyplot as plt

#Algoritimo de ordenação (Bubble_sort)
def bubble_sort(lista):
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(0, tam - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

#Algoritimo de ordenação (insertion_sort)
def insertion_sort(lista):
    for i in range(1, len(lista)):
        pivo = lista[i]
        j = i - 1
        while j >= 0 and pivo < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = pivo

#Algoritimo de ordenação (selection_sort)
def selection_Sort(lista):
    tam = len(lista)
    for i in range(tam):
        min_index = i
        for j in range(i + 1, tam):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

#Algoritimo de ordenação (merge_sort)
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        L = lista[:meio]
        R = lista[meio:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

#Menu onde o usuario irá escolher qual algoritimo desja utilizar
def menu_operacao():
    print('''
    =============== Qual Operação Deseja Realizar ===============
    (1) Bubble Sort
    (2) Selection Sort
    (3) Insertion Sort
    (4) Merge Sort
    =============================================================''')
    
    while True:
        escolha = int(input("Escolha: "))
        if escolha in (1, 2, 3, 4):
            return escolha
        else:
            print("Escolha inválida. Digite Novamente")

#Usuario deve informar o tamanho da lista que deseja ordenar
def escolha_tamnho():
    while True:
        tamanho = int(input("Qual o tamanho da lista que deseja ordenar: "))
        if tamanho >= 1:
            return tamanho
        else:
            print("Tamanho Invalido. Digite Novamente")

#Gerar uma lista aleatoria de acordo com o tamanho que o usuario forneceu 
def gerar_lista_aleatoria(tamanho):
    lista = []
    for _ in range(tamanho):
        numero_aleatorio = random.randint(0, tamanho)
        lista.append(numero_aleatorio)
    return lista

#Função para mostrar o nome do algoritimo no final da execução
def algoritmo(escolha):
    algoritmos = {
        1: "Bubble Sort",
        2: "Selection Sort",
        3: "Insertion Sort",
        4: "Merge Sort"
    }
    return algoritmos.get(escolha, "Algoritmo não encontrado")

#Função para calcular o tempo de execução de acordo com o algoritimo escolhido
def obter_time(escolha, tamanho):
        lista = gerar_lista_aleatoria(tamanho)
        print(f"Lista desordenada: {lista}")
        inicio = time.time()
        match escolha:
            case 1:
                bubble_sort(lista)
            case 2:
                selection_Sort(lista)
            case 3:
                insertion_sort(lista)
            case 4:
                merge_sort(lista)
        
        fim = time.time()
        print(f"Lista ordenada: {lista}")
        return fim - inicio

#Função para gerar grafico de acordo com o tempo e a media obtida
def criar_grafico(tempos_execucao, nome_algoritmo, media_tempo_execucao, tamanho):
    # Criar um gráfico de linhas com os tempos de execução
    plt.plot(range(1, len(tempos_execucao) + 1), tempos_execucao, label='Tempos de Execução', marker='o')

    # Adicionar uma linha horizontal para representar a média
    plt.axhline(y=media_tempo_execucao, color='r', linestyle='--', label='Média')

    # Adicionar rótulos aos pontos do gráfico (tempos exatos)
    for i, tempo in enumerate(tempos_execucao):
        plt.text(i + 1, tempo, f'{tempo:.3f}', ha='center', va='bottom')
    
    x_ticks = range(1, len(tempos_execucao) + 1, 1)
    plt.xticks(x_ticks)

    # Adicionar "legenda" aos eixos e um título
    plt.xlabel(f'Execução {nome_algoritmo}')
    plt.ylabel('Tempo (segundos)')
    plt.title(f'Gráfico de Linhas com Média de Tempo de Execução (Tamanho da Lista: {tamanho})')

    # Adicionar uma legenda
    plt.legend()

    # Exibir o gráfico
    plt.show()

#Programa Principal 
def principal():
    escolha = menu_operacao()
    tamanho = escolha_tamnho()  
    tempos_execucao = []
    
    for i in range(3):
        tempo_execucao = obter_time(escolha, tamanho)  
        tempos_execucao.append(tempo_execucao)  
        print(f'Tempo de execução (execução {i + 1}): {tempo_execucao:.3f}')
        nome_algoritmo = algoritmo(escolha)
        print(f'O algoritmo escolhido foi {nome_algoritmo}')
    #Calcular a media dos tempos obtidos 
    media_tempo_execucao = sum(tempos_execucao) / len(tempos_execucao)
    print(f"A média obtida é {media_tempo_execucao:.3f}")
    criar_grafico(tempos_execucao, nome_algoritmo, media_tempo_execucao, tamanho)

# Principal
principal()
