from inventory_report.reports.report import Report
from inventory_report.inventory import Inventory
from datetime import datetime
from collections import Counter


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventories = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        now = datetime.today().date()
        oldest_manufacture = self.find_oldest_manufacture()
        expiration_date = self.find_closest_expiration_date(now)
        company_name = self.find_largest_company_name()

        return (
            f"Oldest manufacturing date: {oldest_manufacture}\n"
            f"Closest expiration date: {expiration_date}\n"
            f"Company with the largest inventory: {company_name}\n"
        )

    def find_oldest_manufacture(self) -> str:
        oldest_manufacture = None
        for inventory in self.inventories:
            for product in inventory.data:
                manufacturing_date = datetime.strptime(
                    product.manufacturing_date, "%Y-%m-%d"
                ).date()
                if (
                    oldest_manufacture is None
                    or manufacturing_date < oldest_manufacture
                ):
                    oldest_manufacture = manufacturing_date
        return str(oldest_manufacture)

    def find_closest_expiration_date(self, now: datetime.date) -> str:
        valid_products = []
        for inventory in self.inventories:
            for product in inventory.data:
                expiration_date = datetime.strptime(
                    product.expiration_date, "%Y-%m-%d"
                ).date()
                if expiration_date >= now:
                    valid_products.append(product)

        expiration_date = min(
            valid_products,
            key=lambda product: datetime.strptime(
                product.expiration_date, "%Y-%m-%d"
            ),
        ).expiration_date

        return expiration_date

    # Empresa com o maior estoque, ou seja, aquela que + repete.
    def find_largest_company_name(self) -> str:
        companies_count = Counter()
        for inventory in self.inventories:
            for product in inventory.data:
                companies_count[product.company_name] += 1

        largest_company = companies_count.most_common(1)[0][0]
        return largest_company
