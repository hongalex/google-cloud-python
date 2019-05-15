# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT! This is a generated sample ("Request",  "vision_ocr_pdf_gcs")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-vision

import sys

# [START vision_ocr_pdf_gcs]

from google.cloud import vision_v1
from google.cloud.vision_v1 import enums


def sample_batch_annotate_files():
    """Perform OCR on a .pdf file stored in Cloud Storage"""
    # [START vision_ocr_pdf_gcs_core]

    client = vision_v1.ImageAnnotatorClient()

    mime_type = 'application/pdf'
    uri = 'gs://cloud-samples-data/vision/document/three_pages.pdf'
    gcs_source = {'uri': uri}
    input_config = {'mime_type': mime_type, 'gcs_source': gcs_source}
    type_ = enums.Feature.Type.DOCUMENT_TEXT_DETECTION
    features_element = {'type': type_}
    features = [features_element]
    requests_element = {'input_config': input_config, 'features': features}
    requests = [requests_element]

    response = client.batch_annotate_files(requests)
    # Get the response for the first request (hello_world.pdf)
    first_response = response.responses[0]
    print('Total pages: {}'.format(first_response.total_pages))
    for image_response in first_response.responses:
        text_annotation = image_response.full_text_annotation
        print('Full text: {}'.format(text_annotation.text))

    # [END vision_ocr_pdf_gcs_core]


# [END vision_ocr_pdf_gcs]


def main():
    sample_batch_annotate_files()


if __name__ == '__main__':
    main()
