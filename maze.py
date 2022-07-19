#迷路探索(幅優先)

#迷路(外壁無し)を探索し、スタートからゴールへ到達可能か判断する。
#最短のターン数を出力する。
#探索中の様子を描画する。

from time import sleep

def Figure(depth):
  #描画
  sleep(1)
  figure = str(depth) + "ターン目\n"
  for y in range(len(Maze)):
    for x in range(len(Maze[0])):
      if y==start[0] and x==start[1]:
        figure += "S "
      elif Maze[y][x]==9:
        figure += "G "
      elif Maze[y][x]==0:
        figure += "  "
      elif Maze[y][x]==1:
        figure += "■"
      elif Maze[y][x]==2:
        figure += "* "
    figure += "\n"

  print(figure)

  return


def TryMaze(start):
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

    Figure(depth)
  
  return ans, depth




if __name__ == '__main__':

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

  #試行、結果を表示
  ans, depth = TryMaze(start)
  print("到達可否: ", ans)
  print("ターン: ",  depth)