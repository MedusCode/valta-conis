# Valta-coins back-end

___
## End-points:

___
#### POST `/user`

Создает нового пользователя в системе

#### Body 
```
{
    "user_integration_id": String,
    "login": String,
    "email"?: String,
    "password": String,
    "first_name": String,
    "last_name": String,
    "second_name"?: String,
    "phone_number": String,
    "new_policy_integration_id": String,
    "sales_channel_integration_id": String
}
```
___
#### GET `/user/{user_integration_id}`

Поиск пользователя по id

#### Params 
```
"user_integration_id": String
```
___
#### GET `/user`

Получение инициалов и wallet_id по email или phone_number или login

#### Body 
```
{
    "login"?: String,
    "email"?: String,
    "phone_number"?: String,
}
```
___
#### GET `/user/me`

Получение информции о себе
___
#### POST `/login`

Получение Access Token

#### Body 
```
{
    "login": String,
    "password": String,
}
```
___
#### POST `/transaction/transfer/{wallet_id}`

Отправить coins другому пользователю

#### Params 
```
"wallet_id": String
```
#### Body 
```
{
    "amount": Integer,
}
```
___
#### GET `/transaction/token`

Получение Transaction token
___
#### GET `/transaction/count` (в разработке)

Подсчитывает возможное количество начисления или списания coins

#### Body 
```
{
    "transaction_token": String,
    "trading_point_integration_id": String,
    "order_amount": Float,
    "delivery_type_integration_id": String,
    "payment_type_integration_id": String,
    "filial_integration_id": String,
    "products": [
        {
            "product_integration_id": String,
            "vendor_code": String,
            "barcode": String,
            "name": String,
            "quantity": Float,
            "price": Float,
            "user_price": Float,
            "automatic_discount": Integer,
            "total_amount": Float
        }
    ]
}
```
___
#### POST `/transaction/order` (в разработке)

Создает новый заказ

#### Body 
```
{
    "transaction_token": String, 
    "order_integration_id": String,
    "resource_integration_id": String,
    "trading_point_integration_id": String,
    "order_amount": Float,
    "order_date"?: Date,
    "address_integration_id"?: String,
    "delivery_address"?: String,
    "delivery_type_integration_id": String,
    "payment_type_integration_id": String,
    "filial_integration_id": String,
    "consultant_integration_id"?: String,
    "products": [
        {
            "product_integration_id": String,
            "vendor_code"?: String,
            "barcode"?: String,
            "name"?: String,
            "quantity": Float,
            "price": Float,
            "user_price": Float,
            "automatic_discount": Integer,
            "total_amount": Float,
        }
    ]
}
```
___
#### GET `/product`

Получение всех продуктов 
___
#### GET `/product/{product_integration_id}`

Поиск продукта по id

#### Params 
```
"product_integration_id": String
```
___
#### POST `/product`

Создает новый продукт в системе

#### Body 
```
{
    "product_integration_id": String,
    "name": String,
    "vendor_code": String,
    "barcode": String,
}
```
___
#### PATCH `/product/{product_integration_id}`

Обновляет ифнормацию о продукте в системе

#### Params 
```
"product_integration_id": String
```
#### Body 
```
{
    "product_integration_id": String,
    "name": String,
    "vendor_code": String,
    "barcode": String,
}
```
___
#### DELETE `/product/{product_integration_id}`

Удаляет продукт из систесы

#### Params 
```
"product_integration_id": String
```
___
