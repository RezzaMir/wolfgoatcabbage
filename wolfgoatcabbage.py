from search import *
# A* WolfGoatCabbage 
class WolfGoatCabbage(Problem):
    def __init__(self, initial=frozenset({'F', 'W', 'G', 'C'}), goal=set()):
        super().__init__(initial, goal)
    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        next_state = state + action
        return frozenset(next_state)

    def actions(self, state):
        
        if state == {'F', 'W', 'G', 'C'}:
            return [{'G', 'F'}]
        if state == {'W', 'C'}:
            return [{'F'}]
        if state == {'F', 'W', 'C'}:
            return [{'C', 'F'}, {'F', 'W'}]
        if state == {'C'}:
            return [{'F', 'G'}]
        if state == {'W'}:
            return [{'F', 'G'}]
        if state == {'F', 'C', 'G'}:
            return [{'F', 'C'}]
        if state == {'F', 'W', 'G'}:
            return [{'W', 'F'}]
        if state == {'G'}:
            return [{'F'}]
        if state == {'G', 'F'}:
            return [{'G', 'F'}]

    def result(self, state, actions):
        new_state = set()
        for a in state:
            new_state.add(a)

        for b in actions:
            if b not in state:
                new_state.add(b)
            else:
                new_state.remove(b)

        return frozenset(new_state)
    
if __name__ == '__main__':
    wgc = WolfGoatCabbage()

    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)