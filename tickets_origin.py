from Movidesk import HelpdeskMovidesk
import clients_data

# replace Ctrl + Shift + R

movidesk_origin = HelpdeskMovidesk(clients_data.token_movidesk_origin)
ticket_origin = movidesk_origin.get_tickets_movidesk('4000002')  # 2979853
ticket_origin_id = ticket_origin['id']
ticket_origin_protocol_ticket = ticket_origin['protocol']
ticket_origin_type = ticket_origin['type']  # obrigatório
ticket_origin_subject = ticket_origin['subject']
ticket_origin_category = ticket_origin['category']
ticket_origin_urgency = ticket_origin['urgency']
ticket_origin_status = ticket_origin['status']  # obrigatório
ticket_origin_base_status = ticket_origin['baseStatus']
ticket_origin_justification = ticket_origin['justification']
ticket_origin_origin = ticket_origin['origin']
ticket_origin_created_date = ticket_origin['createdDate']  # obrigatório
ticket_origin_is_deleted = ticket_origin['isDeleted']
ticket_origin_email_account = ticket_origin['originEmailAccount']
ticket_origin_owner = ticket_origin['owner']  # obrigatório
ticket_origin_owner_id = ticket_origin['owner']['id']
ticket_origin_owner_person_type = ticket_origin['owner']['personType']
ticket_origin_owner_profile_type = ticket_origin['owner']['profileType']
ticket_origin_owner_business_name = ticket_origin['owner']['businessName']
ticket_origin_owner_email = ticket_origin['owner']['email']
ticket_origin_owner_phone = ticket_origin['owner']['phone']
ticket_origin_owner_team = ticket_origin['ownerTeam']  # obrigatório
ticket_origin_created_by = ticket_origin['createdBy']  # obrigatório
ticket_origin_created_by_id = ticket_origin['createdBy']['id']
ticket_origin_created_by_person_type = ticket_origin['createdBy']['personType']
ticket_origin_created_by_profileType = ticket_origin['createdBy']['profileType']
ticket_origin_created_by_business_name = ticket_origin['createdBy']['businessName']
ticket_origin_created_by_email = ticket_origin['createdBy']['email']
ticket_origin_service_full = ticket_origin['serviceFull']
ticket_origin_serviceFirstLevelId = ticket_origin['serviceFirstLevelId']
ticket_origin_serviceFirstLevel = ticket_origin['serviceFirstLevel']
ticket_origin_service_second_level = ticket_origin['serviceSecondLevel']
ticket_origin_service_third_level = ticket_origin['serviceThirdLevel']
ticket_origin_contact_form = ticket_origin['contactForm']
ticket_origin_tags = ticket_origin['tags']
ticket_origin_cc = ticket_origin['cc']
ticket_origin_closed_in = ticket_origin['closedIn']
ticket_origin_canceled_in = ticket_origin['canceledIn']
ticket_origin_actionCount = ticket_origin['actionCount']
ticket_origin_life_time_working_time = ticket_origin['lifeTimeWorkingTime']
ticket_origin_stopped_time = ticket_origin['stoppedTime']
ticket_origin_stopped_time_working_time = ticket_origin['stoppedTimeWorkingTime']
ticket_origin_resolved_in_first_call = ticket_origin['resolvedInFirstCall']
ticket_origin_chat_widget = ticket_origin['chatWidget']
ticket_origin_chat_group = ticket_origin['chatGroup']
ticket_origin_chat_talk_time = ticket_origin['chatTalkTime']
ticket_origin_chat_waiting_time = ticket_origin['chatWaitingTime']
ticket_origin_sequence = ticket_origin['sequence']
ticket_origin_sla_agreement = ticket_origin['slaAgreement']
ticket_origin_sla_agreement_rule = ticket_origin['slaAgreementRule']
ticket_origin_sla_solution_time = ticket_origin['slaSolutionTime']
ticket_origin_sla_response_time = ticket_origin['slaResponseTime']
ticket_origin_sla_solution_changed_by_user = ticket_origin['slaSolutionChangedByUser']
ticket_origin_sla_solution_changed_by = ticket_origin['slaSolutionChangedBy']
if ticket_origin_sla_solution_changed_by:
    ticket_origin_sla_solution_changed_by_id = ticket_origin['slaSolutionChangedBy']['id']
    ticket_origin_sla_solution_changed_by_person_type = ticket_origin['slaSolutionChangedBy']['personType']
    ticket_origin_sla_solution_changed_by_profile_type = ticket_origin['slaSolutionChangedBy']['profileType']
    ticket_origin_sla_solution_changed_by_business_name = ticket_origin['slaSolutionChangedBy']['businessName']
    ticket_origin_sla_solution_changed_by_email = ticket_origin['slaSolutionChangedBy']['email']
    ticket_origin_sla_solution_changed_by_phone = ticket_origin['slaSolutionChangedBy']['phone']
