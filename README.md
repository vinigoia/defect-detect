<p align="center">
  <img src="https://github.com/vinigoia/defect-detect/blob/c766e972dd478f8cda17cd8d5fc5797f91714ad6/assets/logo_take.jpg"width="70%"</p>

<div align="center">
  
  [![Linkedin Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/vinicius-goia-75a403234)](https://www.linkedin.com/in/vinicius-goia-75a403234)

</div>

# Detecção de Defeitos em Superfícies

Este repositório refere-se ao projeto de etapa de processo seletivo da Empresa Take and Go para a vaga de Desenvolvedor de Inteligência Artificial. Os algoritmos carregam o dataset e treinam um modelo capaz de realizar classificações em novas imagens.

## Pré-requisitos   

* **Python** - Dependências necessárias para executar na linguagem. [Instalação Python][https://www.python.org/downloads/)

* **VSCode** - Editor de código utilizado durante o desenvolvimento. Disponível para Windows, macOS e Linux. [Instalação oficial do VSCode](https://code.visualstudio.com/download)

* **GitHub** - Plataforma de hospedagem de código. É essencial ter uma conta para interagir com os repositórios. [Como criar uma conta no GitHub](https://docs.github.com/pt/get-started/onboarding/getting-started-with-your-github-account)

## Instalação e Configuração

Aqui está um resumo dos passos que você precisa seguir:

1. Clonar o [Repositório Github](https://github.com/vinigoia/defect-detect.git) para a sua máquina local e entrar na pasta:

   ```bash
   git clone https://github.com/vinigoia/defect-detect.git
   cd defect-detect
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

No bash, o link `http://localhost:6006/` será exibido. Clicando nele, o servidor do Tensorboard será acessado através de uma pagina web.

# Tensorboard

<p align="center">
  <img src="https://www.tensorflow.org/tensorboard/images/tensorboard.gif"width="50%"</p>

O Tensorboard funciona através dos logs gerados durante o processo de treinamento e, de maneira interativa, é possível observar diversas métricas.

# Resultados

## Matriz Confusão

<img src="https://github.com/vinigoia/defect-detect/blob/c766e972dd478f8cda17cd8d5fc5797f91714ad6/assets/confusion_matrix.png"/>

## Imagem Desfocada

<img src="https://github.com/vinigoia/blur_Images_api/blob/main/Arquivos%20de%20teste/img_blurred%20(1).png"/>

