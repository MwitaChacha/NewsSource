from app import app
import urllib.request,json
from .models import source,article

# Getting api key
apiKey = app.config['API_KEY']

# Getting base url
base_url = app.config['NEWS_SOURCE_API_URL']

def get_sources():
    """
    Function that gets the json response to our url request
    """
    get_sources_url = base_url.format(apiKey)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results= None

        if get_sources_response["sources"]:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results