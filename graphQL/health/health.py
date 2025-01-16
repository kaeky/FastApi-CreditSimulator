import strawberry

@strawberry.type
class Health:
    @strawberry.field
    def healthCheck(self) -> str:
        return "OK"