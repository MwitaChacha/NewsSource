from app import app
import urllib.request,json
from .models import source

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

def process_results(source_list):
    """
    Function that processes the source result and transform them into a list of objects
    Args:
    source_list: A list of dictionaries that contain movie details
    Returns:
    source_results: A list of Source objects
    """
    source_results=[]
    for source_item in source_list:
        id = source_item.get("id")
        name = source_item.get("name")
        description = source_item.get("description")
        url = source_item.get("url")
        category = source_item.get("category")


        source_object=source.Source(id,name,description,url,category)
        source_results.append(source_object)

       

    return source_results