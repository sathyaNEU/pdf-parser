from dotenv import load_dotenv
import os
load_dotenv()


endpoint = os.getenv("AZURE_DOC_INT_ENDPOINT")
key = os.getenv("AZURE_DOC_INT_KEY")


from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
print(endpoint,key)

# # sample document
# formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"

# document_analysis_client = DocumentAnalysisClient(
#         endpoint=endpoint, credential=AzureKeyCredential(key)
#     )
    
# poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-document", formUrl)
# result = poller.result()

# print("----Key-value pairs found in document----")
# for kv_pair in result.key_value_pairs:
#     if kv_pair.key and kv_pair.value:
#         print("Key '{}': Value: '{}'".format(kv_pair.key.content, kv_pair.value.content))
#     else:
#         print("Key '{}': Value:".format(kv_pair.key.content))

# print("----------------------------------------")