ticket_origin_sla_solution_Date = ticket_origin['slaSolutionDate']
ticket_origin_sla_solution_date_is_paused = ticket_origin['slaSolutionDateIsPaused']
ticket_origin_jira_issue_Key = ticket_origin['jiraIssueKey']
ticket_origin_redmine_issue_id = ticket_origin['redmineIssueId']
ticket_origin_movidesk_ticket_number = ticket_origin['movideskTicketNumber']
ticket_origin_linked_to_integrated_ticket_number = ticket_origin['linkedToIntegratedTicketNumber']
ticket_origin_reopened_in = ticket_origin['reopenedIn']
ticket_origin_last_action_date = ticket_origin['lastActionDate']
ticket_origin_last_update = ticket_origin['lastUpdate']
ticket_origin_sla_response_date = ticket_origin['slaResponseDate']
ticket_origin_sla_real_response_date = ticket_origin['slaRealResponseDate']
ticket_origin_clients = ticket_origin['clients']  # obrigatório
ticket_destin_clients = []
if ticket_origin_clients:
    for client in ticket_origin_clients:
        ticket_origin_clients_id = client['id']
        ticket_origin_clients_person_type = client['personType']
        ticket_origin_clients_profile_type = client['profileType']
        ticket_origin_clients_business_name = client['businessName']
        ticket_origin_clients_email = client['email']
        ticket_origin_clients_phone = client['phone']
        ticket_origin_clients_is_deleted = client['isDeleted']
        ticket_origin_clients_organization = client['organization']
        if ticket_origin_clients_organization:
            ticket_origin_clients_organization_id = ticket_origin_clients_organization['id']
            ticket_origin_clients_organization_person_type = ticket_origin_clients_organization['personType']
            ticket_origin_clients_organization_profile_type = ticket_origin_clients_organization['profileType']
            ticket_origin_clients_organization_business_name = ticket_origin_clients_organization['businessName']
            ticket_origin_clients_organization_email = ticket_origin_clients_organization['email']
            ticket_origin_clients_organization_phone = ticket_origin_clients_organization['phone']
        ticket_origin_clients_address = client['address']
        ticket_origin_clients_complement = client['complement']
        ticket_origin_clients_cep = client['cep']
        ticket_origin_clients_city = client['city']
        ticket_origin_clients_bairro = client['bairro']
        ticket_origin_clients_number = client['number']
        ticket_origin_clients_reference = client['reference']

        ticket_origin_clients_dict = {
            "id": ticket_origin_clients_id,
            "personType": ticket_origin_clients_person_type,
            "profileType": ticket_origin_clients_profile_type,
            "businessName": ticket_origin_clients_business_name,
            "email": ticket_origin_clients_email,
            "phone": ticket_origin_clients_phone,
            "isDeleted": ticket_origin_clients_is_deleted,
            "organization": {
                "id": ticket_origin_clients_organization_id,
                "personType": ticket_origin_clients_organization_person_type,
                "profileType": ticket_origin_clients_organization_profile_type,
                "businessName": ticket_origin_clients_organization_business_name,
                "email": ticket_origin_clients_organization_email,
                "phone": ticket_origin_clients_organization_phone
            } if ticket_origin_clients_organization else None,
            "address": ticket_origin_clients_address,
            "complement": ticket_origin_clients_complement,
            "cep": ticket_origin_clients_cep,
            "city": ticket_origin_clients_city,
            "bairro": ticket_origin_clients_bairro,
            "number": ticket_origin_clients_number,
            "reference": ticket_origin_clients_reference
        }
        ticket_destin_clients.append(ticket_origin_clients_dict)
        b = ticket_destin_clients

