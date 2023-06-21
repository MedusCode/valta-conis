from src import ma
from src.components.wallet.wallet_model import Wallet


class WalletDao(ma.SQLAlchemySchema):
    class Meta:
        model = Wallet

    id = ma.auto_field()
    vc_balance = ma.auto_field()
    vc_service_balance = ma.auto_field()


wallet_dao = WalletDao()
