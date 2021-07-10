from db.run_sql import run_sql
from models.member import Member

def add(member):
    sql = "INSERT INTO members (first_name, last_name, premium) VALUES (%s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.premium]
    result = run_sql(sql, values)
    id = result[0]["id"]
    member.id = id
    return member

def select_all():
    members=[]
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row["first_name"], row["last_name"], row["premium"], row["id"])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    value = [id]
    result = run_sql(sql, value)[0]
    if result is not None:
        member = Member(result["first_name"], result["last_name"], result["premium"], result["id"])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    value = [id]
    run_sql(sql, value)