ticket_origin_actions = ticket_origin['actions']
ticket_destin_actions = []
if ticket_origin_actions:
    for action in ticket_origin_actions:
        ticket_origin_actions_id = action['id']
        ticket_origin_actions_type = action['type']
        ticket_origin_actions_origin = action['origin']
        ticket_origin_actions_description = action['description']
        ticket_origin_actions_html_description = action['htmlDescription']
        ticket_origin_actions_status = action['status']
        ticket_origin_actions_justification = action['justification']
        ticket_origin_actions_created_date = action['createdDate']
        ticket_origin_actions_created_by = action['createdBy']
        ticket_origin_actions_created_by_id = action['createdBy']['id']
        ticket_origin_actions_created_by_person_type = action['createdBy']['personType']
        ticket_origin_actions_created_by_profile_type = action['createdBy']['profileType']
        ticket_origin_actions_created_by_business_name = action['createdBy']['businessName']
        ticket_origin_actions_created_by_email = action['createdBy']['email']
        ticket_origin_actions_created_by_phone = action['createdBy']['phone']
        ticket_origin_actions_is_deleted = action['isDeleted']

        ticket_origin_actions_time_appointments = action['timeAppointments']
        if ticket_origin_actions_time_appointments:
            for time_appointment in ticket_origin_actions_time_appointments:
                ticket_origin_actions_time_appointments_id = time_appointment['id']
                ticket_origin_actions_time_appointments_activity = time_appointment['activity']
                ticket_origin_actions_time_appointments_date = time_appointment['date']
                ticket_origin_actions_time_appointments_period_start = time_appointment['periodStart']
                ticket_origin_actions_time_appointments_period_end = time_appointment['periodEnd']
                ticket_origin_actions_time_appointments_work_time = time_appointment['workTime']
                ticket_origin_actions_time_appointments_accounted_time = time_appointment['accountedTime']
                ticket_origin_actions_time_appointments_work_type_name = time_appointment['workTypeName']
                ticket_origin_actions_time_appointments_created_by = time_appointment['createdBy']
                ticket_origin_actions_time_appointments_created_by_id = time_appointment['createdBy']['id']
                ticket_origin_actions_time_appointments_created_by_person_type = time_appointment['createdBy'][
                    'personType']
                ticket_origin_actions_time_appointments_created_by_profile_type = time_appointment['createdBy'][
                    'profileType']
                ticket_origin_actions_time_appointments_created_by_businessName = time_appointment['createdBy'][
                    'businessName']
                ticket_origin_actions_time_appointments_created_by_email = time_appointment['createdBy']['email']
                ticket_origin_actions_time_appointments_created_by_phone = time_appointment['createdBy']['phone']
                ticket_origin_actions_time_appointments_created_by_team = time_appointment['createdByTeam']
                ticket_origin_actions_time_appointments_created_by_team_id = time_appointment['createdByTeam']['id']
                ticket_origin_actions_time_appointments_created_by_team_name = time_appointment['createdByTeam']['name']

        ticket_origin_actions_attachments = action['attachments']
        if ticket_origin_actions_attachments:
            for attachment in ticket_origin_actions_attachments:
                ticket_origin_actions_attachments_file_name = attachment['fileName']
                ticket_origin_actions_attachments_path = attachment['path']
                ticket_origin_actions_attachments_created_by = attachment['createdBy']
                ticket_origin_actions_attachments_created_by_id = attachment['createdBy']['id']
                ticket_origin_actions_attachments_created_by_person_type = attachment['createdBy']['personType']
                ticket_origin_actions_attachments_created_by_profileType = attachment['createdBy']['profileType']
                ticket_origin_actions_attachments_created_by_business_name = attachment['createdBy']['businessName']
                ticket_origin_actions_attachments_created_by_email = attachment['createdBy']['email']
                ticket_origin_actions_attachments_created_by_phone = attachment['createdBy']['phone']
                ticket_origin_actions_attachments_created_date = attachment['createdDate']

        ticket_origin_actions_expenses = action['expenses']
        if ticket_origin_actions_expenses:
            for expenses in ticket_origin_actions_expenses:
                ticket_origin_actions_expenses_id = expenses['id']
                ticket_origin_actions_expenses_type = expenses['type']
                ticket_origin_actions_expenses_service_report = expenses['serviceReport']
                ticket_origin_actions_expenses_created_by = expenses['createdBy']
                ticket_origin_actions_expenses_created_by_id = expenses['createdBy']['id']
                ticket_origin_actions_expenses_created_by_person_type = expenses['createdBy']['personType']
                ticket_origin_actions_expenses_created_by_profile_type = expenses['createdBy']['profileType']
                ticket_origin_actions_expenses_created_by_business_name = expenses['createdBy']['businessName']
                ticket_origin_actions_expenses_created_by_email = expenses['createdBy']['email']
                ticket_origin_actions_expenses_created_by_phone = expenses['createdBy']['phone']
                ticket_origin_actions_expenses_created_by_team = expenses['createdByTeam']
                ticket_origin_actions_expenses_date = expenses['date']
                ticket_origin_actions_expenses_quantity = expenses['quantity']
                ticket_origin_actions_expenses_value = expenses['value']

        ticket_origin_actions_tags = action['tags']

        ticket_origin_actions_dict = {
            "id": ticket_origin_actions_id,
            "type": ticket_origin_actions_type,
            "origin": ticket_origin_actions_origin,
            "description": ticket_origin_actions_description,
            "htmlDescription": ticket_origin_actions_html_description,
            "status": ticket_origin_actions_status,
            "justification": ticket_origin_actions_justification,
            "createdDate": ticket_origin_actions_created_date,
            "createdBy": {
                "id": ticket_origin_actions_created_by_id,
                "personType": ticket_origin_actions_created_by_person_type,
                "profileType": ticket_origin_actions_created_by_profile_type,
                "businessName": ticket_origin_actions_created_by_business_name,
                "email": ticket_origin_actions_created_by_email,
                "phone": ticket_origin_actions_created_by_phone
            } if ticket_origin_actions_created_by else None,
            "isDeleted": ticket_origin_actions_is_deleted,
            "timeAppointments": [
                {
                    "id": ticket_origin_actions_time_appointments_id,
                    "activity": ticket_origin_actions_time_appointments_activity,
                    "date": ticket_origin_actions_time_appointments_date,
                    "periodStart": ticket_origin_actions_time_appointments_period_start,
                    "periodEnd": ticket_origin_actions_time_appointments_period_end,
                    "workTime": ticket_origin_actions_time_appointments_work_time,
                    "accountedTime": ticket_origin_actions_time_appointments_accounted_time,
                    "workTypeName": ticket_origin_actions_time_appointments_work_type_name,
                    "createdBy": {
                        "id": ticket_origin_actions_time_appointments_created_by_id,
                        "personType": ticket_origin_actions_time_appointments_created_by_person_type,
                        "profileType": ticket_origin_actions_time_appointments_created_by_profile_type,
                        "businessName": ticket_origin_actions_time_appointments_created_by_businessName,
                        "email": ticket_origin_actions_time_appointments_created_by_email,
                        "phone": ticket_origin_actions_time_appointments_created_by_phone
                    } if ticket_origin_actions_time_appointments_created_by else None,
                    "createdByTeam": {
                        "id": ticket_origin_actions_time_appointments_created_by_team_id,
                        "name": ticket_origin_actions_time_appointments_created_by_team_name
                    } if ticket_origin_actions_time_appointments_created_by_team else None
                }
            ] if ticket_origin_actions_time_appointments else [],
            "attachments": [
                {
                    "fileName": ticket_origin_actions_attachments_file_name,
                    "path": ticket_origin_actions_attachments_path,
                    "createdBy": {
                        "id": ticket_origin_actions_attachments_created_by_id,
                        "personType": ticket_origin_actions_attachments_created_by_person_type,
                        "profileType": ticket_origin_actions_attachments_created_by_profileType,
                        "businessName": ticket_origin_actions_attachments_created_by_business_name,
                        "email": ticket_origin_actions_attachments_created_by_email,
                        "phone": ticket_origin_actions_attachments_created_by_phone
                    } if ticket_origin_actions_attachments_created_by else None,
                    "createdDate": ticket_origin_actions_attachments_created_date
                }
            ] if ticket_origin_actions_attachments else [],
            "expenses": [
                {
                    "id": ticket_origin_actions_expenses_id,
                    "type": ticket_origin_actions_expenses_type,
                    "serviceReport": ticket_origin_actions_expenses_service_report,
                    "createdBy": {
                        "id": ticket_origin_actions_expenses_created_by_id,
                        "personType": ticket_origin_actions_expenses_created_by_person_type,
                        "profileType": ticket_origin_actions_expenses_created_by_profile_type,
                        "businessName": ticket_origin_actions_expenses_created_by_business_name,
                        "email": ticket_origin_actions_expenses_created_by_email,
                        "phone": ticket_origin_actions_expenses_created_by_phone
                    } if ticket_origin_actions_expenses_created_by else None,
                    "createdByTeam": ticket_origin_actions_expenses_created_by_team,
                    "date": ticket_origin_actions_expenses_date,
                    "quantity": ticket_origin_actions_expenses_quantity,
                    "value": ticket_origin_actions_expenses_value
                }
            ] if ticket_origin_actions_expenses else [],
            "tags": ticket_origin_actions_tags
        }
        ticket_destin_actions.append(ticket_origin_actions_dict)
        c = ticket_destin_actions

