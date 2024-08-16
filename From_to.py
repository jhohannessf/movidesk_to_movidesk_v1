import pandas as pd
from Movidesk import HelpdeskMovidesk
import clients_data

import os
from dotenv import load_dotenv

load_dotenv()

class FromTo:
    def __init__(self):
        self.from_to = pd.ExcelFile('files/from-to.xlsx')

    def pd_sheets_access_profile(self):
        sheets_access_profile = pd.read_excel(self.from_to, 'Perfil de acesso')
        return sheets_access_profile

    def pd_sheets_classification(self):
        sheets_classification = pd.read_excel(self.from_to, sheet_name='Classificação')
        return sheets_classification

    def pd_sheets_justification(self):
        sheets_justification = pd.read_excel(self.from_to, 'Justificativa')
        return sheets_justification

    def pd_sheets_status(self):
        sheets_status = pd.read_excel(self.from_to, 'Status')
        return sheets_status

    def pd_sheets_category(self):
        sheets_category = pd.read_excel(self.from_to, 'Categoria')
        return sheets_category

    def pd_sheets_urgency(self):
        sheets_urgency = pd.read_excel(self.from_to, 'Urgencia')
        return sheets_urgency

    def pd_sheets_service(self):
        sheets_service = pd.read_excel(self.from_to, 'Serviços')
        return sheets_service

    def pd_sheets_group(self):
        sheets_group = pd.read_excel(self.from_to, 'Grupos')
        return sheets_group

    def pd_sheets_custom_fields_tickets(self):
        sheets_custom_fields_tickets = pd.read_excel(self.from_to, 'Campos Adicionais - Tickets')
        return sheets_custom_fields_tickets

    def pd_sheets_custom_fields_persons(self):
        sheets_custom_fields_persons = pd.read_excel(self.from_to, 'Campos Adicionais - Pessoas')
        return sheets_custom_fields_persons

    def pd_sheets_database(self):
        sheets_database = pd.read_excel(self.from_to, 'Database')
        return sheets_database

    def from_to_access_profile(self, cod_ref_origin):
        path_sheets = self.pd_sheets_access_profile()
        movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
        person_origin_request = movidesk_origin.get_persons_movidesk(cod_ref_origin)
        person_origin_access_profile = person_origin_request['accessProfile']
        for index, row in path_sheets.iterrows():
            from_to_origin = row['Perfil Origem']
            from_to_destin = row['Perfil Movidesk']
            if person_origin_access_profile == from_to_origin:
                person_destin_access_profile = from_to_destin
                # person_destin_access_profile = from_to_destin.split('||')[1].strip()
                return person_destin_access_profile

    def from_to_classification(self, cod_ref_origin):
        path_sheets = self.pd_sheets_classification()
        movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
        person_origin_request = movidesk_origin.get_persons_movidesk(cod_ref_origin)
        person_origin_classification = person_origin_request['classification']
        for index, row in path_sheets.iterrows():
            from_to_origin = row['Classificação Origem']
            from_to_destin = row['Classificação Movidesk']
            if person_origin_classification == from_to_origin:
                person_destin_classification = from_to_destin
                # person_destin_classification = from_to_destin.split('||')[1].strip()
                return person_destin_classification

    def from_to_justification(self):
        path_sheets = self.pd_sheets_justification()
        movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
        ticket_origin_request = movidesk_origin.get_tickets_movidesk('3325655')
        ticket_origin_justification = ticket_origin_request['justification']
        for index, row in path_sheets.iterrows():
            from_to_origin = row['Justificativa Origem']
            from_to_destin = row['Justificativa Movidesk']
            if ticket_origin_justification == from_to_origin:
                person_destin_justification = from_to_destin
                # person_destin_justification = from_to_destin.split('||')[1].strip()
                return person_destin_justification

    def from_to_status(self):
        path_sheets = self.pd_sheets_status()
        movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
        ticket_origin_request = movidesk_origin.get_tickets_movidesk('3325655')
        ticket_origin_status = ticket_origin_request['status']
        for index, row in path_sheets.iterrows():
            from_to_origin = row['Status Origem']
            from_to_destin = row['Status Movidesk']
            if ticket_origin_status == from_to_origin:
                ticket_destin_status = from_to_destin.split('||')[1].strip()
                return ticket_destin_status

    def from_to_category(self):
        path_sheets = self.pd_sheets_category()
        # Aqui vai ficar o retorno da base de origem
        movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
        ticket_origin_request = movidesk_origin.get_tickets_movidesk('3325655')
        ticket_origin_id_ticket = ticket_origin_request['id']
        ticket_origin_category = ticket_origin_request['category']
        for index, row in path_sheets.iterrows():
            from_to_origin = row['Categoria Origem']
            from_to_destin = row['Categoria Movidesk']
            if ticket_origin_category == from_to_origin:
                ticket_origin_category = from_to_destin
                destin_id = from_to_destin.split('||')[0].strip()
                destin_name = from_to_destin.split('||')[1].strip()
                """Patch no Movidesk"""
                request_movi = HelpdeskMovidesk(clients_data.token_movidesk_origin)
                request_movi_patch = request_movi.post_tickets_movidesk(ticket_origin_id_ticket, data={"category": destin_name})
                return request_movi_patch

    def from_to_urgency(self):
        movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
        ticket_origin_request = movidesk_origin.get_tickets_movidesk('3325655')
        ticket_origin_urgency = ticket_origin_request['urgency']
        path_sheets = self.pd_sheets_urgency()
        for index, row in path_sheets.iterrows():
            from_to_origin = row['Urgencia Origem']
            from_to_destin = row['Urgencia Movidesk']
            if ticket_origin_urgency == from_to_origin:
                ticket_destin_urgency = from_to_destin.split('||')[1].strip()
                return ticket_destin_urgency

    def from_to_service(self):
        movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
        ticket_origin_request = movidesk_origin.get_tickets_movidesk('3325655')
        ticket_origin_service = ticket_origin_request['serviceFull']
        path_sheets = self.pd_sheets_service()
        for index, row in path_sheets.iterrows():
            from_to_origin = row['Serviço Origem']
            from_to_destin = row['Serviço Movidesk']
            if ticket_origin_service == from_to_origin:
                ticket_destin_service = from_to_destin.split('||')[1].strip()
                return ticket_destin_service

    def from_to_group_persons(self, cod_ref_origin):
        path_sheets = self.pd_sheets_group()
        movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
        person_origin_request = movidesk_origin.get_persons_movidesk(cod_ref_origin)
        person_origin_teams = person_origin_request['teams']
        person_destin_teams = set() #não aceita valores repetidos
        for team in person_origin_teams:
            team_to_destin_mapping = path_sheets.set_index('Grupo Origem')['Grupo Movidesk'].to_dict()
            if team in team_to_destin_mapping:
                # team_to_destin = team_to_destin_mapping.get(team, 'Administradores').split('||')[1].strip()
                team_to_destin = team_to_destin_mapping[team].split('||')[1].strip()
                person_destin_teams.add(team_to_destin)
            else:
                continue
            # person_destin_teams.append(team_to_destin)
        return list(person_destin_teams)

    def from_to_group_tickets(self, number_ticket):
        path_sheets = self.pd_sheets_group()
        movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
        ticket_origin_request = movidesk_origin.get_tickets_movidesk(number_ticket)
        ticket_origin_team = ticket_origin_request['ownerTeam']
        ticket_destin_team = []
        for team in ticket_origin_team:
            team_to_destin_mapping = path_sheets.set_index('Grupo Origem')['Grupo Movidesk'].to_dict()
            if team in team_to_destin_mapping:
                # team_to_destin = team_to_destin_mapping.get(team, 'Administradores').split('||')[1].strip()
                team_to_destin = team_to_destin_mapping[team].split('||')[1].strip()
            else:
                team_to_destin = str(os.getenv('default_owner_team'))
            return team_to_destin

    def from_to_custom_fields_persons(self, cod_ref_origin):
        sheets_cf_persons = self.pd_sheets_custom_fields_persons()
        movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
        persons_origin_request = movidesk_origin.get_persons_movidesk(cod_ref_origin)
        person_origin_custom_field = persons_origin_request['customFieldValues']
        person_destin_custom_field_values = []
        if person_origin_custom_field:
            for field in person_origin_custom_field:
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

                for index, row in sheets_cf_persons.iterrows():
                    cf_persons_origin = row['Campo Origem']
                    cf_persons_destin = row['Opção Movidesk']
                    if pd.isna(cf_persons_origin):
                        break
                    if pd.isna(cf_persons_destin):
                        break

                    cf_persons_parts_origin = cf_persons_origin.split('||')
                    cf_persons_parts_destin = cf_persons_destin.split('||')

                    from_to_origin_field_id = row['Campo Origem'].split('||')[0].strip()
                    from_to_origin_field_id = int(from_to_origin_field_id)
                    from_to_origin_field_name = row['Campo Origem'].split('||')[1].strip()
                    from_to_origin_option = row['Campo Origem'].split('||')[3].strip() if len(
                        cf_persons_parts_origin) >= 4 else ''
                    from_to_destin_field_id = row['Opção Movidesk'].split('||')[0].strip()
                    from_to_destin_field_id = int(from_to_destin_field_id)
                    from_to_destin_option_name = row['Opção Movidesk'].split('||')[3].strip() if len(
                        cf_persons_parts_destin) >= 4 else ''
                    from_to_destin_rule_id = row['Regra de exibição'].split('||')[0].strip()
                    from_to_destin_rule_id = int(from_to_destin_rule_id)
                    if person_origin_custom_field_values_value:
                        if person_origin_custom_field_values_custom_field_id == from_to_origin_field_id:
                            person_origin_custom_field_values_custom_field_id_destin = from_to_destin_field_id
                            person_origin_custom_field_values_custom_field_rule_id_destin = from_to_destin_rule_id
                    if person_origin_custom_field_values_items:
                        if person_origin_custom_field_values_custom_field_id == from_to_origin_field_id:
                            if not pd.isna(from_to_origin_option) and not pd.isna(
                                    person_origin_custom_field_values_items_custom_field_item):
                                if person_origin_custom_field_values_items_custom_field_item == from_to_origin_option:
                                    person_origin_custom_field_values_custom_field_id_destin = from_to_destin_field_id
                                    person_origin_custom_field_values_items_custom_field_item_destin = from_to_destin_option_name
                                    person_origin_custom_field_values_custom_field_rule_id_destin = from_to_destin_rule_id

                person_origin_custom_field_values_dict = {
                    "customFieldId": person_origin_custom_field_values_custom_field_id_destin,
                    "customFieldRuleId": person_origin_custom_field_values_custom_field_rule_id_destin,
                    "line": person_origin_custom_field_values_line,
                    "value": person_origin_custom_field_values_value,
                    "items": [
                        {
                            "personId": person_origin_custom_field_values_items_person_id,
                            "clientId": person_origin_custom_field_values_items_client_id,
                            "team": person_origin_custom_field_values_items_team,
                            "customFieldItem": person_origin_custom_field_values_items_custom_field_item_destin,
                            "storageFileGuid": person_origin_custom_field_values_items_storage_file_guid,
                            "fileName": person_origin_custom_field_values_items_file_name
                        }
                    ] if person_origin_custom_field_values_items else []
                }
                person_destin_custom_field_values.append(person_origin_custom_field_values_dict)
            return person_destin_custom_field_values

    def from_to_custom_fields_tickets(self, number_tickets):
        movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
        persons_origin_request = movidesk_origin.get_tickets_movidesk(number_tickets)
        person_origin_custom_field = persons_origin_request['customFieldValues']
        person_destin_custom_field_values = []
        if person_origin_custom_field:
            for field in person_origin_custom_field:
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

                path = FromTo()
                sheets_cf_persons = path.pd_sheets_custom_fields_persons()

                for index, row in sheets_cf_persons.iterrows():
                    cf_persons_origin = row['Campo Origem']
                    cf_persons_destin = row['Opção Movidesk']
                    if pd.isna(cf_persons_origin):
                        break
                    if pd.isna(cf_persons_destin):
                        break

                    cf_persons_parts_origin = cf_persons_origin.split('||')
                    cf_persons_parts_destin = cf_persons_destin.split('||')

                    from_to_origin_field_id = row['Campo Origem'].split('||')[0].strip()
                    from_to_origin_field_id = int(from_to_origin_field_id)
                    from_to_origin_field_name = row['Campo Origem'].split('||')[1].strip()
                    from_to_origin_option = row['Campo Origem'].split('||')[3].strip() if len(
                        cf_persons_parts_origin) >= 4 else ''
                    from_to_destin_field_id = row['Opção Movidesk'].split('||')[0].strip()
                    from_to_destin_field_id = int(from_to_destin_field_id)
                    from_to_destin_option_name = row['Opção Movidesk'].split('||')[3].strip() if len(
                        cf_persons_parts_destin) >= 4 else ''
                    from_to_destin_rule_id = row['Regra de exibição'].split('||')[0].strip()
                    from_to_destin_rule_id = int(from_to_destin_rule_id)
                    if person_origin_custom_field_values_value:
                        if person_origin_custom_field_values_custom_field_id == from_to_origin_field_id:
                            person_origin_custom_field_values_custom_field_id_destin = from_to_destin_field_id
                            person_origin_custom_field_values_custom_field_rule_id_destin = from_to_destin_rule_id
                    if person_origin_custom_field_values_items:
                        if person_origin_custom_field_values_custom_field_id == from_to_origin_field_id:
                            if not pd.isna(from_to_origin_option) and not pd.isna(
                                    person_origin_custom_field_values_items_custom_field_item):
                                if person_origin_custom_field_values_items_custom_field_item == from_to_origin_option:
                                    person_origin_custom_field_values_custom_field_id_destin = from_to_destin_field_id
                                    person_origin_custom_field_values_items_custom_field_item_destin = from_to_destin_option_name
                                    person_origin_custom_field_values_custom_field_rule_id_destin = from_to_destin_rule_id

                person_origin_custom_field_values_dict = {
                    "customFieldId": person_origin_custom_field_values_custom_field_id_destin,
                    "customFieldRuleId": person_origin_custom_field_values_custom_field_rule_id_destin,
                    "line": person_origin_custom_field_values_line,
                    "value": person_origin_custom_field_values_value,
                    "items": [
                        {
                            "personId": person_origin_custom_field_values_items_person_id,
                            "clientId": person_origin_custom_field_values_items_client_id,
                            "team": person_origin_custom_field_values_items_team,
                            "customFieldItem": person_origin_custom_field_values_items_custom_field_item_destin,
                            "storageFileGuid": person_origin_custom_field_values_items_storage_file_guid,
                            "fileName": person_origin_custom_field_values_items_file_name
                        }
                    ] if person_origin_custom_field_values_items else []
                }
                person_destin_custom_field_values.append(person_origin_custom_field_values_dict)
            return person_destin_custom_field_values
