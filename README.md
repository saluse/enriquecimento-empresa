# Projeto para Enriquecimento de Dados para Empresas Baseado no CNPJ #

Este projeto tem como objetivo fornecer um robusto sistema de enriquecimento de dados para empresas, utilizando o CNPJ como chave primária. Com esta solução, será possível melhorar significativamente a qualidade e a quantidade de informações disponíveis sobre as empresas na sua base de dados.

> *Nota: Os dados fornecidos aqui neste projeto estão disponíveis de forma pública no site: https://brasil.io/home/ e https://brasilapi.com.br/*

## Funcionalidades Principais: ##

### Geolocalização Detalhada: ###

* Estado: Identificação do estado onde a empresa está localizada.
* Município: Detalhamento do município da empresa.
* Cidade: Informação específica sobre a cidade de atuação.
* Bairro: Precisão sobre o bairro em que a empresa se encontra.
* Rua: Endereço completo, incluindo nome da rua.
* CEP: Código postal para correspondências e logística.
  
### Dados de Situação Cadastral: ###

* Nome Fantasia: Nome pelo qual a empresa é conhecida no mercado.
* Situação Cadastral: Status atual do cadastro da empresa, indicando se está ativa, inativa, entre outras situações possíveis.
* Início das Atividades: Data de início das operações da empresa, proporcionando uma visão sobre sua experiência e tempo de mercado.
* Informações Econômicas e Fiscais:
* CNAE Fiscal: Classificação Nacional de Atividades Econômicas, que detalha a atividade econômica principal da empresa, auxiliando na segmentação e análise de mercado.
  
### Benefícios do Projeto: ###

* Tomada de Decisão Aprimorada: Com dados mais completos e precisos, as empresas poderão tomar decisões mais informadas e estratégicas.
* Aumento da Eficiência Operacional: Automatização do processo de enriquecimento de dados, reduzindo a necessidade de intervenções manuais e minimizando erros.
* Melhoria da Experiência do Cliente: Dados atualizados e detalhados permitem um melhor entendimento do perfil e das necessidades dos clientes, possibilitando um atendimento mais personalizado.
* Compliance e Regulação: Manter as informações cadastrais sempre atualizadas ajuda a cumprir com regulamentações e obrigações legais, evitando possíveis penalidades.
  
 **Este projeto representa um avanço significativo na gestão e utilização de dados corporativos, contribuindo para um ambiente empresarial mais competitivo e eficiente.**

### Release ###

Dentro da pasta data existe um arquivo chamado cnpj.csv que contem diversos cnpjs que são compartilhados de forma pública na web. 
Com essa base inicial, utilizaremos os cnpjs como chave para fazer uma conexão com a BrasilAPI (https://brasilapi.com.br/api/cnpj/v1/{cnpj}) e trazer diversos dados como Estado, Município, cidade, bairro, rua, cep, dados de situação cadastral, nome fantasia,
início das atividades, CNAE fiscal.
O resultado é salvo na pasta output.
