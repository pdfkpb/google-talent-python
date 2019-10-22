from google.cloud import talent_v4beta1
import six


def list_companies(project_id):
    """List Companies"""

    client = talent_v4beta1.CompanyServiceClient()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    parent = client.project_path(project_id)

    # Iterate over all results
    for response_item in client.list_companies(parent):
        print('Company Name: {}'.format(response_item.name))
        print('Display Name: {}'.format(response_item.display_name))
        print('External ID: {}'.format(response_item.external_id))


def create_company(project_id, display_name, external_id):
    """Create Company"""

    client = talent_v4beta1.CompanyServiceClient()

    # project_id = 'Your Google Cloud Project ID'
    # tenant_id = 'Your Tenant ID (using tenancy is optional)'
    # display_name = 'My Company Name'
    # external_id = 'Identifier of this company in my system'

    if isinstance(project_id, six.binary_type):
        project_id = project_id.decode('utf-8')
    if isinstance(display_name, six.binary_type):
        display_name = display_name.decode('utf-8')
    if isinstance(external_id, six.binary_type):
        external_id = external_id.decode('utf-8')
    parent = client.project_path(project_id)
    company = {'display_name': display_name, 'external_id': external_id}

    response = client.create_company(parent, company)
    print(response)
    print('Created Company')
    print('Name: {}'.format(response.name))
    print('Display Name: {}'.format(response.display_name))
    print('External ID: {}'.format(response.external_id))
