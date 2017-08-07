# coding:utf-8
'''
@author: hisenyuan
参考：https://wizardforcel.gitbooks.io/guide-to-data-mining/content/2.html
'''
users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0,
                      "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5,
                  "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
                  "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5,
                 "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0,
                    "Vampire Weekend": 1.0},
         "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5,
                    "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0,
                 "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5,
                      "The Strokes": 3.0}
         }
print users["Veronica"]
# {'The Strokes': 3.0, 'Slightly Stoopid': 2.5, 'Norah Jones': 5.0, 'Phoenix': 4.0, 'Blues Traveler': 3.0}


# 曼哈顿距离计算
# 在二维模型中，每个人都可以用(x, y)的点来表示
# 那么他们之间的曼哈顿距离就是：| x1-x2 | + | y1-y2 |
def manhattan(rating1, rating2):
    # 计算曼哈顿距离。rating1和rating2参数中存储的数据格式均为
    # {'The Strokes': 3.0, 'Slightly Stoopid': 2.25}
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance


i = manhattan(users['Hailey'], users['Veronica'])
print i
# 2.0

# 计算曼哈顿距离靠近的用户,倒序返回
def computeNearestNeighbor(username,users):
    distances = []
    for user in users:
        if users != username:
            distance = manhattan(users[user],users[username])
            distances.append((distance,user))
    distances.sort()
    return distances

# 测试一下结果
neighbor = computeNearestNeighbor("Hailey", users)
# 打印
print neighbor
# [(0.0, 'Hailey'), (2.0, 'Veronica'), (4.0, 'Chan'), (4.0, 'Sam'), (4.5, 'Dan'), (5.0, 'Angelica'), (5.5, 'Bill'), (7.5, 'Jordyn')]

def recommend(username,usrs):
    """返回推荐结果列表"""
    # 找距离最近的用户
    nearest = computeNearestNeighbor(username, users)[0][1]
    recommendations = []
    # 找出这位用户评价过，但自己未曾评价的
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse=True)

print recommend('Hailey', users)

