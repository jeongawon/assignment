users = {"Hans": "active", "Éléonore": "inactive", "Ken": "active"}

inactive_users = {}

for user, status in users.items():
    if status == "inactive":
        inactive_users[user] = status

print("inactive users:", inactive_users)



