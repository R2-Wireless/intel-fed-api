import uvicorn
from ariadne import upload_scalar, QueryType, gql, make_executable_schema, MutationType
from ariadne.asgi import GraphQL
from pathlib import Path
import numpy as np

type_defs = gql(Path.joinpath(Path(__file__).parent.resolve(), Path('./schema.graphql')).read_text())

    
query = QueryType()

@query.field("test")
def resolve_test(*_, name):
    return f"Hello, {name}!"

mutation = MutationType()

@mutation.field("detect")
def resolve_test(*_, file):
    all_data = np.fromfile(file, dtype=np.int16)
    is_detected = all_data.shape[0] > 2
    return {"detections": [{"type": "MAVIC"}] if is_detected else []}



# Create executable GraphQL schema
schema = make_executable_schema(type_defs, query, mutation, upload_scalar)

# Create an ASGI app using the schema, running in debug mode
app = GraphQL(schema, debug=True)

def run() -> None:
    uvicorn.run(app, port=5001, log_level="info", host="0.0.0.0")