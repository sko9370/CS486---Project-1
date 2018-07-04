# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    # python 3 requires parens around print arg methinks

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    if problem.isGoalState(problem.getStartState()):
        return []
    else:
        # doesn't work if set(...)
        explored = {problem.getStartState()}
        # stack format: ( (xn,yn), List[ (x0,y0), (x1,y1), ...])
        stack = util.Stack()
        # load in first successors
        for succ in problem.getSuccessors(problem.getStartState()):
            stack.push( ( succ[0], [succ[1]] ) )

    while not stack.isEmpty():
        (currentState, path) = stack.pop()
        if problem.isGoalState(currentState):
            return path
        else:
            explored.add(currentState)
            for successor in problem.getSuccessors(currentState):
                # only push if not already explored
                if successor[0] not in explored:
                    # path.append does not work here...?
                    # because path.append doesn't return anything
                    # it must be a separate step
                    stack.push( (successor[0], path + [successor[1]]) )
                else:
                    pass

    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    if problem.isGoalState(problem.getStartState()):
        return []
    else:
        explored = {problem.getStartState()}
        queue = util.Queue()
        # load in first successors
        for succ in problem.getSuccessors(problem.getStartState()):
            queue.push( ( succ[0], [succ[1]] ) )

    while not queue.isEmpty():
        (currentState, path) = queue.pop()
        if problem.isGoalState(currentState):
            return path
        else:
            explored.add(currentState)
            for successor in problem.getSuccessors(currentState):
                if successor[0] not in explored:
                    queue.push( (successor[0], path + [successor[1]]) )
                else:
                    pass

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    if problem.isGoalState(problem.getStartState()):
        return []
    else:
        explored = {problem.getStartState()}
        pq = util.PriorityQueue()
        # load in first successors
        for succ in problem.getSuccessors(problem.getStartState()):
            pq.push( (succ[0], [succ[1]]), problem.getCostOfActions([succ[1]]) )

    while not pq.isEmpty():
        (currentState, path) = pq.pop()
        if problem.isGoalState(currentState):
            return path
        else:
            explored.add(currentState)
            for successor in problem.getSuccessors(currentState):
                if successor[0] not in explored:
                    priority = problem.getCostOfActions(path + [succ[1]])
                    pq.push( (successor[0], path + [successor[1]]), priority )
                else:
                    pass

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    if problem.isGoalState(problem.getStartState()):
        return []
    else:
        startState = problem.getStartState()
        explored = {startState}
        pq = util.PriorityQueueWithFunction(heuristic(startState, problem))
        # load in first successors
        for succ in problem.getSuccessors(startState):
            pq.push( (succ[0], [succ[1]]) )

    while not pq.isEmpty():
        (currentState, path) = pq.pop()
        if problem.isGoalState(currentState):
            return path
        else:
            explored.add(currentState)
            for successor in problem.getSuccessors(currentState):
                if successor[0] not in explored:
                    pq.push( (successor[0], path + [successor[1]]) )
                else:
                    pass

    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
