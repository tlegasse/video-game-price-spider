from abc import ABC, abstractclassmethod


class ProductDataWriter(ABC):
    @abstractclassmethod
    def set_product_data(self) -> None:
        """
            Sets product_data
        """

    @abstractclassmethod
    def write_product_data(self) -> None :
        """
            Writes product data.
        """

    @abstractclassmethod
    def set_console(self, console: str) -> None :
        """
            Sets selected console
        """
