# Finanças IA: Análise Inteligente de Gastos com Gemini

Finanças IA é um script Python que utiliza a poderosa API de inteligência artificial do Google (Gemini) para analisar seus gastos diretamente do Google Sheets, oferecendo insights financeiros personalizados para ajudar jovens adultos a gerenciar seu dinheiro de forma eficaz.

## Contexto com a Imersão de IA

Este projeto, "Finanças IA", integra os conceitos e ferramentas apresentados na imersão de Inteligência Artificial. Inspirado pela Aula 4, ele utiliza a capacidade de geração de linguagem natural da API Gemini para fornecer insights financeiros personalizados e explicações claras sobre os dados analisados. "Finanças IA" demonstra a aplicação da IA para automatizar a análise de dados financeiros e auxiliar na tomada de decisões.

## Utilidade do Projeto

Para jovens adultos, acompanhar gastos e criar orçamentos eficazes pode ser uma tarefa desafiadora. "Finanças IA" surge como uma solução para simplificar esse processo. Ao analisar automaticamente os dados de gastos do Google Sheets e fornecer insights relevantes, o projeto capacita os usuários a entenderem seus hábitos financeiros e a tomarem decisões mais conscientes.

## Criatividade da Solução

A criatividade do "Finanças IA" reside na sua capacidade de utilizar a API Gemini para ir além da simples apresentação de dados. O script não apenas processa os números do Google Sheets, mas também os interpreta e gera insights financeiros personalizados em linguagem natural. Essa abordagem permite que os usuários compreendam facilmente sua situação financeira e identifiquem oportunidades de melhoria. A integração com o Google Sheets, uma ferramenta amplamente utilizada, facilita o acesso aos dados e torna a solução prática e acessível.

## Eficácia da Solução:

"Finanças IA" oferece uma solução eficaz para a análise de gastos, proporcionando insights rápidos e personalizados. Ao automatizar a análise de dados, o script economiza tempo e esforço do usuário. A API Gemini gera recomendações sob medida, aumentando a relevância das informações. A integração com o Google Sheets simplifica o acesso aos dados e a implementação da solução.

## Como Usar:

Para utilizar o "Finanças IA" e obter insights sobre suas finanças, siga os passos abaixo:

### 1. Pré-requisitos:

- Você precisará de uma conta Google ativa.
- Organize seus dados de gastos em uma planilha do Google Sheets. Certifique-se de que a planilha tenha colunas para "Data", "Categoria" e "Valor" (você pode incluir outras colunas, mas essas são essenciais para a análise inicial).

### 2. Conectando sua Planilha:

- Informe ao script o link público da sua planilha do Google Sheets ou, se estiver executando o código localmente, certifique-se de que o script tenha as permissões necessárias para acessar a planilha (isso envolverá a configuração de credenciais da API Google Sheets).

### 3. Executando o Script:

- Execute o script Python. Ele irá ler os dados da sua planilha do Google Sheets.

### 4. Obtendo Insights:

- O script, utilizando a API Gemini, irá analisar seus dados e fornecer insights financeiros no console. Você poderá receber informações como:
  - "No último mês, sua maior categoria de gasto foi 'Alimentação', representando X% do seu total de despesas."
  - "Percebi que você tem um gasto considerável com 'Lazer' nos fins de semana. Que tal explorar opções mais econômicas para essas atividades?"
  - "Seu gasto total foi de R$ Y."
  - "Você gastou R$ Z em 'Transporte', um aumento de W% em relação ao mês anterior."

## Tecnologias Utilizadas:

- Python: A linguagem de programação utilizada para desenvolver a lógica do script, a interação com as APIs do Google e o processamento dos dados.
- API Gemini (via google-generativeai): A API de inteligência artificial do Google para análise de gastos e geração de insights em linguagem natural.
- Google Sheets API (via google-api-python-client): A API do Google Sheets para acessar os dados da planilha do usuário.
- Google Cloud Platform (GCP): A plataforma do Google Cloud para gerenciar as credenciais de acesso às APIs do Google.

## Instalação e Execução:

### 1. Pré-requisitos:

