import boto3

from fastapi import APIRouter, HTTPException, Query

router = APIRouter()

s3 = boto3.client('s3')

@router.get("/list_buckets")
async def get_buckets():
    response = s3.list_buckets()
    return response

@router.get("/list_objects")
async def get_bucket(bucket_name: str = Query(...)):
    bucket_list = await get_buckets()
    for bucket in bucket_list['Buckets']:
        if bucket['Name'] == bucket_name:
            try:
                response = s3.list_objects_v2(Bucket=bucket_name)
                return response
            except Exception as e:
                raise HTTPException(status_code=404, detail=str(e))
        
    raise HTTPException(status_code=404, detail="Bucket not found")