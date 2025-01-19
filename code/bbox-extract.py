import fitz  # PyMuPDF
from PIL import Image

def extract_img_from_polygon(pdf_path, page_number, polygon, dpi=72):
    doc = fitz.open(pdf_path)
    page = doc[page_number]
    print(f"Page dimensions: {page.rect}")
    
    pixmap = page.get_pixmap()
    w, h = pixmap.width, pixmap.height
    
    # Convert inch-based coordinates to pixels
    scaled_polygon = [(x * dpi, y * dpi) for x, y in zip(polygon[::2], polygon[1::2])]
    
    # Find the bounding box
    x_coords, y_coords = zip(*scaled_polygon)
    x1, y1 = int(min(x_coords)), int(min(y_coords))
    x2, y2 = int(max(x_coords)), int(max(y_coords))
    
    # Ensure coordinates are within the page bounds
    x1, y1 = max(0, x1), max(0, y1)
    x2, y2 = min(w, x2), min(h, y2)
    
    # Extract the image data
    image = Image.frombytes("RGB", [w, h], pixmap.samples)
    
    # Crop the image
    cropped_image = image.crop((x1, y1, x2, y2))
    
    cropped_image.show()
    
    doc.close()
    return cropped_image

# Example usage
pdf_path = "docs/src.pdf"
page_number = 10  # Page numbers are 0-indexed
polygon = [1.1235, 2.2592, 7.0518, 2.2594, 7.053, 7.2459, 1.1252, 7.245]
# polygon = [
#                         0.9846,
#                         8.8519,
#                         7.497,
#                         8.8544,
#                         7.4966,
#                         9.9668,
#                         0.9842,
#                         9.9644
#                     ]
extracted_image = extract_img_from_polygon(pdf_path, page_number, polygon)
