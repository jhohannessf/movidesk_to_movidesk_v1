import requests
import pandas as pd
import psycopg2
import warnings
import urllib3
import json
from datetime import datetime

from Movidesk import HelpdeskMovidesk
import clients_data

from From_to import FromTo
import clients_data

warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore", category=UserWarning)


class Database:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database=clients_data.database,
                user="postgres",
                password="postgres"
            )
            print("Conexão com o banco de dados estabelecida com sucesso.")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.conn = None

    def created_database(self):
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgres")
        cur = conn.cursor()
        conn.set_isolation_level(0)
        database = clients_data.database
        # Consulta SQL para verificar se o banco de dados já existe
        check_database_query = f"SELECT datname FROM pg_database WHERE datname = '{database}'"
        # Execute a consulta para verificar a existência do banco de dados
        cur.execute(check_database_query)
        # Recupere o resultado da consulta
        resultado = cur.fetchone()
        # Se o banco de dados não existe, crie-o
        if resultado is None:
            create_database_query = f"CREATE DATABASE {database}"
            cur.execute(create_database_query)
            cur.close()
            conn.close()
            print(f"Banco de dados '{database}' criado com sucesso.")
        else:
            print(f"O banco de dados '{database}' já existe e não foi criado novamente.")
            cur.close()
            conn.close()

    def created_table(self):
        conn = psycopg2.connect(host="localhost", database=clients_data.database, user="postgres", password="postgres")
        cur = conn.cursor()
        create_table_query = """
            CREATE TABLE IF NOT EXISTS persons (
                Id text,
                TenantIdOrigin text,
                TenantIdDestin text,
                Migrated int4,
                Erro text,
                Data text,
                Reprocessed bool,
                GetDateOrigin timestamp,
                QueryDateOrigin timestamp,
                MigratedIn timestamp
            );
            CREATE TABLE IF NOT EXISTS persons_migration_history (
                PersonType int4,
                Top int4,
                Skip int4,
                Page int4,
                URL text,
                TenantIdOrigin text,
                TenantIdDestin text
            );
            CREATE TABLE IF NOT EXISTS tickets (
                Id uuid,
                OriginTicketId int4,
                MovideskTicketId int4,
                TenantIdOrigin text,
                TenantIdDestin text,
                MovideskTicketSequence int4,
                Migrated int4,
                Data text,
                Reprocessed bool,
                GetDateOrigin timestamp,
                QueryDateOrigin timestamp,
                MigratedIn timestamp
            );
            CREATE TABLE IF NOT EXISTS tickets_migration_history (
                Id uuid,
                Page int4,
                Query text,
                StartAt timestamp,
                EndAt timestamp,
                TenantIdOrigin text,
                TenantIdDestin text
            );
            CREATE TABLE IF NOT EXISTS actions (
                Id uuid,
                TicketNumber int4,
                ActionNumber int4,
                TenantIdOrigin text,
                TenantIdDestin text,
                Migrated int4,
                Data text,
                Reprocessed bool,
                GetDateOrigin timestamp,
                QueryDateOrigin timestamp,
                MigratedIn timestamp
            );
            CREATE TABLE IF NOT EXISTS attachments (
                Id uuid,
                TicketNumber int4,
                ActionNumber int4,
                Sequence int4,
                TenantIdOrigin text,
                TenantIdDestin text,
                AttachmentUrl text,
                Migrated int4,
                Data text,
                Reprocessed bool,
                GetDateOrigin timestamp,
                QueryDateOrigin timestamp,
                MigratedIn timestamp
            );
            """
        # Execute a consulta para criar a tabela
        cur.execute(create_table_query)
        print(f"Tabelas criadas com sucesso!")
        # Faça commit das alterações no banco de dados
        conn.commit()
        cur.close()
        conn.close()

    def insert_date_persons(self, data, response, error_message):
        conn = psycopg2.connect(host="localhost", database=clients_data.database, user="postgres", password="postgres")
        cur = conn.cursor()
        id = data['id']
        tenant_id_origin = clients_data.tenant_id_origin
        tenant_id_destin = clients_data.tenant_id_destin
        migrated = 0
        data_string = json.dumps(data)
        cur.execute("SELECT Migrated FROM persons WHERE Id = %s", (id,))
        result = cur.fetchone()

        # Inicializa reprocessed como False
        reprocessed = False
        if result:
            old_migrated = result[0]
            # Atualiza reprocessed se migrated mudar de 0 para 1
            if old_migrated == 0 and migrated == 1:
                reprocessed = True
        get_date_origin = data.get('createdDate', None)
        query_date_origin = data.get('changedDate', None)
        migrated_in = datetime.now()  # datetime.date.today())

        insert_data_query_persons = """
                   INSERT INTO persons (Id, TenantIdOrigin, TenantIdDestin, Migrated, Erro, Data, Reprocessed, GetDateOrigin,
                   QueryDateOrigin, MigratedIn)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
               """
        try:
            cur.execute(insert_data_query_persons, (id, tenant_id_origin, tenant_id_destin, migrated, error_message,
                                                    data_string, reprocessed, get_date_origin, query_date_origin,
                                                    migrated_in))
            conn.commit()
        except Exception as e:
            print(f"Erro durante a execução da consulta: {e}")

    def insert_date_persons_migration_history(self, person_type, top, skip, page, url):
        conn = psycopg2.connect(host="localhost", database=clients_data.database, user="postgres", password="postgres")
        cur = conn.cursor()
        # id = data['id']
        tenant_id_origin = clients_data.tenant_id_origin
        tenant_id_destin = clients_data.tenant_id_destin
        insert_data_query_persons_migration_history = """
        INSERT INTO persons_migration_history (PersonType, Top, Skip, Page, 
        URL, TenantIdOrigin, TenantIdDestin) VALUES (%s, %s, %s, %s, %s, %s, %s);
        """
        try:
            cur.execute(insert_data_query_persons_migration_history, vars=(person_type, top, skip, page, url,
                                                                           tenant_id_origin, tenant_id_destin))
            conn.commit()
        except Exception as e:
            print(f"Erro durante a execução da consulta: {e}")

    def update_migrated_persons(self, person_id, migrated, error_message):
        conn = psycopg2.connect(host="localhost", database=clients_data.database, user="postgres", password="postgres")
        if not conn:
            print("Conexão com o banco de dados não está disponível.")
            return

        try:
            cur = conn.cursor()
            query = """
                        UPDATE persons
                        SET Migrated = %s, Erro = %s
                        WHERE Id = %s
                    """
            cur.execute(query, (migrated, error_message, person_id))
            conn.commit()
            cur.close()
            print(f"Status de migração atualizado para o id '{person_id}'")

        except Exception as e:
            print(f"Erro ao atualizar status de migração no banco de dados: {e}")

    def get_not_migrated_records(self):
        if not self.conn:
            print("Conexão com o banco de dados não está disponível.")
            return []

        try:
            cur = self.conn.cursor()
            query = "SELECT Id, Data FROM persons WHERE Migrated = 0"
            cur.execute(query)
            records = cur.fetchall()
            cur.close()

            # Debugging output
            print(f"Registros não migrados encontrados: {records}")

            return records

        except Exception as e:
            print(f"Erro ao buscar registros não migrados: {e}")
            return []

    def retry_migration(self):
        # Assume que `self` é uma instância da classe `Database` já conectada.
        records = self.get_not_migrated_records()
        movidesk_destin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
        patch_count = 0

        for person_id, data in records:
            try:
                # Converte os dados para JSON
                data_json = json.loads(data)

                # Faz o POST para a API de destino
                response = movidesk_destin.post_persons_movidesk(id_persons=person_id, data=data_json)

                if response.status_code == 200:
                    # Atualiza o status como migrado se a resposta for bem-sucedida
                    self.update_migrated_persons(person_id, migrated=1, error_message="Pessoa Remigrada")
                    self.update_reprocessed_persons(person_id, reprocessed=True, error_message="Pessoa Remigrada")
                else:
                    # Atualiza o status com a mensagem de erro
                    error_message = response.text
                    self.update_migrated_persons(person_id, migrated=0, error_message=error_message)

                    if error_message == '[{"errorMessage":"The ID entered already exists","propertyName":"Id"}]':
                        self.update_migrated_persons(person_id, migrated=1, error_message="Pessoa Remigrada")
                        self.update_reprocessed_persons(person_id, reprocessed=True, error_message="Pessoa Remigrada")

                    # Incrementa o contador e faz o logging do erro
                    patch_count += 1
                    record = f'{patch_count} - ERRO: A pessoa de id: {person_id} NÃO FOI REMIGRADA. Erro: {error_message}'
                    movidesk_destin.write_record(file_path='files/log.txt', record=record)

            except Exception as e:
                # Atualiza o status com a mensagem de erro em caso de exceção
                self.update_migrated_persons(person_id, migrated=0, error_message=str(e))

        # Fecha a conexão com o banco de dados
        self.close_connection()

    def update_reprocessed_persons(self, person_id, reprocessed, error_message):
        conn = psycopg2.connect(host="localhost", database=clients_data.database, user="postgres", password="postgres")
        cur = conn.cursor()
        update_query = """
            UPDATE persons
            SET Reprocessed = %s, Erro = %s
            WHERE Id = %s;
        """
        try:
            cur.execute(update_query, (reprocessed, error_message, person_id))
            conn.commit()
        except Exception as e:
            print(f"Erro durante a atualização da consulta: {e}")
        finally:
            cur.close()
            conn.close()

    def person_exists_bd(self, person_id):
        conn = psycopg2.connect(host="localhost", database=clients_data.database, user="postgres", password="postgres")
        if not conn:
            print("Conexão com o banco de dados não está disponível.")
            return False

        try:
            cur = conn.cursor()
            query = "SELECT 1 FROM persons WHERE Id = %s LIMIT 1"
            cur.execute(query, (person_id,))
            exists = cur.fetchone() is not None
            cur.close()

            # Debugging output
            print(f"Verificação de existência para o id '{person_id}': {exists}")

            return exists

        except Exception as e:
            print(f"Erro ao verificar existência da pessoa no banco de dados: {e}")
            return False


    def get(self, param):
        pass

    def close_connection(self):
        if self.conn:
            self.conn.close()


