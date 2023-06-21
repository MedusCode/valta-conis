from marshmallow import pre_load

from src import ma
from src.components.product.product_model import Product
from src.constants.exception_message import ExceptionMessage
from src.helpers.marshmallow.handle_duplicates_conflicts import handle_duplicates_conflicts


class ProductDao(ma.SQLAlchemySchema):
    class Meta:
        model = Product

    product_integration_id = ma.auto_field()
    name = ma.auto_field()
    vendor_code = ma.auto_field()
    barcode = ma.auto_field()

    @pre_load()
    def load_duplicate_check(self, product, **_):
        handle_duplicates_conflicts(
            self.Meta.model,
            product,
            {
                "product_integration_id": ExceptionMessage.PRODUCT_INTEGRATION_ID_ALREADY_EXISTS.value,
                "barcode": ExceptionMessage.BARCODE_ALREADY_EXISTS.value,
                "vendor_code": ExceptionMessage.VENDOR_CODE_ALREADY_EXISTS.value
            },
            exception_message=ExceptionMessage.FAILED_TO_CREATE_PRODUCT.value
        )


product_dao = ProductDao()
products_dao = ProductDao(many=True)
