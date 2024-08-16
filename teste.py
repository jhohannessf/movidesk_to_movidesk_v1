import requests
import warnings
import urllib3
import time

from concurrent.futures import ThreadPoolExecutor, as_completed
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


def consulta_api(person_origin):
    person_origin = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[0]
    status_code = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[1].status_code
    text_requests = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[1].text
    url = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[2]
    patch_count = 0
    start_time = time.time()
    for person in person_origin:
        if status_code == 200:
            return person
        else:
            return None


def de_para(person_origin):
    person = consulta_api(person_origin)
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
    # De-Para
    from_to = FromTo()
    persons_destin_access_profile = from_to.from_to_access_profile(person_origin_id)
    persons_destin_classification = from_to.from_to_classification(person_origin_id)
    persons_destin_teams = from_to.from_to_group_persons(person_origin_id)
    person_destin_custom_field_values = from_to.from_to_custom_fields_persons(person_origin_id)
    person_destin_at_assets = []
    data_destin = {
        "id": person_origin_id,
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
    return data_destin

bd = Database()

while True:
    person_origin = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[0]
    status_code = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[1].status_code
    text_requests = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[1].text
    url = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[2]
    patch_count = 0
    start_time = time.time()
    if status_code != 200 or not person_origin:
        break
    b = consulta_api(person_origin)
    a = de_para(b)
    bd = Database()
    person_exists = bd.person_exists_bd(a['id'])
    person_not_migrated = bd.get_not_migrated_records()
    if person_exists and step == 1:
        print(f"A pessoa de cód.ref. {person_origin} já existe no banco de dados do Migrador")
    elif person_not_migrated and step == 5:
        migrated = bd.get_not_migrated_records()
        for not_migrated in migrated:
            bd.retry_migration()
            print("Pessoas remigradas com sucesso")
            # AQUI PRECISA TER UM BREAK PARA PARAR O LAÇO
    else:
        insert_bd_persons = bd.insert_date_persons(a, movidesk_destin.person_validation(person_origin), None)
        print(f"Pessoa inserida no banco do migrador com sucesso!")

print(f'Para migrar 100 pessoas demorou: {time.time() - start_time}')

if step == 1:
    insert_bd_persons_migration_history = bd.insert_date_persons_migration_history(clients_data.person_type, top, skip,
                                                                                   page, url)
    skip += top
    page += 1
else:
    print("Remigração finalizada.")




#     response = requests.post(post_url, json=mapped_data)
#     return response.status_code
# api_urls = ["http://example.com/api/resource/{}".format(i) for i in range(100)]
# post_url = "http://example.com/api/destination"
# with ThreadPoolExecutor(max_workers=10) as executor:
#     # Fase 1: Consultas e Armazenamento
#     future_to_data = {executor.submit(consulta_api, url): url for url in api_urls}
#     stored_data = []
#     for future in as_completed(future_to_data):
#         data = future.result()
#         if data:
#             stored_data.append(data)
#     # Fase 2: Processamento e Postagem
#     future_to_post = {executor.submit(processa_e_posta, data, post_url): data for data in stored_data}
#     for future in as_completed(future_to_post):
#         status_code = future.result()
#         if status_code == 200:
#             print("Dados postados com sucesso!")
#         else:
#             print(f"Erro ao postar dados: {status_code}")