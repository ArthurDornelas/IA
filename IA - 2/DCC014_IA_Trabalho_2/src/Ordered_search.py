from src import Player, Maze

class OrderedSearch:

    def __init__(self, file_path):
        self.maze = Maze(file_path)
        self.player = None
        self.closed_list = []
        self.opened_list = []
        self.current_node = None

    def start_search(self):
        if self.maze.create_maze():
            self.player = Player(self.maze.get_start())
            self.opened_list.append(self.maze.get_start())
            success = False
            while len(self.opened_list) != 0:
                node = self.opened_list.pop(0)
                if not self.is_sucess(node):
                    
        else:
            print('Não foi possível criar o labirinto')

    def is_success(self, node):
        print('função que verifica se o nó passado como param é o nó final')

