from decouple import config
import motor.motor_asyncio

MONGO_URL = config("MONGO_URL")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

database = client.polo_api_db

polo_collection = database.get_collection("polo_api_collection")

# Helpers
def polo_helper(polo) -> dict:
    return {
        "id": str(polo["_id"]),
        "ad_link": polo["ad_link"],
        "asking_price": polo["asking_price"],
        "model_year": polo["model_year"],
        "kms_driven": polo["kms_driven"],
        "ad_title": polo["ad_title"],
        "ad_location": polo["ad_location"]
    }

async def retrieve_ad_listings():
    ad_listings = []
    async for listing in polo_collection.find():
        ad_listings.append(polo_helper(listing))
    return ad_listings

async def get_listing(id):
    listing = await polo_collection.find_one({"id": id})
    return listing

async def create_listing(listing):
    document = listing
    result = await  polo_collection.insert_one(document)
    return result

async def update_listing(id, data):
    await polo_collection.update_one({"id": id}, {"$set": data})
    document = await polo_collection.find_one({"id": id})
    return document

async def delete_listing(id):
    await polo_collection.delete_one({"id": id})
    return True

