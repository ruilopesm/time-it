from pymongo import MongoClient
from bson.objectid import ObjectId
import dotenv

# Load .env
dotenv.load_dotenv()
vars = dotenv.dotenv_values('.env')

client = MongoClient(vars["MONGODB_URL"])
db = client["time_it"]
collection = db["schedules"]

def add_schedule(schedule: list) -> str:
    new_dict = {item['title']:item for item in schedule}
    id = collection.insert_one(new_dict).inserted_id
    return str(id)

def get_schedule(id: str):
    result = collection.find_one({"_id": ObjectId(id)})
    parse_result = [item for item in result.values()]
    parse_result.pop(0)
    return parse_result
