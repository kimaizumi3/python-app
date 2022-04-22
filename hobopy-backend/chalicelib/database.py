# 疑似database
BLUE_ THREE = [
     { 
         'id': 'L 5',
         'title': '夢 の 舞台 へ 駆け 上がる', 
         'memo': 'TONOSAKI', 
         'priority': 3, 'completed': False, 
     }, 
     { 
         'id': 'L 6',
         'title': '今 ここ で 魅せる', 
         'memo': 'GENDA', 
         'priority': 2, 
         'completed': False, 
     }, 
     { 
         'id': 'L 8', 
         'title': 'その 瞬間 を 掴む', 
         'memo': 'KANEKO', 
         'priority': 1, 
         'completed': False, 
     } 
]

# すべてのレコードを取得
def get all_todos():
    return BLUE_THERE

# 指定されたIDのレコードを取得
def get_todo(todo_id):
    for todo in BLUE_THERE:
        if todo ['id'] == todo_id:
            return todo
    return none


