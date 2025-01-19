from dotenv import load_dotenv
import os
import json
load_dotenv()


endpoint = os.getenv("AZURE_DOC_INT_ENDPOINT")
key = os.getenv("AZURE_DOC_INT_KEY")


from azure.core.credentials import AzureKeyCredential
# from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeOutputOption, AnalyzeDocumentRequest

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
print(endpoint,key)

# sample document
formUrl = "https://sfopenaccessbucket.s3.us-east-1.amazonaws.com/src.pdf"


document_intelligence_client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    
poller = document_intelligence_client.begin_analyze_document(
    "prebuilt-layout",
    AnalyzeDocumentRequest(url_source=formUrl),
    pages="11",
    output=[AnalyzeOutputOption.FIGURES]
)

# document_analysis_client = DocumentAnalysisClient(
#     endpoint=endpoint, credential=AzureKeyCredential(key)
# )

# poller = document_analysis_client.begin_analyze_document_from_url(
#     "prebuilt-layout", formUrl, pages="11"
# )       

result = poller.result()
operation_id = poller.details["operation_id"]


# print("----Key-value pairs found in document----")
# for kv_pair in result.key_value_pairs:
#     if kv_pair.key and kv_pair.value:
#         print("Key '{}': Value: '{}'".format(kv_pair.key.content, kv_pair.value.content))
#     else:
#         print("Key '{}': Value:".format(kv_pair.key.content))

# print("----------------------------------------")

# print("Tables found in document")
# if result.tables:
#         for table_idx, table in enumerate(result.tables):
#             print(f"Table # {table_idx} has {table.row_count} rows and " f"{table.column_count} columns")
#             if table.bounding_regions:
#                 for region in table.bounding_regions:
#                     print(f"Table # {table_idx} location on page: {region.page_number} is {region.polygon}")
#             # Analyze cells.
#             for cell in table.cells:
#                 print(f"...Cell[{cell.row_index}][{cell.column_index}] has text '{cell.content}'")
#                 if cell.bounding_regions:
#                     for region in cell.bounding_regions:
#                         print(f"...content on page {region.page_number} is within bounding polygon '{region.polygon}'")
# print("----------------------------------------")

# print("Figures found in document:")
# if result.figures:                    
#     for figures_idx,figures in enumerate(result.figures):
#         print(f"Figure # {figures_idx} has the following spans:{figures.spans}")
#         for region in figures.bounding_regions:
#             print(f"Figure # {figures_idx} location on page:{region.page_number} is within bounding polygon '{region.polygon}'")                    

# print("----------------------------------------")

if result.figures:
    for figure in result.figures:
        if figure.id:
            response = document_intelligence_client.get_analyze_result_figure(
                model_id=result.model_id, result_id=operation_id, figure_id=figure.id
            )
            with open(f"artifacts/{figure.id}.png", "wb") as writer:
                writer.writelines(response)
else:
    print("No figures found.")

with open('artifacts/data.json', 'w') as file:
    json.dump(result.as_dict(), file)
