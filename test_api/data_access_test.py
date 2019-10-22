from data_access import create_company, list_companies
from uuid import uuid4

def main():
    create_company('plated-valor-167300', 'Facebook', str(uuid4()))

if __name__ == '__main__':
    main()