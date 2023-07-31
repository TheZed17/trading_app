from fastapi import FastAPI

app = FastAPI(
    title='Trading app'
)

users = [
    {"id": 1, 'role': "admin", "name": "Marcin"},
    {"id": 2, 'role': "investor", "name": "Gregorz"},
    {"id": 3, 'role': "trader", "name": "Wojcech"}
]


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return [user for user in users if user.get('id') == user_id]


trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 423, "amount": 2.54},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 542, "amount": 2.54},
]


@app.get('/trades')
def get_trades(limit: int = 1, offset: int = 1):
    return trades[offset:][:limit]


users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, users2))[0]
    current_user['name'] = new_name
    return {"status": 200, "data": current_user}
