from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from graphQL.schema import schema

graphql_app = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
@app.get("/health")
def health_check() -> dict:
    return {"status": "OK"}