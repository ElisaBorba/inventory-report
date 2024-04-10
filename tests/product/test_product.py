from inventory_report.product import Product


def test_create_product() -> None:
    """Testa se o método de criação de produto está funcionando"""

    # Arrange
    product_data = {
        "id": "1",
        "product_name": "Produto Teste",
        "company_name": "Empresa Teste",
        "manufacturing_date": "2022-01-01",
        "expiration_date": "2023-01-01",
        "serial_number": "123456789",
        "storage_instructions": "Armazenar em um lugar seguro",
    }

    # Act
    instance = Product(**product_data)

    # Assert
    assert instance.id == "1"
    assert instance.product_name == "Produto Teste"
    assert instance.company_name == "Empresa Teste"
    assert instance.manufacturing_date == "2022-01-01"
    assert instance.expiration_date == "2023-01-01"
    assert instance.serial_number == "123456789"
    assert instance.storage_instructions == "Armazenar em um lugar seguro"
