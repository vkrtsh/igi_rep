import pickle
import csv
from checking import check_input


class Product:
    def __init__(self, name, exporting_country, count):
        self.name = name
        self.exporting_country = exporting_country
        self.count = count


class ProductSummary:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def sort_products(self, key="name"):
        if key == "name":
            self.products.sort(key=lambda x: x.name)
        elif key == "country":
            self.products.sort(key=lambda x: x.exporting_country)
        elif key == "count":
            self.products.sort(key=lambda x: x.count)
        else:
            print("Invalid sort key")

    def find_countries_for_product(self, product_name):
        countries = set()
        total_count = 0
        for product in self.products:
            if product.name == product_name:
                countries.add(product.exporting_country)
                total_count += product.count
        return list(countries), total_count

    def save_to_csv(self, filename):
        with open(filename, "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Name", "Countries", "Count"])
            for product in self.products:
                writer.writerow([product.name, product.exporting_country, product.count])

    @staticmethod
    def load_from_csv(filename):
        product_summary = ProductSummary()
        with open(filename, "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                name, exporting_country, count = row
                product = Product(name, exporting_country, count)
                product_summary.add_product(product)
        return product_summary

    def save_to_pickle(self, filename):
        with open(filename, "wb") as pickle_file:
            pickle.dump(self.products, pickle_file)

    @staticmethod
    def load_from_pickle(filename):
        product_summary = ProductSummary()
        with open(filename, "rb") as pickle_file:
            product_summary.products = pickle.load(pickle_file)
        return product_summary


def task1_run():
    product_summary = ProductSummary()
    while True:
        print(
                "-----Choose an action-----\n"
                "1. Add a product\n"
                "2. Sorting products by country of export\n"
                "3. Sorting products by name\n"
                "4. Sorting products by count of goods\n"
                "5. Find products\n"
                "6. Save to csv\n"
                "7. Load from csv\n"
                "8. Save to pickle\n"
                "9. Load from pickle\n"
                "0. Exit\n"
                "--------------------------\n"
            )
        choice = check_input("Enter the number ", 0, 9, int)
        match choice:
            case 0:
                break
            case 1:
                name = check_input("Enter product name: ", 1, 100, str)
                country = check_input("Enter the exporters country: ", 1, 100, str)
                count = check_input("Enter the count of products: ", 1, 1000000, int)
                product_summary.add_product(Product(name, country, count))
            case 2:
                product_summary.sort_products(key="country")
                print("Products after sorting by export country: ")
                for product in product_summary.products:
                    print(f"{product.name}: {product.exporting_country}")
            case 3:
                product_summary.sort_products(key="name")
                print("Products after sorting by name:")
                for product in product_summary.products:
                    print(f"{product.name}: {product.exporting_country}: {product.count}")
            case 4:
                product_summary.sort_products(key="count")
                print("Products after sorting by count of products: ")
                for product in product_summary.products:
                    print(f" {product.name}: {product.count}")
            case 5:
                product_name = check_input("Enter the product name to search: ", 1, 100, str)
                found_product = product_summary.find_product(product_name)
                if found_product:
                    print(
                        f"Found product: {found_product.name} from country {found_product.exporting_country} in count {found_product.count}"
                    )
                else:
                    print("Product not found.")
            case 6:
                product_summary.save_to_csv("D://BSUIR_4sem//ИГИ//253501_ARTISH_1//IGI//LR4//task1//products.txt")
            case 7:
                product_summary = ProductSummary.load_from_csv("D://BSUIR_4sem//ИГИ//253501_ARTISH_1//IGI//LR4//task1//products.txt")
                for product in product_summary.products:
                    print(product.name, product.exporting_country, product.count)
            case 8:
                product_summary.save_to_pickle("D://BSUIR_4sem//ИГИ//253501_ARTISH_1//IGI//LR4//task1//products.pkl")
            case 9:
                product_summary = ProductSummary.load_from_pickle("D://BSUIR_4sem//ИГИ//253501_ARTISH_1//IGI//LR4//task1//products.pkl")
                for product in product_summary.products:
                    print(product.name, product.exporting_country, product.count)
