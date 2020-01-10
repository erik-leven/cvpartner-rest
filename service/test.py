from flask import json
import json
entities = [{'override_language_code': None, 'include_officeless_reference_projects': False, 'deactivated': True,'deactivated_at': False, 'preferred_download_format': 'pdf-from-word', 'default_cv_id': '5e15fd3d275c790f706ef11c', 'international_toggle': 'expand', 'deactivated': False, 'image': {'url': None, 'fit_thumb': {'url': None}, 'large': {'url': None}, 'small_thumb': {'url': None}, 'thumb': {'url': None}}, 'telephone': '+4712345678', 'default_cv_template_id': '5a58b7d47da82e0ea9f3801b', 'country_code': 'no', 'language_code': 'no', 'selected_office_ids': [], 'id': '5e15fd3c275c790f706ef11b', 'user_id': '5e15fd3c275c790f706ef11b', 'country_id': '5085b1c5a6add17a1500000d', 'company_id': '4f460a2de8ee2a74be000001', 'company_subdomains': ['bouvet'], 'selected_tag_ids': [], 'language_codes': ['no', 'int', 'se'], 'role': 'external', 'company_name': 'Bouvet', 'email': 'vincent.cogtas@bouvet.no', 'masterdata_languages': ['no', 'int', 'se'], 'expand_proposals_toggle': True, 'company_group_ids': [], 'role_allowed_tag_ids': [], 'upn': 'vincent.cogtas@bouvet.no', 'office_name': 'Region \xd8st', 'name': 'Vincent Cogtas', 'roles': ['external'], 'role_allowed_office_ids': [], 'office_id': '5761326569702d4e41000000', '_id': '5e15fd3c275c790f706ef11b', 'external_unique_id': '3370'}, {'override_language_code': None, 'include_officeless_reference_projects': True, 'deactivated_at': False, 'preferred_download_format': 'pdf-from-word', 'default_cv_id': '58530d9af278af7e829fd0fd', 'international_toggle': 'hide'},{'override_language_code': None, 'include_officeless_reference_projects': False, 'deactivated_at': False, 'preferred_download_format': 'pdf-from-word', 'default_cv_id': '5e15fd3d275c790f706ef11c', 'international_toggle': 'expand', 'deactivated': False, 'image': {'url': None, 'fit_thumb': {'url': None}, 'large': {'url': None}, 'small_thumb': {'url': None}, 'thumb': {'url': None}}, 'telephone': '+4712345678', 'default_cv_template_id': '5a58b7d47da82e0ea9f3801b', 'country_code': 'no', 'language_code': 'no', 'selected_office_ids': [], 'id': '5e15fd3c275c790f706ef11b', 'user_id': '5e15fd3c275c790f706ef11b', 'country_id': '5085b1c5a6add17a1500000d', 'company_id': '4f460a2de8ee2a74be000001', 'company_subdomains': ['bouvet'], 'selected_tag_ids': [], 'language_codes': ['no', 'int', 'se'], 'role': 'external', 'company_name': 'Bouvet', 'email': 'vincent.cogtas@bouvet.no', 'masterdata_languages': ['no', 'int', 'se'], 'expand_proposals_toggle': True, 'company_group_ids': [], 'role_allowed_tag_ids': [], 'upn': 'vincent.cogtas@bouvet.no', 'office_name': 'Region \xd8st', 'name': 'Vincent Cogtas', 'roles': ['external'], 'role_allowed_office_ids': [], 'office_id': '5761326569702d4e41000000', '_id': '5e15fd3c275c790f706ef11b', 'external_unique_id': '3370'}, {'override_language_code': None, 'include_officeless_reference_projects': True, 'deactivated_at': False, 'preferred_download_format': 'pdf-from-word', 'default_cv_id': '58530d9af278af7e829fd0fd', 'international_toggle': 'hide'},{'override_language_code': None, 'include_officeless_reference_projects': False, 'deactivated_at': False, 'preferred_download_format': 'pdf-from-word', 'default_cv_id': '5e15fd3d275c790f706ef11c', 'international_toggle': 'expand', 'deactivated': False, 'image': {'url': None, 'fit_thumb': {'url': None}, 'large': {'url': None}, 'small_thumb': {'url': None}, 'thumb': {'url': None}}, 'telephone': '+4712345678', 'default_cv_template_id': '5a58b7d47da82e0ea9f3801b', 'country_code': 'no', 'language_code': 'no', 'selected_office_ids': [], 'id': '5e15fd3c275c790f706ef11b', 'user_id': '5e15fd3c275c790f706ef11b', 'country_id': '5085b1c5a6add17a1500000d', 'company_id': '4f460a2de8ee2a74be000001', 'company_subdomains': ['bouvet'], 'selected_tag_ids': [], 'language_codes': ['no', 'int', 'se'], 'role': 'external', 'company_name': 'Bouvet', 'email': 'vincent.cogtas@bouvet.no', 'masterdata_languages': ['no', 'int', 'se'], 'expand_proposals_toggle': True, 'company_group_ids': [], 'role_allowed_tag_ids': [], 'upn': 'vincent.cogtas@bouvet.no', 'office_name': 'Region \xd8st', 'name': 'Vincent Cogtas', 'roles': ['external'], 'role_allowed_office_ids': [], 'office_id': '5761326569702d4e41000000', '_id': '5e15fd3c275c790f706ef11b', 'external_unique_id': '3370'}, {'override_language_code': None, 'include_officeless_reference_projects': True, 'deactivated_at': False, 'preferred_download_format': 'pdf-from-word', 'default_cv_id': '58530d9af278af7e829fd0fd', 'international_toggle': 'hide'},{'override_language_code': None, 'include_officeless_reference_projects': False, 'deactivated_at': False, 'preferred_download_format': 'pdf-from-word', 'default_cv_id': '5e15fd3d275c790f706ef11c', 'international_toggle': 'expand', 'deactivated': False, 'image': {'url': None, 'fit_thumb': {'url': None}, 'large': {'url': None}, 'small_thumb': {'url': None}, 'thumb': {'url': None}}, 'telephone': '+4712345678', 'default_cv_template_id': '5a58b7d47da82e0ea9f3801b', 'country_code': 'no', 'language_code': 'no', 'selected_office_ids': [], 'id': '5e15fd3c275c790f706ef11b', 'user_id': '5e15fd3c275c790f706ef11b', 'country_id': '5085b1c5a6add17a1500000d', 'company_id': '4f460a2de8ee2a74be000001', 'company_subdomains': ['bouvet'], 'selected_tag_ids': [], 'language_codes': ['no', 'int', 'se'], 'role': 'external', 'company_name': 'Bouvet', 'email': 'vincent.cogtas@bouvet.no', 'masterdata_languages': ['no', 'int', 'se'], 'expand_proposals_toggle': True, 'company_group_ids': [], 'role_allowed_tag_ids': [], 'upn': 'vincent.cogtas@bouvet.no', 'office_name': 'Region \xd8st', 'name': 'Vincent Cogtas', 'roles': ['external'], 'role_allowed_office_ids': [], 'office_id': '5761326569702d4e41000000', '_id': '5e15fd3c275c790f706ef11b', 'external_unique_id': '3370'}, {'override_language_code': None, 'include_officeless_reference_projects': True, 'deactivated_at': False, 'preferred_download_format': 'pdf-from-word', 'default_cv_id': '58530d9af278af7e829fd0fd', 'international_toggle': 'hide'}]
for ent in entities:
  print(ent.get("deactivated", ""))