ticket_origin_parent_tickets = ticket_origin['parentTickets']
ticket_destin_parent_tickets = []
if ticket_origin_parent_tickets:
    for parent in ticket_origin_parent_tickets:
        ticket_origin_parent_tickets_id = parent['id']
        ticket_origin_parent_tickets_subject = parent['subject']
        ticket_origin_parent_tickets_is_deleted = parent['isDeleted']

        ticket_origin_parent_tickets_dict = {
            "id": ticket_origin_parent_tickets_id,
            "subject": ticket_origin_parent_tickets_subject,
            "isDeleted": ticket_origin_parent_tickets_is_deleted
        } if ticket_origin_parent_tickets else []
        ticket_destin_parent_tickets.append(ticket_origin_parent_tickets_dict)
        d = ticket_destin_parent_tickets

ticket_origin_children_tickets = ticket_origin['childrenTickets']
ticket_destin_children_tickets = []
if ticket_origin_children_tickets:
    for children in ticket_origin_children_tickets:
        ticket_origin_children_tickets_id = children['id']
        ticket_origin_children_tickets_subject = children['subject']
        ticket_origin_children_tickets_is_deleted = children['isDeleted']

        ticket_origin_children_tickets_dict = {
            "id": ticket_origin_children_tickets_id,
            "subject": ticket_origin_children_tickets_subject,
            "isDeleted": ticket_origin_children_tickets_is_deleted
        }
        ticket_destin_children_tickets.append(ticket_origin_children_tickets_dict)
        e = ticket_destin_children_tickets

