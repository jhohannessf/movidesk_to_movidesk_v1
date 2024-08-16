import requests
import warnings
import urllib3

from Movidesk import HelpdeskMovidesk
import clients_data

warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore", category=UserWarning)

movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
# cod_ref_persons = open('files/cod_ref_persons', 'r')

top = 100
skip = 0

while True:
    cod_ref_persons = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[0]
    status_code = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[1].status_code
    text_requests = movidesk_origin.get_persons_all_movidesk(top=top, skip=skip)[1].text
    for person_origin in cod_ref_persons:
        person_origin_id = person_origin['id']
        person_origin_code_reference_additional = person_origin['codeReferenceAdditional']
        person_origin_is_active = person_origin['isActive']
        person_origin_person_type = person_origin['personType']
        person_origin_profile_type = person_origin['profileType']
        person_origin_access_profile = person_origin['accessProfile']
        person_origin_business_name = person_origin['businessName']
        person_origin_business_branch = person_origin['businessBranch']
        person_origin_corporate_name = person_origin['corporateName']
        person_origin_cpf_cnpj = person_origin['cpfCnpj']
        person_origin_user_name = person_origin['userName']
        person_origin_password = person_origin.get('password', None)
        person_origin_role = person_origin['role']
        person_origin_boss_id = person_origin['bossId']
        person_origin_boss_name = person_origin['bossName']
        person_origin_classification = person_origin['classification']
        person_origin_culture_id = person_origin['cultureId']
        person_origin_time_zone_id = person_origin['timeZoneId']
        person_origin_created_date = person_origin['createdDate']
        person_origin_created_by = person_origin['createdBy']
        person_origin_changed_date = person_origin['changedDate']
        person_origin_changed_by = person_origin['changedBy']
        person_origin_observations = person_origin['observations']
        person_origin_authenticate_on = person_origin['authenticateOn']
        person_origin_addresses = person_origin['addresses']
        if person_origin_addresses:
            for address in person_origin_addresses:
                person_origin_addresses_address_type = address['addressType']
                person_origin_addresses_country = address['country']
                person_origin_addresses_postal_code = address['postalCode']
                person_origin_addresses_state = address['state']
                person_origin_addresses_district = address['district']
                person_origin_addresses_city = address['city']
                person_origin_addresses_street = address['street']
                person_origin_addresses_number = address['number']
                person_origin_addresses_complement = address['complement']
                person_origin_addresses_reference = address['reference']
                person_origin_addresses_is_default = address['isDefault']
                person_origin_addresses_country_id = address['countryId']
        person_origin_contacts = person_origin['contacts']
        if person_origin_contacts:
            for contact in person_origin_contacts:
                person_origin_contacts_contact_type = contact['contactType']
                person_origin_contacts_contact = contact['contact']
                person_origin_contacts_is_default = contact['isDefault']
        person_origin_emails = person_origin['emails']
        if person_origin_emails:
            for email in person_origin_emails:
                person_origin_emails_email_type = email['emailType']
                person_origin_emails_email = email['email']
                person_origin_emails_is_default = email['isDefault']
        person_origin_teams = person_origin['teams']

        person_origin_relationships = person_origin['relationships']
        person_destin_relationships = []
        for org in person_origin_relationships:
            person_origin_relationships_id = org['id']
            person_origin_relationships_name = org['name']
            person_origin_relationships_sla_agreement = org['slaAgreement']
            person_origin_relationships_force_children_to_have_some_agreement = org['forceChildrenToHaveSomeAgreement']
            person_origin_relationships_allow_all_services = org['allowAllServices']
            person_origin_relationships_include_in_parents = org['includeInParents']
            person_origin_relationships_load_child_organizations = org['loadChildOrganizations']
            person_origin_relationships_services = org['services']
            person_origin_relationships_id_to_delete = org.get('idToDelete', None)
            person_origin_relationships_is_get_method = org['isGetMethod']

            person_origin_relationships_dict = {
                "id": person_origin_relationships_id,
                "name": person_origin_relationships_name,
                "slaAgreement": person_origin_relationships_sla_agreement,
                "forceChildrenToHaveSomeAgreement": person_origin_relationships_force_children_to_have_some_agreement,
                "allowAllServices": person_origin_relationships_allow_all_services,
                "includeInParents": person_origin_relationships_include_in_parents,
                "loadChildOrganizations": person_origin_relationships_load_child_organizations,
                "services": person_origin_relationships_services,
                "idToDelete": person_origin_relationships_id_to_delete,
                "isGetMethod": person_origin_relationships_is_get_method
            }
            person_destin_relationships.append(person_origin_relationships_dict)

        person_origin_custom_field_values = person_origin['customFieldValues']
        person_destin_custom_field_values = []
        if person_origin_custom_field_values:
            for field in person_origin_custom_field_values:
                person_origin_custom_field_values_custom_field_id = field['customFieldId']
                person_origin_custom_field_values_custom_field_rule_id = field['customFieldRuleId']
                person_origin_custom_field_values_line = field['line']
                person_origin_custom_field_values_value = field['value']
                person_origin_custom_field_values_items = field['items']
                if person_origin_custom_field_values_items:
                    for item in person_origin_custom_field_values_items:
                        person_origin_custom_field_values_items_person_id = item['personId']
                        person_origin_custom_field_values_items_client_id = item['clientId']
                        person_origin_custom_field_values_items_team = item['team']
                        person_origin_custom_field_values_items_custom_field_item = item['customFieldItem']
                        person_origin_custom_field_values_items_storage_file_guid = item['storageFileGuid']
                        person_origin_custom_field_values_items_file_name = item['fileName']

                person_origin_custom_field_values_dict = {
                    "customFieldId": person_origin_custom_field_values_custom_field_id,
                    "customFieldRuleId": person_origin_custom_field_values_custom_field_rule_id,
                    "line": person_origin_custom_field_values_line,
                    "value": person_origin_custom_field_values_value,
                    "items": [
                        {
                            "personId": person_origin_custom_field_values_items_person_id,
                            "clientId": person_origin_custom_field_values_items_client_id,
                            "team": person_origin_custom_field_values_items_team,
                            "customFieldItem": person_origin_custom_field_values_items_custom_field_item,
                            "storageFileGuid": person_origin_custom_field_values_items_storage_file_guid,
                            "fileName": person_origin_custom_field_values_items_file_name
                        }
                    ] if person_origin_custom_field_values_items else []
                }
                person_destin_custom_field_values.append(person_origin_custom_field_values_dict)
                a = person_destin_custom_field_values

        person_origin_at_assets = person_origin['atAssets']
        person_destin_at_assets = []
        if person_origin_at_assets:
            for assets in person_origin_at_assets:
                person_origin_at_assets_id = assets['id']
                person_origin_at_assets_name = assets['name']
                person_origin_at_assets_label = assets['label']

                person_origin_at_assets_dict = {
                    "id": person_origin_at_assets_id,
                    "name": person_origin_at_assets_name,
                    "label": person_origin_at_assets_label
                }
                person_destin_at_assets.append(person_origin_at_assets_dict)

    skip += top
        # if status_code == 200:
        #     skip += 100
        # elif status_code == 404:
        #     break


