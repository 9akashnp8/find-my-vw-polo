from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from database import (
    retrieve_ad_listings,
    get_listing,
    create_listing,
    update_listing,
    delete_listing
)
from models import (
    ErrorResponseModel,
    ResponseModel,
    PoloSchema
)

router = APIRouter()

@router.get("/", response_description="Polo Listings retrieved")
async def get_listings():
    listings = await retrieve_ad_listings()
    if listings:
        return ResponseModel(listings, "Listings successfully retrieved")
    return ResponseModel(listings, "Empty List Returned")

@router.get("/{id}")
async def get_polo_listing_by_id(id):
    response = await get_listing(id)
    if response:
        return ResponseModel(response, "Retrieved Listing")
    raise HTTPException(404, "There is no listing with this ID")

@router.post("/")
async def create_polo_listing(listing: PoloSchema):
    response = await create_listing(listing.dict())
    if response:
        return ResponseModel(response, "Created Listing")
    raise HTTPException(400, "Something went wrong")

@router.put("/{id}")
async def update_polo_listing(id, listing: PoloSchema):
    response = await update_listing(id, listing)
    if response:
        return ResponseModel(response, "Updated Listing")
    raise HTTPException(404, "There is no listing with this ID")

@router.delete("/{id}")
async def delete_polo_listing(id):
    response = await delete_listing(id)
    if response:
        return "Successfully deleted"
    raise HTTPException(404, "There is no listing with this ID")