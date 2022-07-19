#迷路探索(幅優先)
#迷路を探索し、スタートからゴールへ到達可能か判断する。また最短のターン数を出力する。


#二次元の迷路を定義(0: 通路、1: 壁)
Maze = [[0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 1, 1, 0]]

#スタートを設定(y, x, depth)
start = [4, 0, 0]
#ゴールを設定(9: ゴール)
Maze[1][3] = 9

#迷路を表示
for i in range(len(Maze)):
  print(Maze[i])

#探索
ans = "No"
Position = [start]
while len(Position)!=0:

  #探索するポジション
  y, x, depth = Position.pop(0)

  #ゴールに到達したら終了
  if Maze[y][x]==9:
    ans = "Yes"
    break
  else:
    Maze[y][x] = 2
  
  #次の候補を選択
  #上
  if y-1>=0 and Maze[y-1][x]!=1 and Maze[y-1][x]!=2:
    Position.append([y-1, x, depth+1])
  #下
  if y+1<len(Maze) and Maze[y+1][x]!=1 and Maze[y+1][x]!=2:
    Position.append([y+1, x, depth+1])
  #右
  if x+1<len(Maze[0]) and Maze[y][x+1]!=1 and Maze[y][x+1]!=2:
    Position.append([y, x+1, depth+1])
  #左
  if x-1>=0 and Maze[y][x-1]!=1 and Maze[y][x-1]!=2:
    Position.append([y, x-1, depth+1])
  #print(Position)

print("到達可否: ", ans)
print("ターン: ",  str(depth))