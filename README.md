# Adapter

## Definição do GoF, no livro "Padrões de Projeto" (2000)

### Intenção: 
Converter a interface de uma classe em outra interface, esperada pelos clientes. O **Adapter** permite que classes com 
interfaces incompatíveis trabalhem em conjunto - o que, de outra forma, seria impossível.

### Tipo de pattern:
Estrutural

### Também conhecido como:
Wrapper

### Aplicável quando:
- Você quiser usar uma classe existente, mas sua interface não corresponder à interface de que necessita.
- Você quiser criar uma classe reutilizável que coopere com classes não-relacionadas ou não-prevista, ou seja, classes 
que não necessariamente tenham interfaces compatíveis.
- (Somente para Objetos) Você precisar usar várias subclasses existentes, porém, for impraticável adaptar essas 
interfaces criando subclasses para cada uma. Um **Adapter** de objeto pode adaptar a interface da sua classe-mãe.

### Participantes:
- **Target:** Define a interface específica do domínio que o **Client** usa.
- **Client:** Colabora com objetos compatíveis com a interface do **Target**
- **Adaptee:** Define uma interface existente que necessita ser adaptada.
- **Adapter:** Adapta a interface do Adaptee à interface de **Target** 