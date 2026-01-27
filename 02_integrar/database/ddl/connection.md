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

# Problemas Encontrados e Soluções

Durante a carga dos dados, alguns problemas de tipagem foram identificados
e corrigidos, o que reforça o caráter realista do case.

---

## Erro 1 – Formato de Data/Hora

Erro:
ERROR: date/time field value out of range

Causa:
Datas no CSV estavam como texto.

Solução:
Conversão explícita usando TO_TIMESTAMP.

Exemplo:
TO_TIMESTAMP(tpep_pickup_datetime, 'YYYY-MM-DD HH24:MI:SS')

---

## Erro 2 – Tipos Numéricos Incompatíveis

Erro:
ERROR: invalid input syntax for type smallint: "2.0"

Causa:
Campos inteiros vinham como texto com casas decimais.

Solução:
Uso de CAST explícito para INTEGER.

Exemplo:
CAST(vendorid AS INTEGER)
CAST(passenger_count AS INTEGER)
CAST(ratecodeid AS INTEGER)
