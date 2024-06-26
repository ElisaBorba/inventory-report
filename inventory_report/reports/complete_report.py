from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        stocked_products_str = self.stocked_products_str()

        report = super().generate()
        report += "Stocked products by company:\n"
        report += f"{stocked_products_str}\n"
        return report

    def stocked_products_str(self) -> str:
        stocked_count = Counter()
        for inventory in self.inventories:
            for product in inventory.data:
                stocked_count[product.company_name] += 1

        stocked_products_str = "\n".join(
            f"- {company_name}: {qty_products}"
            for company_name, qty_products in stocked_count.items()
        )

        return stocked_products_str
