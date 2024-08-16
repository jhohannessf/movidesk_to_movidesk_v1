import psycopg2
import json
import clients_data
import persons_origin
import requests
import warnings
import urllib3

warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore", category=UserWarning)


def main():
    from Movidesk import HelpdeskMovidesk
    from From_to import FromTo
    from connection_bd import Database

    movidesk_destin = HelpdeskMovidesk(clients_data.token_movidesk_destin)
    # movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)

    log_file = 'files/log.txt'
    patch_count = 0
    top = 100
    skip = 100

    # Criar banco e tabelas
    bd = Database()
    created_database = bd.created_database()
    created_table = bd.created_table()

    for cod in persons_origin.cod_ref_persons:
        log_file = 'files/log.txt'
        patch_count = 0
        cod_ref_origin_request = cod['id']
        cod_ref_origin = str(cod_ref_origin_request.strip())
        name_name_origin = cod['businessName']
        validation_person_destin = movidesk_destin.person_validation(cod_ref_origin)
        if validation_person_destin == 200:
            print(f"Pessoa com cód. ref. {cod_ref_origin} já cadastrada na base de destino!")
        else:
            from_to = FromTo()
            persons_destin_access_profile = from_to.from_to_access_profile(cod_ref_origin)
            persons_destin_classification = from_to.from_to_classification(cod_ref_origin)
            persons_destin_teams = from_to.from_to_group_persons(cod_ref_origin)
            person_destin_custom_field_values = from_to.from_to_custom_fields_persons(cod_ref_origin)

            # o data não está alterando a partir da segunda consulta
            data = {
                "id": getattr(persons_origin, 'person_origin_id', None),
                "codeReferenceAdditional": getattr(persons_origin, 'person_origin_code_reference_additional', None),
                "isActive": getattr(persons_origin, 'person_origin_is_active', None),
                "personType": getattr(persons_origin, 'person_origin_person_type', None),
                "profileType": getattr(persons_origin, 'person_origin_profile_type', None),
                "accessProfile": persons_destin_access_profile,
                "businessName": getattr(persons_origin, 'person_origin_business_name', None),
                "businessBranch": getattr(persons_origin, 'person_origin_business_branch', None),
                "corporateName": getattr(persons_origin, 'person_origin_corporate_name', None),
                "cpfCnpj": getattr(persons_origin, 'person_origin_cpf_cnpj', None),
                "userName": getattr(persons_origin, 'person_origin_user_name', None),
                "password": getattr(persons_origin, 'person_origin_password', None),
                "role": getattr(persons_origin, 'person_origin_role', None),
                "bossId": getattr(persons_origin, 'person_origin_boss_id', None),
                "bossName": getattr(persons_origin, 'person_origin_boss_name', None),
                "classification": persons_destin_classification,
                "cultureId": getattr(persons_origin, 'person_origin_culture_id', None),
                "timeZoneId": getattr(persons_origin, 'person_origin_time_zone_id', None),
                "createdDate": getattr(persons_origin, 'person_origin_created_date', None),
                "createdBy": getattr(persons_origin, 'person_origin_created_by', None),
                "changedDate": getattr(persons_origin, 'person_origin_changed_date', None),
                "changedBy": getattr(persons_origin, 'person_origin_changed_by', None),
                "observations": getattr(persons_origin, 'person_origin_observations', None),
                "authenticateOn": getattr(persons_origin, 'person_origin_authenticate_on', None),
                "addresses": [
                    {
                        "addressType": getattr(persons_origin, 'person_origin_addresses_address_type', None),
                        "country": getattr(persons_origin, 'person_origin_addresses_country', None),
                        "postalCode": getattr(persons_origin, 'person_origin_addresses_postal_code', None),
                        "state": getattr(persons_origin, 'person_origin_addresses_state', None),
                        "district": getattr(persons_origin, 'person_origin_addresses_district', None),
                        "city": getattr(persons_origin, 'person_origin_addresses_city', None),
                        "street": getattr(persons_origin, 'person_origin_addresses_street', None),
                        "number": getattr(persons_origin, 'person_origin_addresses_number', None),
                        "complement": getattr(persons_origin, 'person_origin_addresses_complement', None),
                        "reference": getattr(persons_origin, 'person_origin_addresses_reference', None),
                        "isDefault": getattr(persons_origin, 'person_origin_addresses_is_default', None),
                        "countryId": getattr(persons_origin, 'person_origin_addresses_country_id', None)
                    }
                ] if getattr(persons_origin, 'person_origin_addresses', None) else [],
                "contacts": [
                    {
                        "contactType": getattr(persons_origin, 'person_origin_contacts_contact_type', None),
                        "contact": getattr(persons_origin, 'person_origin_contacts_contact', None),
                        "isDefault": getattr(persons_origin, 'person_origin_contacts_is_default', None)
                    }
                ] if getattr(persons_origin, 'person_origin_contacts', None) else [],
                "emails": [
                    {
                        "emailType": getattr(persons_origin, 'person_origin_emails_email_type', None),
                        "email": getattr(persons_origin, 'person_origin_emails_email', None),
                        "isDefault": getattr(persons_origin, 'person_origin_emails_is_default', None)
                    }
                ] if getattr(persons_origin, 'person_origin_emails', None) else [],
                "teams": persons_destin_teams,
                # "teams": getattr(persons_origin, 'person_origin_teams', []) if getattr(
                #     persons_origin, 'person_origin_teams', None) else [],
                "relationships": getattr(persons_origin, 'person_destin_relationships', []) if getattr(
                    persons_origin, 'person_origin_relationships', None) else [],
                "customFieldValues": person_destin_custom_field_values,
                "atAssets": getattr(persons_origin, 'person_destin_at_assets', []) if getattr(persons_origin,
                                                                                              'person_destin_at_assets',
                                                                                              None) else []
            }

            # Inserir no banco
            person_exists = bd.person_exists_bd(data['id'])

            if person_exists:
                print(f"A pessoa de cód.ref. {cod_ref_origin} já existe no banco de dados do Migrador")
            else:
                insert_bd = bd.insert_date(data, movidesk_destin.person_validation(cod_ref_origin), None)
                print(f"Pessoa inserida no banco do migrador com sucesso!")

                # Post na base Movidesk
                response = movidesk_destin.post_persons_movidesk(id_persons=cod_ref_origin, data=data)
                if response.status_code == 200:
                    print("Pessoa inserida na base Movidesk com sucesso!")
                    bd.update_migrated_status(data['id'], 1, None)
                else:
                    error_message = response.text
                    print(f"Erro ao inserir na base Movidesk a pessoa de cód.ref {cod_ref_origin}. Erro: {error_message}")
                    bd.update_migrated_status(data['id'], 0, error_message)
                    patch_count += 1
                    record = f'{patch_count} - ERRO: A pessoa de id: {cod_ref_origin} NÃO FOI MIGRADA. Erro: {error_message}'
                    movidesk_destin.write_record(file_path=log_file, record=record)


if __name__ == "__main__":
    main()
