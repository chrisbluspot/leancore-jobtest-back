from typing import List
from fastapi import FastAPI, status, Path, HTTPException
from pydantic import BaseModel
from pydantic import Field
    

app = FastAPI(
    title="LeanShop",
    summary="Buy and sell the best products",
    version="0.0.1",
    contact={
        "name": "Christian Guzmán",
        "url": "https://www.linkedin.com/in/ccguzmane/",
        "email": "christian@leancore.co"
    }
)

class Product(BaseModel):
    id: str = Field(
        title="ID",
        description="ID of the Product",
        example="01d27307-95d9-48ae-bab7-6eb01a6cc04c",
        min_length=1,
        max_length=100,
    )
    name: str = Field(
        title="Name",
        description="Name of the Product",
        example="Xbox Series S - 512GB SSD Console with Wireless Controller - EU Version",
        min_length=1,
    )
    price: float = Field(
        title="Price",
        description="Price of the Product.",
        ge=0,
        example=299.99,
    )
    discount: float = Field(
        title="Discount",
        description="Discount price for the Product.",
        ge=0,
        example=25.0,
    )
    rating: float = Field(
        title="Rating",
        description="Rating of the Product.",
        ge=0,
        le=5,
        example=3.5
    )
    reviews_number: int = Field(
        title="Reviews number",
        description="Number of reviewas for the Product.",
        example=5345
    )
    summary: str = Field(
        title="Summary",
        description="A summary of the Product",
        example="Games built using the Xbox Series X|S development kit showcase unparalleled load times, visuals.",
        min_length=1,
    )
    image: str = Field(
        title="Image",
        description="The url for the image related with the Product",
        example="https://m.media-amazon.com/images/I/419QUnVtXiL._SX300_SY300_QL70_FMwebp_.jpg",
        min_length=1,
    )

class Purchase(BaseModel):
    product: str = Field(
        title="Product",
        description="The ID of the product to purchase",
        example="01d27307-95d9-48ae-bab7-6eb01a6cc04c",
        min_length=1,
        max_length=100
    )
    quantity: int = Field(
        title="Quantity",
        description="Amount of products to purchase",
        example=2,
        gt=0
    )

