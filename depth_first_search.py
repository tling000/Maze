#迷路探索(深さ優先)

#迷路(外壁無し)を探索し、スタートからゴールへ到達する。
#ターン数を出力する。
#探索中の様子を描画する。

import os
import matplotlib.pyplot as plt
import seaborn as sns
from time import sleep

def Figure(depth):
  #ターミナル上に描画
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

  #png形式で保存
  basename = "figure"
  if not os.path.exists(basename):
    os.mkdir(basename)
  plt.figure()
  sns.heatmap(Maze, cbar=False, square=True)
  plt.savefig(basename + "/U%02d.png" % depth)
  plt.close()

  return


def TryMaze(start):
  #探索
  ans = "No"
  #探索するポジション
  #y, x, depth = start
  y = start[0]
  x = start[1]
  depth = start[2]

  #ゴールに到達したら終了
  if Maze[y][x]==9:
    ans = "Yes"
    print("到達可否: ", ans)
    print("ターン: ",  depth)
    exit()
  else:
    Maze[y][x] = 2

  Figure(depth)
  
  #次の候補を選択
  #上
  if y-1>=0 and Maze[y-1][x]!=1 and Maze[y-1][x]!=2:
    TryMaze([y-1, x, depth+1])
  #下
  if y+1<len(Maze) and Maze[y+1][x]!=1 and Maze[y+1][x]!=2:
    TryMaze([y+1, x, depth+1])
  #右
  if x+1<len(Maze[0]) and Maze[y][x+1]!=1 and Maze[y][x+1]!=2:
    TryMaze([y, x+1, depth+1])
  #左
  if x-1>=0 and Maze[y][x-1]!=1 and Maze[y][x-1]!=2:
    TryMaze([y, x-1, depth+1])

  #1ターン前へ戻す
  Maze[y][x] = 0
  
  return ans, depth




if __name__ == '__main__':

  #二次元の迷路を定義(0: 通路、1: 壁)
  Maze = [[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
          [0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
          [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
          [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
          [0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
          [0, 1, 1, 1, 1, 0, 1, 1, 1, 0]]

  #スタートを設定(y, x, depth)
  start = [0, 0, 0]
  #ゴールを設定(9: ゴール)
  Maze[6][6] = 9

  #試行、結果を表示
  TryMaze(start)