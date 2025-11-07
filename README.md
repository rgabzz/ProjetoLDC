# 🛒 Projeto LDC – Lista de Compras

O **Projeto LDC (Lista de Compras)** é uma aplicação web desenvolvida em **Flask**, com o objetivo de facilitar a organização e o gerenciamento de listas de compras personalizadas por usuário.  
Cada pessoa pode criar uma conta, montar suas próprias listas, adicionar itens, e acompanhar o que já foi comprado — tudo de forma prática e responsiva.

---

## 🚀 Funcionalidades Principais

- **Cadastro e Login de Usuários:**  
  Cada usuário possui uma conta própria, garantindo segurança e privacidade dos dados.  
  (As senhas são armazenadas com hash no banco de dados. Implementação futura: criptografia completa do login.)

- **Gerenciamento de Listas:**  
  O usuário pode criar, editar e excluir listas de compras, de acordo com suas necessidades.

- **Controle de Itens:**  
  É possível adicionar, editar ou remover itens de uma lista, com alertas e verificações para evitar duplicidades ou inconsistências.

- **Categorias de Itens:**  
  Cada item pode ser classificado em uma categoria (ex: alimentos, limpeza, higiene etc.), tornando a visualização mais organizada.

- **Marcar Itens como Comprados:**  
  O sistema permite marcar itens já adquiridos, facilitando o acompanhamento do que ainda falta comprar.

- **Busca e Filtros:**  
  O usuário pode buscar rapidamente itens específicos dentro de suas listas.

- **Exportação:**  
  As listas podem ser exportadas em **PDF** ou **texto**, permitindo impressão ou compartilhamento.

- **Interface Responsiva e Intuitiva:**  
  O layout adapta-se automaticamente a diferentes tamanhos de tela, oferecendo boa experiência tanto em computadores quanto em dispositivos móveis.

---

## 🧩 Estrutura do Projeto

O banco de dados segue um modelo relacional, composto por:

- **usuarios** – informações de login e autenticação.  
- **listas** – listas de compras vinculadas a cada usuário.  
- **itens** – itens pertencentes a cada lista, com suas respectivas categorias e status.  

---

## ⚙️ Tecnologias Utilizadas

- **Backend:** Flask (Python)  
- **Banco de Dados:** SQLite ou PostgreSQL (dependendo da configuração)  
- **Frontend:** HTML5, CSS3 (responsivo) e JavaScript  
- **Bibliotecas:**  
  - Flask-Login  
  - Flask-WTF  
  - SQLAlchemy  
  - Werkzeug (para hash de senhas)  
  - ReportLab ou FPDF (para exportação em PDF)

---

## 🧠 Observações Gerais

- O sistema foi desenvolvido com foco em **segurança e usabilidade**.  
- Todas as operações incluem **tratamento de exceções**, garantindo integridade dos dados.  
- O layout e a organização de cores/categorias visam tornar o uso **intuitivo e agradável**.  
- A estrutura do código foi pensada para permitir **expansão futura**, como integração com APIs externas, histórico de compras e relatórios automáticos.

---

## 🛠️ Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/ldc-projeto.git
cd ldc-projeto
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
```

### 3. Ative o ambiente virtual
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

### 4. Instale as dependências
Certifique-se de que o arquivo `requirements.txt` está na pasta raiz do projeto.  
Em seguida, execute:
```bash
pip install -r requirements.txt
```

### 5. Configure o banco de dados
Crie o banco e execute as migrações (se aplicável):
```bash
flask db upgrade
```
Ou, se o projeto usar SQLite, ele será criado automaticamente na primeira execução.

### 6. Execute o servidor
```bash
flask run
```
O sistema estará disponível em:
```
http://localhost:5000
```

---

## 👨‍💻 Desenvolvimento

**Projeto desenvolvido para fins acadêmicos**  

---
🛍️ *"Simplifique suas compras, organize sua rotina."*
