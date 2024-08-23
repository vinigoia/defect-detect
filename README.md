<img src="https://github.com/vinigoia/defect-detect/assets/logo_take.jpg"/>

<div align="center">
  
  [![Linkedin Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/vinicius-goia-75a403234)](https://www.linkedin.com/in/vinicius-goia-75a403234)

</div>

# Detecção de Defeitos em Superfícies

Este repositório refere-se ao projeto de etapa de processo seletivo da Empresa Take and Go para a vaga de Desenvolvedor de Inteligência Artificial. Os algoritmos carregam o dataset e treinam um modelo capaz de realizar classificações em novas imagens.

## Pré-requisitos

* **VSCode** - Editor de código utilizado durante o desenvolvimento. Disponível para Windows, macOS e Linux. [Instalação oficial do VSCode](https://code.visualstudio.com/download)

* **GitHub** - Plataforma de hospedagem de código. É essencial ter uma conta para interagir com os repositórios. [Como criar uma conta no GitHub](https://docs.github.com/pt/get-started/onboarding/getting-started-with-your-github-account)

## Instalação e Configuração

Aqui está um resumo dos passos que você precisa seguir:

1. Clonar o [Repositório Github](https://github.com/vinigoia/defect-detect_api) para a sua máquina local:

   ```bash
   git clone https://github.com/vinigoia/defect-detect_api
   ```

**Obs:** Antes de proseguir, delete as pastas `metrics` e `logs` para que o processo gere-as novamente. O arquivo `defect_model.keras` pode ser mantido pois será substituído. Caso haja necessidade de novos treinamentos com épocas diferentes, na pasta `dataset` certifique-se de deixar apenas o arquivo compactado.

2. Criar um ambiente virtual, acessá-lo e instalar as dependências necessárias:

   ```bash
   python -m venv virt_env
   .\virt_env\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. Executar o comando abaixo para que os códigos sejam executados:

   ```bash
   python defect_detect.py -e E -t T
   ```

4. Inserir o número de épocas e aguardar o processamento.

Ao final do processo, um modelo será gerado, de nome `defect_model.keras`, e as pastas `metrics` e `logs` também serão geradas.

A aplicação também está hospedada no site do Streamlit, podendo ser acessada diretamente pelo [link](https://blurimagesapi-bpsnngqkeuandkara6zets.streamlit.app/)







# Funcionamento

<img src="https://github.com/vinigoia/blur_Images_api/blob/main/Arquivos%20de%20teste/ezgif.com-video-to-gif-converter.gif" width="50%" height="50%"/>

# Resultado

## Imagem Original

<img src="https://github.com/vinigoia/blur_Images_api/blob/main/Arquivos%20de%20teste/ellen-degeneres-de-branco-em-foto.jpg"/>

## Imagem Desfocada

<img src="https://github.com/vinigoia/blur_Images_api/blob/main/Arquivos%20de%20teste/img_blurred%20(1).png"/>

