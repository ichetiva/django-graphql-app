import json
import base64

import pytest
from django.conf import settings
from django.test.client import Client

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def file():
    header = "data:text/plain;base64,"
    with open(
        settings.BASE_DIR / "tests" / "files" / "test_upload_file.py", "rb"
    ) as fp:
        content = base64.b64encode(fp.read()).decode()
    return header + content


def test_upload_file(client_query, file):
    response = client_query(
        """
        mutation uploadFile($input: FileInput!) {
            uploadFile(input: $input) {
                id,
            }
        }
        """,
        op_name="uploadFile",
        input_data={"input": {"file": file}},
    )
    content = json.loads(response.content)
    assert True
