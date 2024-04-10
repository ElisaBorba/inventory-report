from inventory_report.product import Product


def test_product_report() -> None:
    """
    Testa se o "método mágico" str do objeto Product retorna a frase correta
    """

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
    assert (
        product.__str__() == "The product 1 - Teste "
        "with serial number 123456789 "
        "manufactured on 2022-01-01 "
        "by the company Empresa Teste "
        "valid until 2023-01-01 "
        "must be stored according to the following instructions: "
        "Armazenar em um lugar seguro."
    )
