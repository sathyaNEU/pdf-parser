from diagrams import Diagram
from diagrams.aws.storage import S3
from diagrams.azure.ml import CognitiveServices as cs
from diagrams.programming.language import Python as py

# Specify the path to save the diagram
output_path = "artifacts/pdf_parsing_diagram"

with Diagram("PDF Parsing Using Azure Document Intelligence", show=False, filename=output_path):
    python_node = py("Python")
    cs_node = cs("Document Intelligence")
    s3_node = S3("S3")
    python_node >> cs_node
    s3_node >> python_node
    cs_node >> python_node