products = [
    Product(
        id= "01d27307-95d9-48ae-bab7-6eb01a6cc04c",
        name= "Xbox Series S - 512GB SSD Console with Wireless Controller - EU Version",
        price= 865.99,
        discount= 32.0,
        rating= 5,
        reviews_number= 52667,
        summary= "Games built using the Xbox Series X|S development kit showcase unparalleled load times, visuals.",
        image= "https://m.media-amazon.com/images/I/419QUnVtXiL._SX300_SY300_QL70_FMwebp_.jpg"
    ),
    Product(
        id= "d8853fd6-5b88-49ce-b869-08de069c000b",
        name= "Bose Sport Earbuds - Wireless Earphones - Bluetooth In Ear Headphones for Workouts and Running, Triple Black",
        price= 2300,
        discount= 0,
        rating= 4.2,
        reviews_number= 23653,
        summary= "Wireless Bluetooth earbuds engineered by Bose for your best workout yet..Note : If the size of the earbud tips does not match the size of your ear canals or the headset is not worn properly in your ears, you may not obtain the correct sound qualities or call performance. Change the earbud tips to ones that fit more snugly in your ears",
        image= "https://m.media-amazon.com/images/I/61Zv3ry4B7L.__AC_SX300_SY300_QL70_FMwebp_.jpg"
    ),
    Product(
        id= "52f4e074-9ae5-4c7f-8421-709d652a64b9",
        name= "Simple Mobile 4G LTE Prepaid Smartphone",
        price= 220,
        discount= 0,
        rating= 3.5,
        reviews_number= 30546,
        summary= "CARRIER: This phone is locked to Simple Mobile, which means this device can only be used on the Simple Mobile wireless network.",
        image= "https://m.media-amazon.com/images/I/7150tUunFnL._AC_SX679_.jpg"
    ),
    Product(
        id= "d56cb4d1-964a-4e6d-82af-77cdd59b0054",
        name= "4K UHD LED Smart TV with Chromecast Built-in",
        price= 865,
        discount= 19.0,
        rating= 3.8,
        reviews_number= 4786,
        summary= "4K Ultra HD Resolution - Enjoy TV in crystal-clear UHD resolution. Image Aspect ratio:16:9. Enjoy enhanced contrast, accurate colors and fine details utilizing all the most advanced HDR formats.",
        image= "https://m.media-amazon.com/images/I/71ZfLSxip-L.__AC_SX300_SY300_QL70_FMwebp_.jpg"
    ),
    Product(
        id= "5d4f7407-1d4c-4d5f-a484-763eaf4dc105",
        name= "Sony DSCHX8 High Zoom Point & Shoot Camera",
        price= 1200,
        discount= 0,
        rating= 4.8,
        reviews_number= 44682,
        summary= "30x Optical/60x Clear Image Zoom ZEISS Vario-Sonnar T* Lens, 18.2MP Exmor R CMOS Sensor for superb low light images, Built-in retractable OLED Tru-Finder viewfinder",
        image= "https://m.media-amazon.com/images/I/7172c2JXUlL._AC_SX679_.jpg"
    ),
    Product(
        id= "432e3606-1372-4256-8b07-b76270a33600",
        name= "Dell Optiplex 7000x7480 All-in-One Computer Monitor",
        price= 299,
        discount= 0,
        rating= 3.8,
        reviews_number= 15782,
        summary= "OptiPlex DesktopsOur most secure and manageable business-class desktops, delivering reliable productivity for your end-users. Manufacturer: Dell Technologies. Manufacturer Part Number: 6W8P2. Brand Name: Dell. Product Line: OptiPlex. Product Series: 7000. Product Model: 7480. Product Name: OptiPlex 7480 All-in-One Computer. Product Type: All-in-One Computer.",
        image= "https://m.media-amazon.com/images/I/511NyVhHXuL.__AC_SX300_SY300_QL70_FMwebp_.jpg"
    ),
    Product(
        id= "50b488c3-c627-4cc2-aa37-3703ce6a6802",
        name= "Portable Wshing Machine, 11lbs capacity Model 18NMFIAM",
        price= 865.99,
        discount= 25.0,
        rating= 4.1,
        reviews_number= 23633,
        summary= "Easy to Use: - This portable washing machine has 6 most commonly used programs including Normal, Quick, Heavy, Bulky, Delicate, and Spin Only. You are allowed to quickly start the machine the way you like. You can also add extra rinse time by pressing the “Extra Rinse” button. The washer also has 3 water temperatures, meet your different laundry needs. And it comes with a clear lid that allows you to look over the status of clothing at any time.",
        image= "https://m.media-amazon.com/images/I/61m2cCUhdbL._AC_SX679_.jpg"
    ),
    Product(
        id= "50313114-7b69-41d3-a307-3f3f7f34de17",
        name= "2-Barrel Carburetor Carb 2100 Engine Increase Horsepower",
        price= 160,
        discount= 0,
        rating= 3.1,
        reviews_number= 4321,
        summary= "Brand New Premium quality 2 Barrel Carburetor 2100 2150 A800 for Ford 289 302 351 Cu Jeep Engine F100 F250 F350 Jeep 360 Cu with Electric Chok. Aftermarket 2-Barrel Carburetor Replacement Heavy Duty Metal Construction.100% tested before shipment, the perfect choice to replace your defective carb assembly. Part Number: 2100 A800 2150.",
        image= "https://m.media-amazon.com/images/I/81cveyP8HrL.__AC_SX300_SY300_QL70_FMwebp_.jpg"
    ),
    Product(
        id= "bf1b5124-5ee1-4357-9a7d-5e99ea478379",
        name= "JBL FLIP 4 - Waterproof Portable Bluetooth Speaker - Black",
        price= 250,
        discount= 32,
        rating= 4.4,
        reviews_number= 42511,
        summary= "All-purpose Bluetooth speaker - Take the party everywhere with Flip 4, a portable Bluetooth speaker that delivers powerful stereo sound. With durable, waterproof fabric, this speaker features up to 12 hours of continuous, high-quality audio playtime.",
        image= "https://m.media-amazon.com/images/I/71P3we6mFrL._AC_SX679_.jpg"
    ),
]

@app.get("/")
async def root():
    return {"message": "Hello LeanShop"}

@app.get(
    path="/products/{product_id}",
    response_model=Product,
    status_code=status.HTTP_200_OK,
    summary="Get a Product by its ID"
)
async def read_product(product_id: str = Path(
        min_length=1,
        title="Product ID",
        description="This is the product ID. It must be greater than 1 character",
        example="bf1b5124-5ee1-4357-9a7d-5e99ea478379",
    )):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Error. Product with id {product_id} not found.")

@app.get(
    path="/products",
    response_model=List[Product],
    status_code=status.HTTP_200_OK,
    summary="Get all Products"
)
async def all_products():
    return products

@app.post(
    path="/purchase-products",
    response_model=List[Product],
    status_code=status.HTTP_201_CREATED,
    summary="Purchase products"
)
async def purchase_products(purchase: List[Purchase]):
    result = []
    for purchase_item in purchase:
        for product in products:
            if product.id == purchase_item.product:
                result.append(product)
    if len(result) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items in purchase object not found")
    return result