import requests
import warnings
import urllib3
import time
import os


from Movidesk import HelpdeskMovidesk
from From_to import FromTo
from connection_bd import Database
import clients_data

warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore", category=UserWarning)

movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
movidesk_destin = HelpdeskMovidesk(clients_data.token_movidesk_destin)

top = clients_data.top
skip = clients_data.skip
page = clients_data.page
step = clients_data.step

# Criar banco e tabelas
bd = Database()
created_database = bd.created_database()
created_table = bd.created_table()

while True:
    cod_ref_persons = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[0]
    status_code = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[1].status_code
    text_requests = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[1].text
    url = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[2]
    patch_count = 0
    start_time = time.time()
    if status_code != 200 or not cod_ref_persons:
        break

    for person_origin in cod_ref_persons:
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
                # "slaAgreement": org.get('slaAgreement'),
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
        #     [
        #     {
        #         "id": asset.get('id'),
        #         "name": asset.get('name'),
        #         "label": asset.get('label')
        #     }
        #     for asset in person_origin_at_assets
        # ]

        # Mapeia o perfil de acesso, classificação, grupos e custom-fields do destino
        from_to = FromTo()
        persons_destin_access_profile = from_to.from_to_access_profile(person_origin_id)
        persons_destin_classification = from_to.from_to_classification(person_origin_id)
        persons_destin_teams = from_to.from_to_group_persons(person_origin_id)
        person_destin_custom_field_values = from_to.from_to_custom_fields_persons(person_origin_id)
        # Cria o dicionário de dados para inserção
        data = {
            "id": person_origin_id,
            "codeReferenceAdditional": person_origin_code_reference_additional,
            "isActive": True,  # person_origin_is_active,
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
        person_exists = bd.person_exists_bd(data['id'])
        not_migrated = bd.get_not_migrated_records()
        if person_exists and step ==1:
            print(f"A pessoa de cód.ref. {person_origin_id} já existe no banco de dados do Migrador")
        elif not_migrated == [] and step == 5:
            print(f"Não há pessoas para remigrar no banco de dados!")
            break
        elif not_migrated != [] and step == 5:
            remigrated = bd.get_not_migrated_records()
            for not_migrated in remigrated:
                bd.retry_migration()
                print("Pessoas remigradas com sucesso")
            break

        else:
            if step != 5:
                insert_bd_persons = bd.insert_date_persons(data, movidesk_destin.person_validation(person_origin_id), None)
                print(f"Pessoa inserida no banco do migrador com sucesso!")

                # Post na base Movidesk
                response = movidesk_destin.post_persons_movidesk(id_persons=person_origin_id, data=data)
                if response.status_code == 200:
                    print("Pessoa inserida na base Movidesk com sucesso!")
                    bd.update_migrated_persons(data['id'], 1, None)

                else:
                    error_message = response.text
                    print(f"Erro ao inserir na base Movidesk a pessoa de cód.ref {person_origin_id}. Erro: {error_message}")
                    bd.update_migrated_persons(data['id'], 0, error_message)
                    patch_count += 1
                    record = f'{patch_count} - ERRO: A pessoa de id: {person_origin_id} NÃO FOI MIGRADA. Erro: {error_message}'
                    movidesk_destin.write_record(file_path='files/log.txt', record=record)
    if step == 1:
        print(f'Para migrar 100 pessoas demorou: {time.time() - start_time}')
        insert_bd_persons_migration_history = bd.insert_date_persons_migration_history(clients_data.person_type, top,
                                                                                       skip,
                                                                                       page, url)
        skip += top
        page += 1
    else:
        print("Remigração finalizada.")
        print(f'Para Remigrar pessoas demorou: {time.time() - start_time}')
        break


input("Pressione Enter para sair...")

