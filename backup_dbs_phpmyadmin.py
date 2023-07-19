# Libs
import os
import requests as r
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

# Inicio de sesión
s = r.Session()
loginData = {'pma_username': os.getenv('PMA_USER'), 'pma_password': os.getenv('PMA_PASS'), 'target': 'index.php', 'server': '1'}
res1 = s.post(os.getenv('DOMAIN') + "/index.php", data = loginData)

# Resultados del login
loginResContent = res1.text

# Extraer el token del login
soup = BeautifulSoup(loginResContent, 'html.parser')
element = soup.find('input', { 'name' : 'token' })
token = element.get('value')

# Exportar data
exportData = {
  'db': 'db_infoposg',
  'token': token,
  'export_type': 'database',
  'export_method': 'quick',
  'template_id': '',
  'quicl_or_custom': 'quick',
  'what': 'sql',
  'structure_or_data_forced': '0',
  'table_select[]': 'users_idiomas',
  'table_structure[]': 'users_idiomas',
  'table_data[]': 'users_idiomas',
  'output_format': 'sendit',
  'filename_template': '@DATABASE@',
  'remember_template': 'on',
  'charset': 'utf-8',
  'compression': 'none',
  'maxsize': '',
  'texytext_structure_or_data': 'structure_and_data',
  'texytext_null': 'NULL',
  'codegen_structure_or_data': 'data',
  'codegen_format': '0',
  'xml_structure_or_data': 'data',
  'xml_export_events': 'something',
  'xml_export_functions': 'something',
  'xml_export_procedures': 'something',
  'xml_export_tables': 'something',
  'xml_export_triggers': 'something',
  'xml_export_views': 'something',
  'xml_export_contents': 'something',
  'csv_separator': ',',
  'csv_enclosed': '"',
  'csv_escaped': '"',
  'csv_terminated': 'AUTO',
  'csv_null': 'NULL',
  'csv_structure_or_data': 'data',
  'htmlword_structure_or_data': 'structure_and_data',
  'htmlword_null': 'NULL',
  'excel_null': 'NULL',
  'excel_edition': 'win',
  'excel_structure_or_data': 'data',
  'mediawiki_structure_or_data': 'structure_and_data',
  'mediawiki_caption': 'something',
  'mediawiki_headers': 'something',
  'phparray_structure_or_data': 'data',
  'ods_null': 'NULL',
  'ods_structure_or_data': 'data',
  'json_structure_or_data': 'data',
  'odt_structure_or_data': 'structure_and_data',
  'odt_comments': 'something',
  'odt_columns': 'something',
  'odt_null': 'NULL',
  'yaml_structure_or_data': 'data',
  'sql_include_comments': 'something',
  'sql_header_comment': '',
  'sql_compatibility': 'NONE',
  'sql_structure_or_data': 'structure_and_data',
  'sql_create_table': 'something',
  'sql_auto_increment': 'something',
  'sql_create_view': 'something',
  'sql_procedure_function': 'something',
  'sql_create_trigger': 'something',
  'sql_backquotes': 'something',
  'sql_type': 'INSERT',
  'sql_insert_syntax': 'both',
  'sql_max_query_size': '50000',
  'sql_hex_for_binary': 'something',
  'sql_utc_time': 'something',
  'pdf_report_title': '',
  'pdf_structure_or_data': 'structure_or_data',
  'latex_caption': 'something',
  'latex_structure_or_data': 'structure_or_data',
  'latex_structure_caption': 'Estructura de a tabla @TABLE@',
  'latex_structure_continued_caption': 'Estructura de la tabla @TABLE@ (continúa)',
  'latex_structure_label': 'tab:@TABLE@-structure',
  'latex_comments': 'something',
  'latex_columns': 'something',
  'latex_data_caption': 'Contenido de la tabla @TABLE@',
  'latex_data_continued_caption': 'Contenido de la tabla @TABLE@ (continúa)',
  'latex_data_label': 'tab:@TABLE@-data',
  # 'latex_null': '\textit{NULL}',
}
res2 = s.post(os.getenv('DOMAIN') + "/export.php", data = exportData)

print("CODE: ", res2.status_code)

with open('file.sql', 'wb') as file:
  file.write(res2.content)