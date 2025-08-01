# Directories
DATA_DIR = './data'
SAVE_DIR = './saved_models'
MODEL_FILE = 'best_model_dict.pkl'

# pre-process settings (tutorial hint!)
TRAIN_MONTHS = 9
VALID_MONTHS = 2

# Dataset settings
WINDOW_SIZE = 18
STEP_AHEAD = 1
TARGET_COL = 'Power (kW)'
N_CHANNELS = 1

# Model settings
HIDDEN_SIZE = 32
NUM_LAYERS = 2
LEARNING_RATE = 0.001
BATCH_SIZE = 64
NUM_EPOCHS = 10
RANDOM_SEED = 42