# Design e Arquitetura de Software 2
## Bruno Richartz Farias

### Aula 27/02/2025
Design tradeoffs
- Consistência: Dados gravados são salvos corretamente
- Durabilidade: Informação gravada é mantida
- Espaço: Armazenamento não é infinito e não é mais caro, permitindo utilizar bancos menos eficientes em questão de espaço sem problemas
- Escalabilidade: É necessário aumentar a quantidade de máquinas de forma rápida para suprir altas demandas temporárias ou permanentes

ClowdWatch detecta quedas e o EC2 sobe novas para substituir

Infrastructure as code: Scripts que montam e provisionam máquinas automaticamente

Tratar recursos como descartáveis: Não pode dar nome carinhoso pra servidor / A infraestrutura deve ser capaz de recriar servidores defeituosos