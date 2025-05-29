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

### Aula 20/03/2025

- S3 possui durabilidade e disponibilidade de 99,99%;
- Usos do S3: sites estáticos, picos de demanda, recuperação de desastres, armazenamento de dados para análise
- Storage gateway: servidor que serve como buffer, dados gravados nele são mandados para o s3
- Multipart upload: arquivos grandes (mais de 5TB) são armazenados no S3 em múltiplas partes, o arquivo é dividido em partes de tamanhos iguais e enviados para o S3
- Direct connect: usa cloudfront edge locations para criar caminhos mais curtos para acessar o S3. Diminui a latência por não entrar na internet pública
- Transfer family: permite enviar e receber do s3 sem ter que alterar o protocolo de transferência de arquivos do seu software
- Storage classes: formas como o S3 guarda a informação, definem o preço e disponibilidade:
- Classes quentes: acesso imediato ao objeteto armazenado:
- Standard: caro para armazenar, barato para baixar
- Standard-IA (infrequent access): mais barato para armazenar, mais caro para baixar. Server para arquivos pouco acessados
- One zone-IA: faz apenas uma cópia do objeto ao invés de 3, tornando armazenamento mais barato
- Intelligent-tiering: Arquivos são monitorados no s3 e são movidos para a classe mais apropriada, dependendo de fatores, como frequência de acesso
- Classes frias: objetos precisam ser recuperados:
- Há períodos mínimos para manter arquivos e custos extras são aplicados se baixar antes desse tempo
- Glacier deep archive: armazenamento offline, arquivos podem demorar de 12 a 48 horas para serem recuperados, é mais barato para armazenar
- Glacier flexible retrieval: é mais rápido para baixar e mais caro que o deep archive
- Glacier instant retrieval: arquivo disponível instantaneamente, mas precisa passar por reidratação para ser usado
- Outposts: Leva servidores da AWS fisicamente para dentro das empresas, aparece como uma região da própria empresa no console

### Aula 24/03/2025

- Ciclo de vida S3: Definir um período de tempo que após ser excedido, algo é feito com os dados, como: Mover de classe ou apagar
- Versionamento do S3: Não é possível desabilitar após habilitado, pode apenas ser pausado.
- Ao fazer upload de um objeto com a mesma chave ele mantém a chave do objeto e cria um id de versão diferente
- Ao deletar ele cria uma versão marcando o arquivo como apagado, para restaurar o arquivo basta apagar a versão com o marcador
- CORS: é uma proteção para os arquivos do site. Ocorre quando um site tenta consumir dados de outro site e o outro site não permite o acesso
- Todo bucket é privado e criptografado por padrão

### Aula 03/04

- EC2: Elastic compute Cloud, permite criar e hospedar sistemas de software com capacidade computacional redimencionável
- Serve para qualquer coisa que necessite de um servidor
- AMI, uma "foto" do servidor, permitindo criar cópias idênticas do servidor original. Serve para recuperação e repetição
- EBS: Armazenamento persistente na EC2, diferente da instance store no host, que só armazena arquivos temporariamente
- quanto menos gerenciado, mais controle
- (menos gerenciado) Vms, Containers, VPS, PaaS, Serverless (mais gerenciado)
- Compute optimizer: IA que recomenda recursos de computação da AWS mais eficientes para workloads, tem versão gratuita e paga
- File share: usar FSx para Windows, EFS para Linux

### Aula 07/04

- Intence metadata: funciona como uma API rest, em um IP que só funciona na AWS. Usado para perguntar para a AWS coisas que o servidor não sabe
- HPC: cluster, colocar todas as máquinas na mesma AZ e se possível no mesmo rack. Reduz latência
- Spread é o oposto, colocar tudo o mais longe o possível para mais disponibilidade
- Partition: Os dados não ficam no mesmo servidor, mas os servidores estão próximos. Um meio termo. Usa ou Apache Kafka, Apache Cassandra, ou Apache Spark
- EC2 free tier: EC2 de graça nos 12 primeiros meses
- EC2 modelos: 
- on-demand (tudo sempre disponível, mais caro)
- reserved (especificar tudo e usar apenas isso por 1 ou 3 anos)
- saving plans (mais flexível que o reserved mas cobrança por hora)
- EC2 Spot (usar máquinas que não estão em uso na AWS, mas podem ser pedidas de volta)
- Segurança não pode depender de ação manual, abrir portas corretas do firewall, usar tamanho de máquina correto, escolher modelo de precificação correto, evitar desperdício

### Aula 10/04/2025

