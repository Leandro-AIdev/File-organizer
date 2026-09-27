# 📁 File Organizer

Automação desenvolvida em Python para organizar arquivos automaticamente em diferentes categorias, reduzindo o trabalho manual de organização de pastas.

## 🎯 Objetivo

O File Organizer identifica os arquivos presentes em uma pasta e os move automaticamente para pastas específicas de acordo com suas extensões.

Por exemplo:

```text
.jpg  → Imagens
.pdf  → Documentos
.xlsx → Planilhas
.mp4  → Videos
.mp3  → Musicas
.zip  → Compactados
```

## ✨ Funcionalidades

* Organização automática de arquivos
* Criação das pastas de destino
* Classificação por extensão
* Movimentação automática dos arquivos
* Prevenção de sobrescrita de arquivos existentes
* Registro das operações realizadas
* Relatório final da execução
* Contagem de arquivos encontrados, movidos e com erro

## 🛠️ Tecnologias

* Python 3
* `pathlib`
* `shutil`
* `datetime`

## 📂 Categorias

Atualmente o organizador trabalha com categorias como:

* Imagens
* Documentos
* Planilhas
* Apresentações
* Músicas
* Vídeos
* Compactados

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entre na pasta

```bash
cd file-organizer
```

### 3. Execute o programa

```bash
python main.py
```

O programa irá analisar a pasta configurada e organizar os arquivos automaticamente.

## 📊 Exemplo de execução

```text
Arquivos encontrados: 11
Movidos com sucesso: 11
Erros: 0

Log: organizer.log
```

## 📋 Estrutura

```text
File-organizer/
├── main.py
└── README.md
```

## 🚧 Próximas melhorias

* Interface gráfica
* Configuração das categorias pelo usuário
* Modo de simulação antes de mover os arquivos
* Maior controle sobre extensões
* Melhor tratamento de arquivos desconhecidos
* Relatórios mais detalhados

## 👨‍💻 Autor

Leandro

Projeto desenvolvido como parte do portfólio de automação com Python.