class PersonProcessor:
    def __init__(self, db, stop_event):
        self.db = db
        self.stop_event = stop_event

    def process_person_origin(self, person_origin):
        self.person_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)

        if self.stop_event.is_set():
            return
        person_origin_id = person_origin.get('id')
        person_origin_code_reference_additional = person_origin.get('codeReferenceAdditional')
        person_origin_is_active = person_origin.get('isActive')
        person_origin_person_type = person_origin.get('personType')
        person_origin_profile_type = person_origin.get('profileType')
        person_origin_access_profile = person_origin.get('accessProfile')
        person_origin_business_name = person_origin.get('businessName')
        person_origin_business_branch = person_origin.get('businessBranch')
        person_origin_corporate_name = person_origin.get('corporateName')
        person_origin_cpf_cnpj = person_origin.get('cpfCnpj')
        person_origin_user_name = person_origin.get('userName')
        person_origin_password = person_origin.get('password', None)
        person_origin_role = person_origin.get('role')
        person_origin_boss_id = person_origin.get('bossId')
        person_origin_boss_name = person_origin.get('bossName')
        person_origin_classification = person_origin.get('classification')
        person_origin_culture_id = person_origin.get('cultureId')
        person_origin_time_zone_id = person_origin.get('timeZoneId')
        person_origin_created_date = person_origin.get('createdDate')
        person_origin_created_by = person_origin.get('createdBy')
        person_origin_changed_date = person_origin.get('changedDate')
        person_origin_changed_by = person_origin.get('changedBy')
        person_origin_observations = person_origin.get('observations')
        person_origin_authenticate_on = person_origin.get('authenticateOn')
        person_origin_addresses = person_origin.get('addresses', [])
        person_origin_contacts = person_origin.get('contacts', [])
        person_origin_emails = person_origin.get('emails', [])
        person_origin_teams = person_origin.get('teams', [])
        person_origin_relationships = person_origin.get('relationships', [])
        person_origin_custom_field_values = person_origin.get('customFieldValues', [])
        person_origin_at_assets = person_origin.get('atAssets', [])
        person_destin_relationships = [
            {
                "id": org.get('id'),
                "name": org.get('name'),
                "slaAgreement": None,
                "forceChildrenToHaveSomeAgreement": org.get('forceChildrenToHaveSomeAgreement'),
                "allowAllServices": org.get('allowAllServices'),
                "includeInParents": org.get('includeInParents'),
                "loadChildOrganizations": org.get('loadChildOrganizations'),
                "services": org.get('services'),
                "idToDelete": org.get('idToDelete', None),
                "isGetMethod": org.get('isGetMethod')
            }
            for org in person_origin_relationships
        ]
        person_destin_custom_field_values = [
            {
                "customFieldId": field.get('customFieldId'),
                "customFieldRuleId": field.get('customFieldRuleId'),
                "line": field.get('line'),
                "value": field.get('value'),
                "items": [
                    {
                        "personId": item.get('personId'),
                        "clientId": item.get('clientId'),
                        "team": item.get('team'),
                        "customFieldItem": item.get('customFieldItem'),
                        "storageFileGuid": item.get('storageFileGuid'),
                        "fileName": item.get('fileName')
                    }
                    for item in field.get('items', [])
                ]
            }
            for field in person_origin_custom_field_values
        ]

        person_destin_at_assets = []
        return person_origin

    def process_person_destin(self, person_origin):
        from_to = FromTo()
        persons_destin_access_profile = from_to.from_to_access_profile(person_origin)
        persons_destin_classification = from_to.from_to_classification(person_origin)
        persons_destin_teams = from_to.from_to_group_persons(person_origin)
        person_destin_custom_field_values = from_to.from_to_custom_fields_persons(person_origin)
        a = self.process_person_origin(person_origin)
        data = {
            "id": a.person_origin_id,
            "codeReferenceAdditional": person_origin_code_reference_additional,
            "isActive": person_origin_is_active,
            "personType": person_origin_person_type,
            "profileType": person_origin_profile_type,
            "accessProfile": persons_destin_access_profile,
            "businessName": person_origin_business_name,
            "businessBranch": person_origin_business_branch,
            "corporateName": person_origin_corporate_name,
            "cpfCnpj": person_origin_cpf_cnpj,
            "userName": person_origin_user_name,
            "password": person_origin_password,
            "role": person_origin_role,
            "bossId": person_origin_boss_id,
            "bossName": person_origin_boss_name,
            "classification": persons_destin_classification,
            "cultureId": person_origin_culture_id,
            "timeZoneId": person_origin_time_zone_id,
            "createdDate": person_origin_created_date,
            "createdBy": person_origin_created_by,
            "changedDate": person_origin_changed_date,
            "changedBy": person_origin_changed_by,
            "observations": person_origin_observations,
            "authenticateOn": person_origin_authenticate_on,
            "addresses": [
                {
                    "addressType": address.get('addressType'),
                    "country": address.get('country'),
                    "postalCode": address.get('postalCode'),
                    "state": address.get('state'),
                    "district": address.get('district'),
                    "city": address.get('city'),
                    "street": address.get('street'),
                    "number": address.get('number'),
                    "complement": address.get('complement'),
                    "reference": address.get('reference'),
                    "isDefault": address.get('isDefault'),
                    "countryId": address.get('countryId')
                }
                for address in person_origin_addresses
            ],
            "contacts": [
                {
                    "contactType": contact.get('contactType'),
                    "contact": contact.get('contact'),
                    "isDefault": contact.get('isDefault')
                }
                for contact in person_origin_contacts
            ],
            "emails": [
                {
                    "emailType": email.get('emailType'),
                    "email": email.get('email'),
                    "isDefault": email.get('isDefault')
                }
                for email in person_origin_emails
            ],
            "teams": persons_destin_teams,
            "relationships": person_destin_relationships,
            "customFieldValues": person_destin_custom_field_values,
            "atAssets": person_destin_at_assets
        }

        # Inserir no banco
        person_exists = self.db.person_exists_bd(data['id'])
        if person_exists and step == 1:
            print(f"A pessoa de cód.ref. {person_origin_id} já existe no banco de dados do Migrador")
        elif person_exists and step == 5:
            migrated = self.db.get_not_migrated_records()
            for not_migrated in migrated:
                self.db.retry_migration()
                print("Pessoas remigradas com sucesso")
                self.stop_event.set()
        else:
            insert_bd_persons = self.db.insert_date_persons(data, movidesk_destin.person_validation(person_origin_id), None)
            print(f"Pessoa inserida no banco do migrador com sucesso!")
            # Post na base Movidesk
            response = movidesk_destin.post_persons_movidesk(id_persons=person_origin_id, data=data)
            patch_count = 0
            if response.status_code == 200:
                print("Pessoa inserida na base Movidesk com sucesso!")
                self.db.update_migrated_persons(data['id'], 1, None)
            else:
                error_message = response.text
                print(f"Erro ao inserir na base Movidesk a pessoa de cód.ref {person_origin_id}. Erro: {error_message}")
                self.db.update_migrated_persons(data['id'], 0, error_message)
                patch_count += 1
                record = f'{patch_count} - ERRO: A pessoa de id: {person_origin_id} NÃO FOI MIGRADA. Erro: {error_message}'
                movidesk_destin.write_record(file_path='files/log.txt', record=record)