ticket_origin_owner_histories = ticket_origin['ownerHistories']
ticket_destin_owner_histories = []
if ticket_origin_owner_histories:
    for owner in ticket_origin_owner_histories:
        ticket_origin_owner_histories_ownerTeam = owner['ownerTeam']
        ticket_origin_owner_histories_owner = owner['owner']
        ticket_origin_owner_histories_owner_id = owner['owner']['id']
        ticket_origin_owner_histories_owner_person_type = owner['owner']['personType']
        ticket_origin_owner_histories_owner_profile_type = owner['owner']['profileType']
        ticket_origin_owner_histories_owner_business_name = owner['owner']['businessName']
        ticket_origin_owner_histories_owner_email = owner['owner']['email']
        ticket_origin_owner_histories_owner_phone = owner['owner']['phone']
        ticket_origin_owner_histories_changed_by = owner['changedBy']
        ticket_origin_owner_histories_changed_by_id = owner['changedBy']['id']
        ticket_origin_owner_histories_changed_by_person_type = owner['changedBy']['personType']
        ticket_origin_owner_histories_changed_by_profile_type = owner['changedBy']['profileType']
        ticket_origin_owner_histories_changed_by_business_name = owner['changedBy']['businessName']
        ticket_origin_owner_histories_changed_by_email = owner['changedBy']['email']
        ticket_origin_owner_histories_changed_by_phone = owner['changedBy']['phone']
        ticket_origin_owner_histories_changed_date = owner['changedDate']
        ticket_origin_owner_histories_permanency_time_full_time = owner['permanencyTimeFullTime']
        ticket_origin_owner_histories_permanency_time_working_time = owner['permanencyTimeWorkingTime']

        ticket_origin_owner_histories_dict = {
            "ownerTeam": ticket_origin_owner_histories_ownerTeam,
            "owner": {
                "id": ticket_origin_owner_histories_owner_id,
                "personType": ticket_origin_owner_histories_owner_person_type,
                "profileType": ticket_origin_owner_histories_owner_profile_type,
                "businessName": ticket_origin_owner_histories_owner_business_name,
                "email": ticket_origin_owner_histories_owner_email,
                "phone": ticket_origin_owner_histories_owner_phone
            } if ticket_origin_owner_histories_owner else None,
            "changedBy": {
                "id": ticket_origin_owner_histories_changed_by_id,
                "personType": ticket_origin_owner_histories_changed_by_person_type,
                "profileType": ticket_origin_owner_histories_changed_by_profile_type,
                "businessName": ticket_origin_owner_histories_changed_by_business_name,
                "email": ticket_origin_owner_histories_changed_by_email,
                "phone": ticket_origin_owner_histories_changed_by_phone
            } if ticket_origin_owner_histories_changed_by else None,
            "changedDate": ticket_origin_owner_histories_changed_date,
            "permanencyTimeFullTime": ticket_origin_owner_histories_permanency_time_full_time,
            "permanencyTimeWorkingTime": ticket_origin_owner_histories_permanency_time_working_time
        }
        ticket_destin_owner_histories.append(ticket_origin_owner_histories_dict)
        f = ticket_destin_owner_histories

