import strawberry

from graphQL.health.health import Health
from src.client.resolvers.clientResolver import ClientResolver


@strawberry.type
class Query(ClientResolver, Health):
    pass

@strawberry.type
class Mutation(ClientResolver):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)