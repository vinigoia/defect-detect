<p align="center">
  <img src="https://github.com/vinigoia/defect-detect/blob/c766e972dd478f8cda17cd8d5fc5797f91714ad6/assets/logo_take.jpg"width="70%"</p>

<div align="center">
  
  [![Linkedin Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/vinicius-goia-75a403234)](https://www.linkedin.com/in/vinicius-goia-75a403234)

</div>

# Detecção de Defeitos em Superfícies

Este repositório refere-se ao projeto de etapa de processo seletivo da Empresa Take and Go para a vaga de Desenvolvedor de Inteligência Artificial. Os algoritmos carregam o dataset e treinam um modelo capaz de realizar classificações em novas imagens.

<p align="center">
  <img src="https://github.com/vinigoia/defect-detect/blob/defect-detect-proj/assets/epoch_metrics_csv.png"width="50%"</p>

## Pré-requisitos   

* **Python** - Dependências necessárias para executar a linguagem. [Instalação Python](https://www.python.org/downloads/)

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
**Obs:** A flag `-e E` habilita a avaliação do modelo ao final do proceso. A flag `-t T` habilita o servidor Tensorboard no final do processo.

4. Inserir o número de épocas e aguardar o processamento.

Ao final do processo, um modelo será gerado, de nome `defect_model.keras`, e as pastas `metrics` e `logs` também serão geradas.

No bash, o link `http://localhost:6006/` será exibido. Clicando nele, o servidor do Tensorboard será acessado através de uma pagina web.

# Tensorboard

<p align="center">
  <img src="https://www.tensorflow.org/tensorboard/images/tensorboard.gif"width="50%"</p>

O Tensorboard funciona através dos logs gerados durante o processo de treinamento e, de maneira interativa, é possível observar diversas métricas.

# Resultados

## Matriz Confusão
<p align="center">
  <img src="https://github.com/vinigoia/defect-detect/blob/c766e972dd478f8cda17cd8d5fc5797f91714ad6/assets/confusion_matrix.png"width="50%"</p>

A Matriz Confusão é uma tabela onde é possível observar o desempenho de um classificador. Basicamente ela indica quando o modelo classificou de forma correta ou não as entradas.
A foto acima representa a Matriz Confusão gerada pelos códigos disponibilizados e observa-se que houve poucos erros. A partir disso, pode-se verificar outras métricas.

## Acurácia, Precisão, Recall e F1-Score

<p align="center">
  <img src="https://github.com/vinigoia/defect-detect/blob/c766e972dd478f8cda17cd8d5fc5797f91714ad6/assets/classification_report_json.png"width="30%"</p>

Como observado acima, as nossas métricas para o modelo treinado foram muito boas. Vamos entender o que cada uma delas representa:

### Acurácia

Basicamente a Acurácia nos indica quantos exemplos foram classificados de maneira correta, independentemente da classe. É representada pela fórmula abaixo:

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:700/1*FvMtz5kCu-GOI3GSgi6k4Q.png"width="50%"</p>

Deve-se tomar cuidado em apenas analisar a Acurácia pois, mesmo atingindo porcentagens altas, isso pode não condizer com a realidade, ainda mais quando se possui um dataset desbalanceado.

### Precisão

Conhecida como acurácia das predições positivas, dá ênfase maior aos erros falsos positivos. É representada pela função abaixo:

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:700/1*9yxSYzw298P_JSZuTMVEBg.png"width="50%"</p>

### Recall ou Revogação

Também chamada de sensibilidade ou taxa de verdadeiros positivos (TPR), é a proporção de instâncias positivas que são detectadas corretamente pelo classificador. É representada pela fórmula abaixo:

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:700/1*fqZ1ymVGGSA5fbqYrf1t1Q.png"width="50%"</p>

### F1 Score

É a média harmônica da precisão e do recall, dando importância aos valores mais baixos. Representada pela fórmula abaixo:

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:700/1*qFeLJvX-K3VMfROmKTejpQ.png"width="50%"</p>


# Sobre o Processo

O intuito desse projeto foi demonstrar a construção de códigos que possibilitaram a execução do treinamento de um modelo de maneira automática através de um dataset fornecido.
Alguns processos comumentes utilizados nesse tipo de pipeline foram desconsiderados devido a estrutura do dataset. Por exemplo, o processo de divisão de dados de treinamento e teste já estava realizado. Também observou-se o balancemanto das classes através da quantidade de fotos por pasta.

Em um primeiro caso, havia-se observado métricas muito boas no dataset sem data augmentation e transfer-learning, porém, nos testes, os valores ficaram um pouco abaixo do esperado. Optou-se, então, pela utilização de transfer-learning para a otimização das métricas de treinamento. 

Os códigos foram estruturados de uma maneira em que os processos são claramente visíveis, facilitando qualquer alteração.

Foi verificado a possibilidade da criação de um entregável executável, porém, devido ao seu grande tamanho, não foi disponibilizado aqui. O executável, caso mantido, não poderia ser compilado com a flag `-t T`. Foi utilizado o comando `pyinstaller --onefile defect_detect.py` para esta ação.

Ao final, obteve-se um modelo que atingiu as seguintes métricas no dataset de teste: 
Acurácia: 0.9340 
F1 Score: 0.9297 
Precision: 0.9360 
Recall: 0.9237

Há espaço para novos testes e investigações, bem como aplicações em situações reais de Visão Computacional para a real medição da eficiência.





  