- **Python:** Certifique-se de que o Python 3.9 ou superior esteja instalado em seu sistema. Você pode verificar a versão executando `python --version` ou `python3 --version` no terminal. Se não estiver instalado, você pode baixá-lo em [https://www.python.org/downloads/](https://www.python.org/downloads/).
- **pip:** O gerenciador de pacotes do Python (`pip`) geralmente vem instalado com o Python. Verifique se ele está disponível executando `pip --version` ou `pip3 --version`.

### 2. Configuração do Projeto:

- **Clone o repositório:** Clone o repositório do projeto para o seu computador.
- **Navegue até o diretório do projeto:** Use o comando `cd` no terminal para entrar no diretório onde o projeto foi clonado.

### 3. Gerenciamento de Dependências (Recomendado):

- **Ambiente Virtual (Opcional, mas recomendado):** É uma boa prática criar um ambiente virtual para isolar as dependências do projeto.
  - **Criar um ambiente virtual:**
    ```bash
    python -m venv .venv  # Cria um ambiente virtual na pasta .venv (você pode escolher outro nome)
    ```
  - **Ativar o ambiente virtual:**
    - **Linux/macOS:**
      ```bash
      source .venv/bin/activate
      ```
    - **Windows:**
      ```bash
      .venv\Scripts\activate
      ```
- **Instalar as dependências:** Use o `pip` para instalar as bibliotecas necessárias. Se você tiver um arquivo `requirements.txt`, execute:
  ```bash
  pip install -r requirements.txt
  ```
  Se não tiver, instale as bibliotecas manualmente:
  ```bash
  pip install google-generativeai google-api-python-client google-auth pandas python-dotenv
  ```

### 4. Configuração das Credenciais:

- **Google Cloud Platform (GCP):**
  - Você precisará configurar um projeto no Google Cloud Platform (GCP) e habilitar a API do Google Sheets.
  - Crie uma conta de serviço e gere um arquivo de credenciais JSON.
  - Compartilhe a planilha do Google Sheets com o endereço de e-mail da conta de serviço (com permissão de leitura).
- **Variáveis de Ambiente:**
  - Para executar o script, você precisará definir as seguintes variáveis de ambiente:
    - `GOOGLE_API_KEY`: Sua chave da API Gemini.
    - `SERVICE_ACCOUNT_INFO`: O conteúdo do seu arquivo de credenciais JSON (ou a string Base64 codificada, conforme descrito anteriormente).
    - `SPREADSHEET_ID`: O ID da sua planilha do Google Sheets.
  - Você pode definir essas variáveis diretamente no seu terminal (para testes rápidos) ou usar um arquivo `.env` (com a biblioteca `python-dotenv`) para desenvolvimento local.
  - Em ambientes de produção (como Docker), é altamente recomendável definir essas variáveis diretamente no ambiente do sistema/container para segurança.

### 5. Execução do Script:

- Navegue até o diretório onde o arquivo `main.py` está localizado.
- Execute o script Python:
  ```bash
  python main.py
  ```

### 6. Execução com Docker (Opcional):

- Se você tiver o Docker instalado, pode executar o projeto em um container.
- **Construir a imagem Docker:**
  ```bash
  docker build -t financas-ia .
  ```
- **Executar o container:**
  ```bash
  docker run -it --rm \
      -e GOOGLE_API_KEY=$GOOGLE_API_KEY \
      -e SERVICE_ACCOUNT_INFO="$SERVICE_ACCOUNT_INFO" \
      -e SPREADSHEET_ID=$SPREADSHEET_ID \
      financas-ia
  ```
  - Certifique-se de substituir as variáveis de ambiente pelos valores reais ou de defini-las no seu ambiente antes de executar o comando.
  - O uso de `docker-compose` também é uma opção para configurar o ambiente.

## Próximos Passos:

- Interface Web Interativa: Desenvolver uma interface web onde o usuário poderá interagir via chat com a aplicação. Isso proporcionará uma experiência mais rica e intuitiva para obter insights financeiros detalhados.
- Login do Usuário com o Google: Implementar um sistema de login do usuário através de sua conta Google para simplificar o acesso à planilha do Google Sheets.s
- Registro de Transações via Chatbot: Implementar a funcionalidade para que o usuário possa adicionar novas despesas e receitas diretamente através de comandos de texto. A API Gemini poderia ser utilizada para entender a entrada do usuário, identificar o valor e a categoria, e adicionar essa transação automaticamente à planilha do Google Sheets do usuário.
