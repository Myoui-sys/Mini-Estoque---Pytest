
# Aula 02 – UC3 | Casos de Teste

## CT-001 – Cadastro de produto com dados válidos

**ID:** CT-001

**OBJETIVO:** Verificar se o sistema permite cadastrar um produto com dados válidos.

**PRÉ-CONDIÇÃO:** Funcionalidades de cadastro, listagem e remoção disponíveis. Regras de negócio definidas no README.

**ENTRADA:** Nome: Caneta Azul; Preço: R$ 1,00; Quantidade: 10.

**PASSOS:**
1. Acessar o menu principal.
2. Selecionar a opção de cadastrar produto.
3. Informar o nome, o preço e a quantidade.
4. Confirmar o cadastro.
5. Acessar a listagem de produtos.
6. Verificar se o produto foi cadastrado com os dados informados.
7. Remover o produto cadastrado.
8. Realizar novamente o cadastro.

**RESULTADO ESPERADO:** O sistema deve permitir o cadastro e apresentar o produto na listagem com todas as informações preenchidas corretamente.

**RESULTADO OBTIDO:** Produto cadastrado com sucesso, apresentando corretamente os dados informados.

**STATUS:** ✅ Passou.

---

## CT-002 – Tentativa de cadastro com preço igual a zero

**ID:** CT-002

**OBJETIVO:** Verificar se o sistema impede o cadastro de produtos com preço igual a zero.

**PRÉ-CONDIÇÃO:** Funcionalidade de cadastro de produtos disponível. Regras de negócio definidas no README.

**ENTRADA:** Nome: Caneta Vermelha; Preço: R$ 0,00; Quantidade: 10.

**PASSOS:**
1. Acessar o menu principal.
2. Selecionar a opção de cadastrar produto.
3. Informar o nome do produto.
4. Informar o preço igual a zero.
5. Informar a quantidade.
6. Confirmar o cadastro.

**RESULTADO ESPERADO:** O sistema deve impedir o cadastro, pois o preço do produto precisa ser maior que zero.

**RESULTADO OBTIDO:** O sistema impediu o cadastro e apresentou a mensagem de erro: "Preço deve ser maior que zero".

**STATUS:** ✅ Passou.
