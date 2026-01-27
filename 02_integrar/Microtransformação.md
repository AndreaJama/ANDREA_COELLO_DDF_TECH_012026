## Bônus – Microtransformação com PostgreSQL

Como bônus do case, foi criada uma pipeline de ingestão a partir de um
banco de dados PostgreSQL em cloud (Supabase), simulando uma base
transacional real.

Durante a configuração da pipeline na Dadosfera, foi aplicada uma
microtransformação do tipo **Hash** sobre a coluna `VendorID`, com o
objetivo de anonimizar identificadores sensíveis mantendo consistência
entre registros repetidos.

Essa abordagem demonstra a aplicação do paradigma **ELT**, no qual os
dados são carregados primeiro e transformados de forma controlada,
garantindo governança, privacidade e rastreabilidade dos dados.

