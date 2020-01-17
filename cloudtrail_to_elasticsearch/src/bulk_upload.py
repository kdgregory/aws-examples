#!/usr/bin/env python3
################################################################################
# Copyright 2019 Chariot Solutions
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

""" Bulk-loads events that have been stored but not picked up by Lambda. This
    module is only intended to be invoked from the command-line:

        bulk_upload.py BUCKET_NAME PREFIX
"""

import sys

from es_helper import ESHelper
from processor import Processor
from s3_helper import S3Helper


if len(sys.argv) != 3:
    print(__doc__)
    sys.exit(1)

# the helpers are constructed as separate objects so we can test with different params
es = ESHelper(use_https=False)
s3 = S3Helper()

processor = Processor(es, s3)
s3.iterate_bucket(sys.argv[1], sys.argv[2], processor.process_from_s3)
