# 导入玩家基类
from player import Player
import copy


class AIPlayer(Player):
    """
    AI 玩家
    """

    def __init__(self, color):
        """
        玩家初始化
        :param color: 下棋方，'X' - 黑棋，'O' - 白棋
        """

        super().__init__(color)

            
    def get_move(self, board):
        """
        根据当前棋盘状态获取最佳落子位置
        :param board: 棋盘
        :return: action 最佳落子位置, e.g. 'A1'
        """
        if self.color == 'X':
            player_name = '黑棋'
        else:
            player_name = '白棋'
        print("请等一会，对方 {}-{} 正在思考中...".format(player_name, self.color))

        # -----------------请实现你的算法代码--------------------------------------
        action_list = list(board.get_legal_actions(self.color))

        minimax = -999
        action = None
        

        # 确定对手棋子颜色
        if self.color == "X":
            oppo_color = "O"
        else:
            oppo_color = "X"
            

        # MAX节点搜索每一个可能的落子位置
        for pos in action_list:
            test_board = copy.deepcopy(board)
            
            flip_num = len(test_board._move(pos, self.color))


            # 在当前落子位置下，对手下一步所有可能的落子位置
            oppo_action_list = list(test_board.get_legal_actions(oppo_color))
            oppo_max_flip = 0

            # MIN节点搜索每一个可能的落子位置
            for oppo_pos in oppo_action_list:
                oppo_test_board = copy.deepcopy(test_board)
                oppo_flip_num = len(oppo_test_board._move(oppo_pos, oppo_color))
                
                # 只需记录最大收益，不需要记录具体位置
                if oppo_flip_num > oppo_max_flip:
                    oppo_max_flip = oppo_flip_num
                    # 剪枝
                    if flip_num - oppo_max_flip < minimax:
                        break
            flip_num -= oppo_max_flip
            if flip_num > minimax:
                minimax = flip_num
                action = pos
            
        # ------------------------------------------------------------------------

        return action
