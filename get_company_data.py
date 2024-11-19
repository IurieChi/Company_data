import requests
import headers 
import json



def get_data_company(cui):
    """_summary_

    Args:
        cui (string): company unic ID 
    Returns:
        JSON: company details like{
                                    'cui': ,
                                    'denumire': ,
                                    'cod_inmatriculare': ,
                                    'euid': ,
                                    'adresa_completa': ,
                                    'localitate': ,
                                    'judet': ,
                                    'sector': ,
                                    'cod_stare': ,
                                    'stare': }
    """
    url = f"http://zimbor.go.ro/solr/firme/select?q.op=OR&q=cui%3A%22{cui}%22"

    #use session to create one request and extract all data.
    session = requests.Session()    
    response = session.get(url, headers = headers.defoult_headers)

    if response.status_code==200:
        data = response.json()
        company_data = data['response']['docs'][0]
        # extracted_data = {
        #                     'cui': company_data['cui'],
        #                     'denumire': company_data['denumire'][0],
        #                     'cod_inmatriculare': company_data['cod_inmatriculare'],
        #                     'euid': company_data['euid'],
        #                     'adresa_completa': company_data['adresa_completa'][0],
        #                     'localitate': company_data['localitate'][0],
        #                     'judet': company_data['judet'][0],
        #                     'sector': company_data['sector'][0],
        #                     'cod_stare': company_data['cod_stare'][0],
        #                     'stare': company_data['stare'][0]
        #                 }
        return company_data#json.dumps(extracted_data, indent=4)
        
    else:
        print(f'Error {response.status_code}')
