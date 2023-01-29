from fastapi import FastAPI, HTTPException
from app.Product import Product


ProductList: list[Product] = [
    Product(0, 'Бытавая техника', 'Электрическая плита', 'поверхность - эмалированная сталь, конфорок - 2 шт'),
    Product(1, 'Компьютерная техника', 'Ноутбук Acer', 'Full HD (1920x1080), IPS, Intel Core i5-11400H'),
    Product(2, 'Смартфоны', 'Xioami', 'ядер - 4x(2 ГГц), 2 Гб, 2 SIM, IPS, 1600x720'),

]

app = FastAPI()


@app.get("/v1/product")
async def get_product():
    return ProductList


@app.get("/v1/product/{id}")
async def get_product_by_id(id: int):
    result = [item for item in ProductList if item.id == id]
    if len(result) > 0:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail="Product not found")

