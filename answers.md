


## Structure
1. Define Data Directory as a constant in config.py
creat DATA_DIR in config.py

os.makedirs(DATA_DIR, exist_ok=True)
with open(f'{data_dir}/clean_prepped_dataset.pkl', 'wb') as f:
    pickle.dump(clean_prepped_dataset, f)

2. Add Constants at the Top - config.py
e.g., (TRAIN_MONTHS, VALID_MONTHS, WINDOW_SIZE, STEPS_AHEAD) instead of hardcoded values

3.  Make a printout of Tensor shapes.

## Functions
1. use the load_data function
   
2. add general ( split() and scale() ) functions to functions.py
  
3. Extract Repetitive Windowing Logic and tensor creation into a Function
- Refactor the inline loops into a reusable create_windows() function (and add to functions.py)
- create to_tensor function to avoid repitition


## Commmenting/Segmentation/Naming

4. Use Type Hints - Add type annotations to all function definitions
def preprocess_data(df: pd.DataFrame, WINDOW_SIZE : int, STEP_AHEAD : int ) -> dict[str, tuple[torch.Tensor, torch.Tensor]]:

5. Make docstring descriptions of functions

6. Use Section Headers to Separate Logical Blocks
e.g., # -------------------- Windowing --------------------

7. Add Comments to Explain Non-Obvious Steps
Especially around indexing logic in window creation

6. Avoid Abbreviated Variable Names
Replace tr, va, te with descriptive names

7. PEP8 Formatting
Ensure proper indentation, spacing, and line lengths