- Considerações para criar um banco de dados: Escalabilidade, Quantidade de espaço de armazenamento necessário, Características dos dados e durabilidade
- Amazon RDS: Serviço de banco de dados relacionais gerenciados da Amazon
- Amazon DynamoDB, Amazon Neptune e Amazon ElastiCache: Serviços de banco de dados não relacionais gerenciados da Amazon
- Amazon Aurora: Banco de dados relacionar que simula um MySQL(sendo 5x mais rápido) ou Postgres(sendo 3x mais rápido)
- Amazon Aurora Serverless: Capaz de ligar e desligar sozinho

### Aula 17/04/2025

- Connection pooling: melhora a escalabilidade por meio de um rds proxy entre a aplicação e o BD, evitando a exaustão do servidor devivo às várias conexões
- Backups no RDS: automatizado (faz a cada 5 dias, retenção de 7 a 35 dias), snapshot (manual, retenção perpétua)
- KMS: key management system, cofre de chaves
- Chave simétrica: a mesma chave que criptografa é a que descriptografa
- Chave assimétrica: as chaves que criptografam e descriptografam são diferentes
- DynamoDB: BD NoSQL, serverless, performance de um dígito de milisegundo. Ideal para arquitetura baseada em eventos. Ativo/ativo. Critpografia automática padrão, usa IAM roles para autenticar acesso
- Redshift: BD para data warehouse, para pesquisas pesadas e históricas
- Outros DBs disponibilizados na AWS: DocumentDB, Keyspaces, MemoryDB Neptune, Timestream, Quantum Ledger

### Aula 05/05/2025

- VPC: Virtual Private Cloud: Pertence a apenas uma região e fica isolada nela | É possível definir a velocidade máxima do tráfego
- CIDR: Como a máscara de rede, ele define o tamanho da rede
- Subnet pública: Os recursos dela estão disponíveis pra internet de dentro pra fora e de fora pra dentro 

### Aula 08/05/2025

- Máquinas em uma VPC que não tem acesso à internet não conseguem baixar nada, é necessário uma máquina para intermediar a comunicação. (NAT device instance e NAT gateway)
- Banco de dados: VPC privada
- Batch-processing instances: VPC privada
- Instâncias de aplicações web: VPC pública
- Instâncias de NAT gateway: VPC pública
- Security group: Usado para definir quem possui permissão de acessar o que
- Network ACL: Valida a permissão na entrada e na saída
- AWS Network Firewall: Servidor de firewall que pode ser utilizado em uma subnet especial, é usado para controlar as regras de entrada e saída para a internet
- VPC flow logs: log de tentativa de conexão 

### Aula 19/05/2025

- AWS Transit Gateway: roteador central, conectar todos os vpcs nele para resolver conexões mais facilmente. serviço regional capaz de se conectar com 5000 "coisas"
- Topologia Full Mesh: todas as vpcs falam entre sí
- Topologia Hub and Spoke (shared vpc): hub com serviços compartilhados que se conecta com todas as vpcs
- Transit Gateway: ajuda a criar essas topologias, seviço pago e regional. Cria até 5000 conexões
- Vcp Peering: conexão entre vpcs, gratúito se ambas estão na mesma região, pago senão
- Direct Connect: conexão exclusiva criada por meio de um circúito do servidor da região até você

### Aula 19/05/2025

- IAM groups: criar um conjunto de permissões e atribuir usuários à esse grupo, simplificando o gerenciamento de permissões
- RBAC: Tipo de permissão onde é criado um papel que um usuário pode assumir temporariamente
- ABAC: Permite definir permissões com base em atributos associados a um grupo
- Amazon Cognito: Serviço que provê autenticação, autorização, e gerenciamento de usuários

### Aula 29/05/2025

- Empresas se organizam com apenas uma conta para a empresa toda ou uma conta para cada equipe e organizam as equipes em árvores subordinadas à conta principal
- AWS Organizations é uma ferramenta para gerir multiplas contas da AWS no caso dessas empresas
- Conta root envia convites para outras contas, formando uma hierarquia de contas. O que dá acesso ao billing consolidado do AWS Organizations
- AWS Control Tower: Cria uma estrutura completa da AWS usando as melhores práticas, ideal para grandes organizações
- Confiabiliade, integridade e disponibilidade. Sempre 1 é sacrificado para garantir as outras
- AWS Key management service: cria e administra chaves de criptografia
- Amazon Macie: varredura de arquivos para encontrar dados com informações sensíveis
- Amazon inspector: Encontra vulnerabilidades conhecidas em EC2 e ECR
- 
