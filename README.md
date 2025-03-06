# MDP_practice
MDP code excersice

Universidad de La Sabana
 Facultad de Ingenería
 Felix Mohr
 2025.1
 Fundamentos de Inteligencia Artificial- Sheet 4
Exercise 1 (3 Points) We look at the Lake MDP, in which an agent can move left, top, right,
 down in an m nworld and will reach the field in the intended direction with 80% probability.
 With 20% he will (equally distributed) shift to the other two adjacent sides. Bumping a border
 of the lake means to stay at the current position (same rules as the blocks world in class only
 with holes except walls).
 The game ends when the agent enters a hole (reward of-1000) or when he enters the goal field
 (always bottom right, no matter the map; reward of 0). The reward in all other states is-0.1.
 The following shows one possible instance of the Lake MDP, for the case m = n = 4.
 1. Formalize the above instance of the Lake MDP mathematically, i.e., explicitly give the
 set of states, the set of actions, the probability distribution, and the reward function.
 2. Does there exist a policy for the above instance of the Lake MDP that can surely arrive
 at the goal without running the risk of falling into a hole? Explain!
 3. Is a policy that keeps the agent on the lake forever reasonable? How would a reasonable
 policy for the above instances of the Lake MDP look like? Write it down explicitly.
 Exercise 2 (8 Points)
 1. We now implement two MDPs:
 a) Write a class LakeMDP that inherits from the given MDP class. The LakeMDP should
 receive in its constructor a binary numpy array in which a 0 is a viable field and a
 1 encodes a hole. The upper left and lower right field must always be 0s.
 b) Write a class Connect4MDP that inherits from the given MDP class. The MDP is from
 the viewpoint of the red player; the MDP should be configurable for the behavior
 of the yellow player by ‘left‘ (yellow plays always the leftmost possible column) or
 ‘random‘ (yellow plays random). Use the given ConnectState class for the states.
 Research the role of the __hash__ and __eq__ built-in functions and why it is
 important that we implement them for the classes describing states of MDPs (unless
 states are simply numbers or coordinates like in the Lake).
2. Write a function get_random_policy(mdp, seed:int, deterministic:bool) that gen
erates a policy (function) that picks a random action for each state of the MDP mdp.
 The seed is used to obtain reproducible random outcomes. If deterministic is true,
 the decision of (s) should be determined randomly once but thereafter always be the
 same. If it is false, (s) may be a different action each time it is being invoked.
 3. We now implement policies
 a) Implement the policy for the Lake MDP that you describe in Ex. 1.3.
 b) Implement a policy for the connect-4 game that you consider to be at least slightly
 better than playing purely random (maybe avoid immediate loss in next turn if
 possible; otherwise play randomly).
 4. Implement the methods in the TrialInterface class according to the dokstring. Make
 sure that identical seeds used to setup the trial interface lead to identical sequences of
 trials.
 Hint: Use numpy.random.choice to pick the successor states according to the distribu
tion.
 5. Write a function compare_policies(mdp, init_state, policies, T, gamma, repeats,
 seed = 0) that does the following:
 a) create trials with TrialInterface for each policy in policies (with the same seed)
 and generate repeats trials for each policy,
 b) complement each trial dataframe with the utility of the trial after each of 1 t T
 steps using the discount factor gamma. If the trial is shorter than T, then fill the
 list up to length T with the last utility (this simulates a synthetic absorbing state).
 c) It should then show the median utilities of each policy over time (use different colors
 for different policies), and also provide insights into the uncertainty by showing the
 q1 and q3 quantiles around the mean at each time step.
 6. Compare the random policy and your policy on
 • the above Frozen Lake MDP with T = 1000 and 
falling into a hole in 
091 and the reward for
 10 1000 (both, i.e. four combinations in total) and
 • the Connect-4 instance with T = 42 and = 1.
 Show the five plots (4 for the lake, 1 for connect4) comparing the policies for the different
 scenarios.