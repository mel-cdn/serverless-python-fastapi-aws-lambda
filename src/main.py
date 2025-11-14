import asyncio
import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/", include_in_schema=False)
def root():
    return {
        "message": "Welcome to FastAPI from AWS Lambda!",
        "docs": "/docs",
        "redoc": "/redoc",
    }


# ======================================================================================================================
# BASIC SYNC VERSION
# ======================================================================================================================
# @app.get("/clients/{client_id}")
# def get_client(client_id: int):
#     print(f'[client_id={client_id}] Request received.')
#     response = get_client_from_repo(client_id=client_id)
#     print(f'[client_id={client_id}] Done.')
#     return response
#
#
# def get_client_from_repo(client_id: int):
#     print(f'[client_id={client_id}] Getting client from repo...')
#
#     # This is the long-running process getting data from a database
#     for r in range(5):
#         print(f'[client_id={client_id}] {r}')
#         time.sleep(1)
#
#     return {
#         "clientId": client_id,
#         "title": "Engr.",
#         "firstName": "Bryce",
#         "lastName": "Hernandez",
#     }


# ======================================================================================================================
# BASIC SYNC VERSION - WHY SHOULD WE ASYNC???
# ======================================================================================================================
# @app.get("/clients/{client_id}/objects")
# def get_client(client_id: int):
#     start = time.time()
#
#     print(f'[client_id={client_id}] Request received.')
#     assets = get_assets_from_repo(client_id=client_id)  # 5 seconds
#     contact_details = get_contact_details_from_repo(client_id=client_id)  # 5 seconds
#     pensions = get_pensions_from_repo(client_id=client_id)  # 5 seconds
#
#     elapsed = time.time() - start
#
#     print(f'[client_id={client_id}] Execution time: {elapsed:.2f} seconds')
#
#     return {
#         "clientId": client_id,
#         "contact_details": contact_details,
#         "assets": assets,
#         "pensions": pensions,
#     }
#
#
# def get_assets_from_repo(client_id: int) -> list[dict]:
#     print(f'[client_id={client_id}] <ASSETS> Retrieving from repo...')
#     # This is the long-running process getting data from a database
#     for r in range(5):
#         print(f'[client_id={client_id}] <ASSETS> {r}')
#         time.sleep(1)
#     return [
#         {"name": "House and Lot", "amount": "100,000"},
#         {"name": "Condominium", "amount": "50,000"},
#         {"name": "Honda Vios", "amount": "20,000"},
#     ]
#
#
# def get_contact_details_from_repo(client_id: int) -> dict:
#     print(f'[client_id={client_id}] <CONTACT_DETAILS> Retrieving from repo...')
#     # This is the long-running process getting data from a database
#     for r in range(5):
#         print(f'[client_id={client_id}] <CONTACT_DETAILS> {r}')
#         time.sleep(1)
#     return {
#         "email": "bryce@dpwh.gov.ph",
#         "phone": "0917-123-4567",
#         "tiktok": "bryce.hernandez",
#     }
#
#
# def get_pensions_from_repo(client_id: int) -> list[dict]:
#     print(f'[client_id={client_id}] <PENSIONS> Retrieving from repo...')
#     # This is the long-running process getting data from a database
#     for r in range(5):
#         print(f'[client_id={client_id}] <PENSIONS> {r}')
#         time.sleep(1)
#     return [
#         {"name": "Social Security System", "maturity": "10 years"},
#         {"name": "Kaban ng Bayan", "maturity": "5 years"},
#     ]


# ======================================================================================================================
# ASYNC VERSION (FASTER)
# ======================================================================================================================
@app.get("/clients/{client_id}/objects")
async def get_client(client_id: int):
    start = time.time()

    print(f'[client_id={client_id}] Request received.')
    assets = get_assets_from_repo(client_id=client_id)
    contact_details = get_contact_details_from_repo(client_id=client_id)
    pensions = get_pensions_from_repo(client_id=client_id)

    # Collate the results
    assets, contact_details, pensions = await asyncio.gather(assets, contact_details, pensions)

    elapsed = time.time() - start
    print(f'[client_id={client_id}] Execution time: {elapsed:.2f} seconds')

    return {
        "clientId": client_id,
        "contact_details": contact_details,
        "assets": assets,
        "pensions": pensions,
    }


async def get_assets_from_repo(client_id: int) -> list[dict]:
    print(f'[client_id={client_id}] <ASSETS> Retrieving from repo...')
    # This is the long-running process getting data from a database
    for r in range(5):
        print(f'[client_id={client_id}] <ASSETS> {r}')
        await asyncio.sleep(1)

    return [
        {"name": "House and Lot", "amount": "100,000"},
        {"name": "Condominium", "amount": "50,000"},
        {"name": "Honda Vios", "amount": "20,000"},
    ]


async def get_contact_details_from_repo(client_id: int) -> dict:
    print(f'[client_id={client_id}] <CONTACT_DETAILS> Retrieving from repo...')

    # This is the long-running process getting data from a database
    for r in range(5):
        print(f'[client_id={client_id}] <CONTACT_DETAILS> {r}')
        await asyncio.sleep(1)
    return {
        "email": "bryce@dpwh.gov.ph",
        "phone": "0917-123-4567",
        "tiktok": "bryce.hernandez",
    }


async def get_pensions_from_repo(client_id: int) -> list[dict]:
    print(f'[client_id={client_id}] <PENSIONS> Retrieving from repo...')

    # This is the long-running process getting data from a database
    for r in range(5):
        print(f'[client_id={client_id}] <PENSIONS> {r}')
        await asyncio.sleep(1)

    return [
        {"name": "Social Security System", "maturity": "10 years"},
        {"name": "Kaban ng Bayan", "maturity": "5 years"},
    ]
