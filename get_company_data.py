import requests
import headers as h 
import json



def get_data_company(cui):
    url = f"http://zimbor.go.ro:8985/solr/firme/select?indent=true&q=cui%3A%22{cui}%22"

    #use session to create one rrequest and extract all data.
    session = requests.Session()    
    response = session.get(url, headers = h.defoult_headers)

    if response.status_code==200:
        data = response.json()
        company_data = data['response']['docs'][0]
        extracted_data = {
                            'cui': company_data['cui'],
                            'denumire': company_data['denumire'][0],
                            'cod_inmatriculare': company_data['cod_inmatriculare'],
                            'euid': company_data['euid'],
                            'adresa_completa': company_data['adresa_completa'][0],
                            'localitate': company_data['localitate'][0],
                            'judet': company_data['judet'][0],
                            'sector': company_data['sector'][0],
                            'cod_stare': company_data['cod_stare'][0],
                            'stare': company_data['stare'][0]
                        }
        return json.dumps(extracted_data, indent=4)
        
    else:
        print(f'Error {response.status_code}')
