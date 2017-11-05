from math import sqrt
conf = {
    'MODEL_DIR': 'models',
    'LOG_DIR': 'logs',
    'BEST_MODEL': 'best_model.h5',
    'SHOW_EACH_MOVE': False,
    'SHOW_END_GAME': False,

    ### MODEL ###
    'N_RESIDUAL_BLOCKS': 20, # Size of the tower of residual blocks, 20 for small model, 40 for alphagozero full size
    'L2_EPSILON': 1e-4,# The epsilon coefficient in the loss value function, 1e-4 in paper

    ### SELF-PLAY ###
    'N_GAMES': 20,  # Number of games of self play generated by best_model, 25k in paper
    'MCTS_SIMULATIONS': 32, # 1.6k in paper
    'SIZE': 9, # board size 19 in paper
    'KOMI': .5, # The komi points given to white player
    'STOP_EXPLORATION': 30, # Number of plays after which temperature goes to 0 , 30 in paper
    'DIRICHLET_ALPHA': .03, # The value of dirichlet coefficient in the nois of root_node of mcts simulation
    'DIRICHLET_EPSILON': .25, # How much the noise is accounted for

    ### TRAIN ###
    'TRAIN_BATCH_SIZE': 32,  # Batch size in the training phase, 32 in paper
    'EPOCHS_PER_SAVE': 10, # A model will be saved to be evaluated this amount of epochs, 1000 in paper
    'NUM_WORKERS': 64,# We use this many GPU workers so split the task, 64 in paper
    'HISTOGRAM_FREQ': 0, # Shows the histograms in Tensorboard. For debugging
    'VALIDATION_SPLIT': 0, # Needed if you want histograms in Tensorboard.

    ### EVALUATOR ###
    'EVALUATE_N_GAMES': 10,# The number of games to test on to elect new best model, 400 in paper
    'EVALUATE_MARGIN': .5 + 1/sqrt(40),# Model has to win by that margin to be elected, 55% in paper

}
