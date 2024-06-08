import random
import csv
import os

def generate_cnpj():
    def calculate_digit(digits):
        weight = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        sum_digits = sum([int(d) * w for d, w in zip(digits, weight[1:])])
        remainder = sum_digits % 11
        return '0' if remainder < 2 else str(11 - remainder)
    
    base = [random.randint(0, 9) for _ in range(12)]
    first_digit = calculate_digit(base)
    second_digit = calculate_digit(base + [int(first_digit)])
    
    cnpj = ''.join(map(str, base)) + first_digit + second_digit
    return cnpj

def generate_cnpj_list(n):
    return [generate_cnpj() for _ in range(n)]

def save_cnpj_list_to_csv(cnpj_list, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["cnpj"])
        for cnpj in cnpj_list:
            writer.writerow([cnpj])

# Exemplo de uso: gerar uma lista de 10 CNPJs
num_cnpjs = 100
cnpj_list = generate_cnpj_list(num_cnpjs)

# Caminho do arquivo para salvar a lista de CNPJs
output_file = os.path.join('data', 'cnpj.csv')

# Salvar a lista de CNPJs no arquivo CSV
save_cnpj_list_to_csv(cnpj_list, output_file)

print(f"Lista de CNPJs gerada e salva em '{output_file}'")
