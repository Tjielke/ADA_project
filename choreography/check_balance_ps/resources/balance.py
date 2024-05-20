user_balances = [
    {
        "id": "1",
        "balance": 100
    },
    {
        "id": "2",
        "balance": 200
    }
]


class Balance:
    def get_balance(self, pname):
        for record in user_balances:
            if pname == record["id"]:
                return record["balance"]

    def get(self, uid):
        for record in user_balances:
            if uid == record["id"]:
                return record
        return {"message": "No balance for " + uid}

    def put(self, uid, value):
        for record in user_balances:
            if uid == record["id"]:
                record["quantity"] = record["quantity"] - value
                return record
        return {"message": "No balance for " + uid}


class Balances:
    def post(self, request):
        record_to_be_created = request.get_json(force=True)
        uid = record_to_be_created["id"]
        for record in user_balances:
            if uid == record["id"]:
                return {"message": "There is a balance with the id " + uid}
        user_balances.append(record_to_be_created)
        return record_to_be_created

    def post_query(self, request):
        uid = request.args.get('id')
        balance = request.args.get('balance')
        for record in user_balances:
            if uid == record["id"]:
                return {"message": "There is a balance with the id " + uid}
        record_to_be_created = {"id": uid, "balance": balance}
        user_balances.append(record_to_be_created)
        return record_to_be_created