ticket_origin_status_histories = ticket_origin['statusHistories']
ticket_destin_status_histories = []
if ticket_origin_status_histories:
    for status in ticket_origin_status_histories:
        ticket_origin_status_histories_status = status['status']
        ticket_origin_status_histories_justification = status['justification']
        ticket_origin_status_histories_changed_by = status['changedBy']
        ticket_origin_status_histories_changed_by_id = status['changedBy']['id']
        ticket_origin_status_histories_changed_by_person_type = status['changedBy']['personType']
        ticket_origin_status_histories_changed_by_profile_type = status['changedBy']['profileType']
        ticket_origin_status_histories_changed_by_business_name = status['changedBy']['businessName']
        ticket_origin_status_histories_changed_by_email = status['changedBy']['email']
        ticket_origin_status_histories_changed_by_phone = status['changedBy']['phone']
        ticket_origin_status_histories_changed_date = status['changedDate']
        ticket_origin_status_histories_permanency_time_full_time = status['permanencyTimeFullTime']
        ticket_origin_status_histories_permanency_time_working_time = status['permanencyTimeWorkingTime']

        ticket_origin_status_histories_dict = {
            "status": ticket_origin_status_histories_status,
            "justification": ticket_origin_status_histories_justification,
            "changedBy": {
                "id": ticket_origin_status_histories_changed_by_id,
                "personType": ticket_origin_status_histories_changed_by_person_type,
                "profileType": ticket_origin_status_histories_changed_by_profile_type,
                "businessName": ticket_origin_status_histories_changed_by_business_name,
                "email": ticket_origin_status_histories_changed_by_email,
                "phone": ticket_origin_status_histories_changed_by_phone
            } if ticket_origin_status_histories_changed_by else None,
            "changedDate": ticket_origin_status_histories_changed_date,
            "permanencyTimeFullTime": ticket_origin_status_histories_permanency_time_full_time,
            "permanencyTimeWorkingTime": ticket_origin_status_histories_permanency_time_working_time
        }
        ticket_destin_status_histories.append(ticket_origin_status_histories_dict)
        g = ticket_destin_status_histories

