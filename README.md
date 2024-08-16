# movidesk_to_movidesk
Versão 1.0.0

Este projeto faz a Migração de pessoas (clientes, agentes e empresas) entre bases Movidesk usando API.

## Uso

* Baixar a ultima versão [aqui](https://github.com/jhohannesfreitas/movidesk_to_movidesk/releases)
* Descompacte o arquivo em qualquer local no computador. Execute na VM ou precisará usar a API Pública.
* Preencha o arquivo `.env`
* Executar o arquivo `persons_paralelismo.exe`
* O Migrador utiliza banco de dados `postgres` para armazenar o historico de migração e os passos executados
    * Baixar a ferramenta dbeaver ou o próprio [Postgres](https://www.postgresql.org/download/) 
    * A conexão com o banco deve ser: host="localhost", database="postgres", user="postgres", password="postgres"
    * Tabelas
       - persons - armazena o historico de pessoas enviadas, a coluna `migrated` indica se o registro foi enviado
       - persons_migration_history - historico de migração
          - armazena paginação e filtro criado no momento da migração
          - se o migrador fechar, você precisa consultar a última query que parou e ajustar no arquivo `.env` qual o skip e page seguinte.
          - obs: diferente dos registros de pessoas, as páginas podem se repetir caso você não altere no arquivo `.env`
* Logs - Todos os logs de erros são salvos na pasta  /files/log.txt

* Migrado de Tickets - versão 2.0.0" - (EM ANDAMENTO)
  * tickets - armazena o historico de tickets enviados, a coluna `migrated` indica se o registro foi enviado
  * actions - ações dos tickets que contem imagens enbed no corpo da ação
  * attachments - anexos dos tickets enviados 
  * filecache - cache de arquivos que ja foram enviados para a s3 para evitar duplicidade de arquivos
  * tickets_migration_history - historico de migração
   * armazena paginação e filtro criado no momento da migração
   * se o migrador fechar, a ultima query será usada para continuar a migração de onde parou 
   * obs: para reprocessar do zero, apague os registros da tabela
  
* Logs - Todos os logs de erros são salvos na pasta  /files/log.txt


* Steps

   * 1 - Migrar pessoas
   * 2 - Migrar tickets (somente na V 2.0.0)
   * 3 - Enviar Anexos (somente na V 2.0.0)
   * 4 - Corrigir imagens enbedadas na descrição da action (valido apenas para migrações executadas no passo 2) (somente na V 2.0.0)
   * 5 - Reenviar pessoas com erros  (valido apenas para migrações executadas no passo 1) 
   * 6 - Reenviar tickets com erros (valido apenas para migrações executadas no passo 2) (somente na V 2.0.0)
   * 7 - Corrigir imagens enbedadas via banco de dados (Busca em tempo real no db do movidesk) (somente na V 2.0.0)


 * .ENV

* Parâmetros de origem
  
   * database = "" #Informe o nome do banco entre as aspas.
   * movidesk_url_api = "https://movidesk-api.internal/public/v1/"
   * token_movidesk_origin = "" # Token origem
   * token_movidesk_destin = "" # Token Destino
   * tenant_id_origin = "" # Tenant Origem
   * tenant_id_destin = "" # Tenant Destino

* Parâmetros de execução
  
   * person_type = 2 # Tipo da pessoa. Pessoa = 1, Empresa = 2, Departamento = 4.
   * profile_type = 2 # Tipo do perfil. Agente = 1, Cliente = 2, Agente e Cliente = 3.
   * top = 100
   * skip = 0
   * page = 1
   * step = 1 # 1= Migrar pessoas; 2= Migrar tickets ; 5= Remigrar pessoas; 6= Remigrar tickets

  
