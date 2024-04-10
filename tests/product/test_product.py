from inventory_report.product import Product


def test_create_product() -> None:
    """Testa se o método de criação de produto está funcionando"""

    # Arrange
    product_data = {
        "id": "1",
        "product_name": "Teste",
        "company_name": "Empresa Teste",
        "manufacturing_date": "2022-01-01",
        "expiration_date": "2023-01-01",
        "serial_number": "123456789",
        "storage_instructions": "Armazenar em um lugar seguro",
    }

    # Act
    product = Product(**product_data)

    # Assert
    assert product.id == "1"
    assert product.product_name == "Teste"
    assert product.company_name == "Empresa Teste"
    assert product.manufacturing_date == "2022-01-01"
    assert product.expiration_date == "2023-01-01"
    assert product.serial_number == "123456789"
    assert product.storage_instructions == "Armazenar em um lugar seguro"