ticket_origin_satisfaction_survey_responses = ticket_origin['satisfactionSurveyResponses']
ticket_destin_satisfaction_survey_responses = []
if ticket_origin_satisfaction_survey_responses:
    for satisfaction_response in ticket_origin_satisfaction_survey_responses:
        ticket_origin_satisfaction_survey_responses_id = satisfaction_response['id']
        ticket_origin_satisfaction_survey_responses_responsed_by = satisfaction_response[
            'responsedBy']
        ticket_origin_satisfaction_survey_responses_responsed_by_id = \
            satisfaction_response['responsedBy']['id']
        ticket_origin_satisfaction_survey_responses_responsed_by_person_type = \
            satisfaction_response['responsedBy']['personType']
        ticket_origin_satisfaction_survey_responses_responsed_by_profile_type = \
            satisfaction_response['responsedBy']['profileType']
        ticket_origin_satisfaction_survey_responses_responsed_by_businessName = \
            satisfaction_response['responsedBy']['businessName']
        ticket_origin_satisfaction_survey_responses_responsed_by_email = \
            satisfaction_response['responsedBy']['email']
        ticket_origin_satisfaction_survey_responses_responsed_by_phone = \
            satisfaction_response['responsedBy']['phone']
        ticket_origin_satisfaction_survey_responses_response_date = satisfaction_response[
            'responseDate']
        ticket_origin_satisfaction_survey_responses_response_satisfaction_survey_model = \
            satisfaction_response['satisfactionSurveyModel']
        ticket_origin_satisfaction_survey_responses_response_satisfaction_survey_net_promoter_score_response = \
            satisfaction_response['satisfactionSurveyNetPromoterScoreResponse']
        ticket_origin_satisfaction_survey_responses_response_satisfaction_survey_positive_negative_response = \
            satisfaction_response['satisfactionSurveyPositiveNegativeResponse']
        ticket_origin_satisfaction_survey_responses_response_satisfaction_survey_smiley_faces_response = \
            satisfaction_response['satisfactionSurveySmileyFacesResponse']
        ticket_origin_satisfaction_survey_responses_response_satisfaction_survey_yes_or_no_response = \
            satisfaction_response['satisfactionSurveyYesOrNoResponse']
        ticket_origin_satisfaction_survey_responses_response_comments = satisfaction_response[
            'comments']
        ticket_origin_satisfaction_survey_responses_response_questionId = satisfaction_response[
            'questionId']
        ticket_origin_satisfaction_survey_responses_dict = {
            "id": ticket_origin_satisfaction_survey_responses_id,
            "responsedBy": {
                "id": ticket_origin_satisfaction_survey_responses_responsed_by_id,
                "personType": ticket_origin_satisfaction_survey_responses_responsed_by_person_type,
                "profileType": ticket_origin_satisfaction_survey_responses_responsed_by_profile_type,
                "businessName": ticket_origin_satisfaction_survey_responses_responsed_by_businessName,
                "email": ticket_origin_satisfaction_survey_responses_responsed_by_email,
                "phone": ticket_origin_satisfaction_survey_responses_responsed_by_phone
            },
            "responseDate": ticket_origin_satisfaction_survey_responses_response_date,
            "satisfactionSurveyModel": ticket_origin_satisfaction_survey_responses_response_satisfaction_survey_model,
            "satisfactionSurveyNetPromoterScoreResponse": ticket_origin_satisfaction_survey_responses_response_satisfaction_survey_net_promoter_score_response,
            "satisfactionSurveyPositiveNegativeResponse": ticket_origin_satisfaction_survey_responses_response_satisfaction_survey_positive_negative_response,
            "satisfactionSurveySmileyFacesResponse": ticket_origin_satisfaction_survey_responses_response_satisfaction_survey_smiley_faces_response,
            "satisfactionSurveyYesOrNoResponse": ticket_origin_satisfaction_survey_responses_response_satisfaction_survey_yes_or_no_response,
            "comments": ticket_origin_satisfaction_survey_responses_response_comments,
            "questionId": ticket_origin_satisfaction_survey_responses_response_questionId
        }
        ticket_destin_satisfaction_survey_responses.append(ticket_origin_satisfaction_survey_responses_dict)
        h = ticket_destin_satisfaction_survey_responses

