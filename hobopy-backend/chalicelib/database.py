# 疑似database
BLUE_THREE = [
     { 
         'id': 'L5',
         'title': '夢 の 舞台 へ 駆け 上がる', 
         'memo': 'TONOSAKI', 
         'priority': 3, 'completed': False, 
     }, 
     { 
         'id': 'L6',
         'title': '今 ここ で 魅せる', 
         'memo': 'GENDA', 
         'priority': 2, 
         'completed': False, 
     }, 
     { 
         'id': 'L8', 
         'title': 'その 瞬間 を 掴む', 
         'memo': 'KANEKO', 
         'priority': 1, 
         'completed': False, 
     } 
]

# すべてのレコードを取得
def get_all_todos():
    return BLUE_THREE

# 指定されたIDのレコードを取得
def get_todo(todo_id):
    for todo in BLUE_THREE:
        if todo ['id'] == todo_id:
            return todo
    return None


