from typing import Dict, List, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]: ...


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        product_list = []

        try:
            with open(self.path, "r") as file:
                json_data = file.read()
                products = json.loads(json_data)

                for product_dict in products:
                    product_list.append(Product(**product_dict))

        except (FileNotFoundError, json.JSONDecodeError) as e:

            print(f"Erro ao importar dados: {e}")

        return product_list


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
