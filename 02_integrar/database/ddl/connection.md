# Etapa 02 – Integração dos Dados

Nesta etapa foi realizada a ingestão dos dados em um banco de dados
PostgreSQL em cloud, simulando uma base transacional real que servirá
como fonte para ingestão na plataforma Dadosfera.

O objetivo foi preparar os dados seguindo boas práticas de ELT,
com separação entre camada de staging e camada refinada.

# PostgreSQL em Cloud – Supabase

Para atender ao bônus do case, foi utilizado o Supabase como serviço
gerenciado de PostgreSQL em cloud.

## Configuração do Banco

- Serviço: Supabase
- Banco: PostgreSQL
- Região: AWS us-east
- Plano: Free
- Schema: public

## Método de Conexão

Foi utilizado o **Transaction Pooler**, pois:
- É compatível com IPv4
- Funciona no plano gratuito
- Recomendado para integrações externas

### Parâmetros de Conexão

Host:
aws-1-us-east-2.pooler.supabase.com

Porta:
6543

Database:
postgres

Usuário:
postgres.<project_id>