ticket_origin_custom_field_values = ticket_origin['customFieldValues']
ticket_destin_custom_field_values = []
if ticket_origin_custom_field_values:
    for field in ticket_origin_custom_field_values:
        ticket_origin_custom_field_values_custom_field_id = field['customFieldId']
        ticket_origin_custom_field_values_custom_field_rule_id = field['customFieldRuleId']
        ticket_origin_custom_field_values_line = field['line']
        ticket_origin_custom_field_values_value = field['value']
        ticket_origin_custom_field_values_items = field['items']
        if ticket_origin_custom_field_values_items:
            for item in ticket_origin_custom_field_values_items:
                ticket_origin_custom_field_values_items_person_id = item['personId']
                ticket_origin_custom_field_values_items_client_id = item['clientId']
                ticket_origin_custom_field_values_items_team = item['team']
                ticket_origin_custom_field_values_items_custom_field_item = item['customFieldItem']
                ticket_origin_custom_field_values_items_storage_file_guid = item['storageFileGuid']
                ticket_origin_custom_field_values_items_file_name = item['fileName']

        custom_field_ticket_dict = {
            "customFieldId": ticket_origin_custom_field_values_custom_field_id,
            "customFieldRuleId": ticket_origin_custom_field_values_custom_field_rule_id,
            "line": ticket_origin_custom_field_values_line,
            "value": ticket_origin_custom_field_values_value,
            "items": [
                {
                    'person_id': ticket_origin_custom_field_values_items_person_id,
                    'client_id': ticket_origin_custom_field_values_items_client_id,
                    'team': ticket_origin_custom_field_values_items_team,
                    'custom_field_item': ticket_origin_custom_field_values_items_custom_field_item,
                    'storage_file_guid': ticket_origin_custom_field_values_items_storage_file_guid,
                    'file_name': ticket_origin_custom_field_values_items_file_name
                }] if ticket_origin_custom_field_values_items else []
        }
        ticket_destin_custom_field_values.append(custom_field_ticket_dict)
        i = ticket_destin_custom_field_values

ticket_origin_assets = ticket_origin['assets']
ticket_destin_assets = []
if ticket_origin_assets:
    for assent in ticket_origin_assets:
        ticket_origin_assets_id = assent['id']
        ticket_origin_assets_name = assent['name']
        ticket_origin_assets_label = assent['label']
        ticket_origin_assets_serial_number = assent['serialNumber']
        ticket_origin_assets_category_full = assent['categoryFull']
        ticket_origin_assets_category_first_level = assent['categoryFirstLevel']
        ticket_origin_assets_category_second_level = assent['categorySecondLevel']
        ticket_origin_assets_category_third_level = assent['categoryThirdLevel']
        ticket_origin_assets_is_deleted = assent['isDeleted']

        ticket_origin_assets_dict = {
            "id": ticket_origin_assets_id,
            "name": ticket_origin_assets_name,
            "label": ticket_origin_assets_label,
            "serialNumber": ticket_origin_assets_serial_number,
            "categoryFull": ticket_origin_assets_category_full if ticket_origin_assets_category_full else [],
            "categoryFirstLevel": ticket_origin_assets_category_first_level,
            "categorySecondLevel": ticket_origin_assets_category_second_level,
            "categoryThirdLevel": ticket_origin_assets_category_third_level,
            "isDeleted": ticket_origin_assets_is_deleted
        }
        ticket_destin_assets.append(ticket_origin_assets_dict)
        j = ticket_destin_assets

ticket_origin_webhook_events = ticket_origin['webhookEvents']
