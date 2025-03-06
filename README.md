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
- Automação do ambiente: IAC - Infrastructure as code, torna o sistema mais estável e confiável, mas pode custar mais e requer desapego, pois as máquinas podem ser susbtituidas a qualquer momento, conforme necessário
- Acoplamento: Alto acoplamento dificulta a recuperação em caso de falhas. Caso o banco de dados caia o sitema vai junto, é necessário desacoplar, por exemplo tendo varias copias do banco de dados e load balancers para distribuir e gerenciar o fluxo de dados
- Escolher a opção de banco correta: banco de dados relacional possui escalabilidade vertical, mais performance necessita de mais recursos de processamento, possui apenas réplicas de leitura. bancos de dados nosql escalam horizontalmente, podendo utilizar réplicas de cópia e escrita para melhorar a performance, também não possui modelo de dados, permitindo mais flexibilidade ao armazenar os dados
- Evitar pontos únicos de falha: Evitar o uso de recursos únicos e de difícil substituição, exemplo: possuir mais de uma cópia do banco pronta para assumir, caso a principal caia
- *Backup de log permite armazenar os comandos aplicados no banco, para replicar no banco de cópia, assim evitando precisar copiar os dados inteiros*
- Otimização de custos: Utilizar apenas os recursos necessários para o funcionamento
- Usar cache: Evitar acessar sempre o banco de dados principal para buscar os mesmos dados que são utilizados com frequencia, vale mais armazenar em um (alguns) banco(s) menor(es) e mais rápido(s) que o usuário demore menos para ter acesso
- Segurança: Princípio do privilégio minimo: Todos não tem acesso a nada que não seja realmente necessário
- Infraestrutura: Sempre tentar aproximar os dados do usuário, para minimizar o tempo de espera
- Local Zone: AZs (Availability Zone) menores para locais onde a demanda não justifica a criação de uma AZ normal
- Wavelength Zone: Um servidor que roda em conjunto à antena 5G para minimizar a latência
- ![alt text](image-1.png)