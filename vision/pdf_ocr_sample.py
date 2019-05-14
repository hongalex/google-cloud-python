from google.cloud import vision_v1 as vision

client = vision.ImageAnnotatorClient()

pdf_file = 'gs://cloud-samples-data/vision/document/three_pages.pdf'

request = vision.types.AnnotateFileRequest(
    input_config=vision.types.InputConfig(
        mime_type='application/pdf',
        gcs_source=vision.types.GcsSource(uri=pdf_file)
    ),
    features=[
        vision.types.Feature(type=vision.enums.Feature.Type.DOCUMENT_TEXT_DETECTION)
    ]
)

response = client.batch_annotate_files(requests=[request])

for annotation_response in response.responses:
  print('Total Pages: {}'.format(annotation_response.total_pages))
  for image_response in annotation_response.responses:
    text_annotation = image_response.full_text_annotation
    print('Page text: {}'.format(text_annotation.text))
    for page in text_annotation.pages:
      for block in page.blocks:
        for paragraph in block.paragraphs:
          for word in paragraph.words:
            word_text = ''.join([symbol.text for symbol in word.symbols])
            print(word_text)