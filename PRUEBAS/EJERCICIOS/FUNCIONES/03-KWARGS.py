#### KEYWORDS ARGUMENTS ####


def get_product(**datos):
    print(
        datos["id"], datos["clase"], datos["brand"]
    )  # Se hace la llamada ARGUMENTO x ARGUMENTO


get_product(
    id="0", clase="Phone", brand="Apple", desc="Iphone13"
)  # Se incluyen en la llamada todos los ARGUMENTOS que queramos
get_product(id="1", clase="Phone", brand="Samsung", desc="A25")
