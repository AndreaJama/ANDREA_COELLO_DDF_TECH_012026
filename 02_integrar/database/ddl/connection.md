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
