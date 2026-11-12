class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        result = []
        prefix = ""

        for char in searchWord:
            prefix += char
            matches = []

            for product in products:
                if product.startswith(prefix):
                    matches.append(product)
                    if len(matches) == 3:
                        break

            result.append(matches)

        return result