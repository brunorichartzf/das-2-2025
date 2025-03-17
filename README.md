# Design e Arquitetura de Software 2
## Bruno Richartz Farias

### Aula 27/02/2025
Design tradeoffs
- Consistência: Dados gravados são salvos corretamente
- Durabilidade: Informação gravada é mantida
- Espaço: Armazenamento não é infinito e não é mais caro, permitindo utilizar bancos menos eficientes em questão de espaço sem problemas
- Escalabilidade: É necessário aumentar a quantidade de máquinas de forma rápida para suprir altas demandas temporárias ou permanentes, o que custa mais dinheiro momentaneamente

ClowdWatch detecta quedas e o EC2 sobe novas para substituir

Infrastructure as code: Scripts que montam e provisionam máquinas automaticamente

Tratar recursos como descartáveis: Não pode dar nome carinhoso pra servidor / A infraestrutura deve ser capaz de recriar servidores defeituosos

### Aula 06/03/2025

Design tradeoffs
- Automação do ambiente: IAC - Infrastructure as code, torna o sistema mais estável e confiável, mas pode custar mais e requer desapego, pois as máquinas podem ser substituídas a qualquer momento, conforme necessário
- Acoplamento: Alto acoplamento dificulta a recuperação em caso de falhas. Caso o banco de dados caia o sistema vai junto, é necessário desacoplar, por exemplo tendo varias copias do banco de dados e load balancers para distribuir e gerenciar o fluxo de dados
- Escolher a opção de banco correta: banco de dados relacional possui escalabilidade vertical, mais performance necessita de mais recursos de processamento, possui apenas réplicas de leitura. bancos de dados nosql escalam horizontalmente, podendo utilizar réplicas de cópia e escrita para melhorar a performance, também não possui modelo de dados, permitindo mais flexibilidade ao armazenar os dados
- Evitar pontos únicos de falha: Evitar o uso de recursos únicos e de difícil substituição, exemplo: possuir mais de uma cópia do banco pronta para assumir, caso a principal caia
- *Backup de log permite armazenar os comandos aplicados no banco, para replicar no banco de cópia, assim evitando precisar copiar os dados inteiros*
- Otimização de custos: Utilizar apenas os recursos necessários para o funcionamento
- Usar cache: Evitar acessar sempre o banco de dados principal para buscar os mesmos dados que são utilizados com frequência, vale mais armazenar em um (alguns) banco(s) menor(es) e mais rápido(s) que o usuário demore menos para ter acesso
- Segurança: Princípio do privilégio mínimo: Todos não tem acesso a nada que não seja realmente necessário
- Infraestrutura: Sempre tentar aproximar os dados do usuário, para minimizar o tempo de espera
- Local Zone: AZs (Availability Zone) menores para locais onde a demanda não justifica a criação de uma AZ normal
- Wavelength Zone: Um servidor que roda em conjunto à antena 5G para minimizar a latência



### Aula 10/03/2025

- Edge location: Zonas de cache para acelerar o download de conteúdo
- Regional cache: Local de onde a Edge location busca os dados, que em troca busca das AZs
- Modelo de responsabilidade compartilhada: A responsabilidade pela segurança é compartilhada entre o usuário da nuvem e o provedor de nuvem. Em resumo: Hardware, disponibilidade, armazenamento, etc - Nuvem / Configurações, criptografia, senhas, portas, etc - usuário
- Implementar uma identidade de usuário forte
- Proteger dados em trânsito e em "descanso"
- Aplicar segurança em todas as camadas
- Manter os dados longe das pessoas: impedir que o usuário tenha acesso direto ao banco de dados - utilizar de autenticação para definir o que o usuário pode ver e fazer
- Manter rastreabilidade
- Se preparar para eventos de segurança
- Automatizar práticas de segurança para evitar cometer erros ao criar/editar manualmente
- Princípio do privilégio mínimo: Dar ao usuário acesso apenas ao que é de estrita necessidade para a sua função
- Sempre usar criptografia


### Aula 13/03/2025

- Autenticação: Provar que eu sou quem digo que sou. O que eu sei (usuario e senha), o que sou (biometria) e o que tenho (chave de segurança)
- Usuário é uma credencial
- Sempre habilitar MFA
- Rotacionar o uso das long-term credentials/access keys
- Guardar as credenciais de forma segura
- Nunca usar usuário root para tarefas que outros usuários possam fazer
- Primeira coisa a se fazer com o usuário root é habilitar o MFA
- Não há limite para o que o usuário root pode fazer
- Acesso programático: Uma Role dá uma chave de acesso temporária, permitindo ao usuário ou máquina realizar as ações definidas, enquanto a chave for válida
- Acesso console: acesso direto pelo usuario, normalmente com uma chave que não expira

### Aula 17/03/2025

- RBAC Role Base Access Control: permissões definidas de acordo com o seu papél na empresa/sistema
- Policies são usadas para definir exatamente as permissões de cada usuário.
- Policies de identidade definem permissões baseado em cada usuário
- Policies de recurso definem permissões por meio de documentos - permissão granular
- Todas tem efeito, ação e recurso. Necessário especificar usuário (principal) no caso de policy de recurso.
- Armazenamento em bloco: dados são armazenados em blocos de tamanho fixo
- Armazenamento em arquivos: dados são armazenados em uma estrutura hierarquica
- Armazenamento de objetos: dados são armazenados em objetos baseados em atributos e meta dados
- 

