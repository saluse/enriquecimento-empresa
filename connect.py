import pandas as pd
import requests
from tqdm import tqdm


def data_atual():
    from datetime import datetime
    return datetime.now().strftime('%Y%m%d')


def get_api_data(cnpj):
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "cnpj": data.get("cnpj"),
            "identificador_matriz_filial": data.get("identificador_matriz_filial"),
            "descricao_matriz_filial": data.get("descricao_matriz_filial"),
            "razao_social": data.get("razao_social"),
            "nome_fantasia": data.get("nome_fantasia"),
            "situacao_cadastral": data.get("situacao_cadastral"),
            "descricao_situacao_cadastral": data.get("descricao_situacao_cadastral"),
            "data_inicio_atividade": data.get("data_inicio_atividade"),
            "cnae_fiscal": data.get("cnae_fiscal"),
            "cnae_fiscal_descricao": data.get("cnae_fiscal_descricao"),
            "descricao_tipo_de_logradouro": data.get("descricao_tipo_de_logradouro"),
            "logradouro": data.get("logradouro"),
            "numero": data.get("numero"),
            "complemento": data.get("complemento"),
            "bairro": data.get("bairro"),
            "cep": data.get("cep"),
            "uf": data.get("uf"),
            "codigo_municipio": data.get("codigo_municipio"),
            "municipio": data.get("municipio"),
            "ddd_telefone_1": data.get("ddd_telefone_1"),
            "ddd_telefone_2": data.get("ddd_telefone_2"),
            "ddd_fax": data.get("ddd_fax"),
            "qualificacao_do_responsavel": data.get("qualificacao_do_responsavel"),
            "capital_social": data.get("capital_social"),
            "porte": data.get("porte"),
            "descricao_porte": data.get("descricao_porte"),
            "opcao_pelo_simples": data.get("opcao_pelo_simples"),
            "data_opcao_pelo_simples": data.get("data_opcao_pelo_simples"),
            "data_exclusao_do_simples": data.get("data_exclusao_do_simples"),
            "opcao_pelo_mei": data.get("opcao_pelo_mei"),
            "situacao_especial": data.get("situacao_especial"),
            "data_situacao_especial": data.get("data_situacao_especial"),
        }
    else:
        print(f"Erro ao obter dados da API para o CNPJ {cnpj}. Status code: {response.status_code}")
        return None


df = pd.read_csv("data/cnpj.csv")

cnpjs = df["cnpj"].unique()

api_data_list = []

for cnpj in tqdm(cnpjs, desc="Obtendo dados da API"):
    api_data = get_api_data(cnpj)
    if api_data:
        api_data_list.append(api_data)

api_df = pd.DataFrame(api_data_list)

api_df.to_csv("output/results.csv", index=False)

print("Processo concluído. Os dados foram salvos em 'output/results.csv'")
