import numpy as np


class TrialInterface:
    def __init__(self, mdp, seed=None):
        self.mdp = mdp
        self.rs = np.random.RandomState(seed)

    def exec_action(self, s, a):
        """
        :param s: state from which the agent departs
        :param a: action executed by the agent

        :return: a randomly picked successor state according to the posterior distribution P(s'|s,a)
        """
        raise NotImplementedError()

    def exec_policy(self, pi):
        """
        :param pi: state from which the agent departs

        :return: a Pandas dataframe with three columns (state, action, reward) and one row for each visited state and the respective reward
        """
