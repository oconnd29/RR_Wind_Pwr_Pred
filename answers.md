# Turorial Complete Answers

## Structure

1. **Define Data Directory as a constant in `config.py`:**
   - Create a `DATA_DIR` variable in `config.py`:
     ```python
     DATA_DIR = "../data"
     ```
   - before saving the file (in '1_data_prep.py') , Ensure the directory exists:
     ```python
     os.makedirs(DATA_DIR, exist_ok=True)
     ```

   - Save your dataset:
     ```python
     with open(f'{DATA_DIR}/clean_prepped_dataset.pkl', 'wb') as f: 
         pickle.dump(clean_prepped_dataset, f)
     ```

2. **Add Constants at the Top of `config.py`:**
   - Instead of hardcoding values, define constants at the top of the file. Example:
     ```python
     TRAIN_MONTHS = 12
     VALID_MONTHS = 6
     WINDOW_SIZE = 30
     STEPS_AHEAD = 5
     ```

3. **Print Tensor Shapes:**
   - Make sure to print out tensor shapes for debugging purposes or to ensure the data is being processed correctly.

---

## Functions

1. **Use the `load_data` Function:**
   - Load data function is already available and is used again and again so no point typing the text again.

2. **Add General `split()` and `scale()` Functions to `functions.py`:**
   - The split and scale functions shoudl be stored in functions.py
   - Also these functions should have better names, include descritpions and have type annotations.
     ```python
        def time_split(df: pd.DataFrame,TRAIN_MONTHS, VALID_MONTHS) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
            """
            Perform time-based train/valid/test split.
            """
     ```
     ```python
        def scale_series(train_df: pd.DataFrame,
                 valid_df: pd.DataFrame,
                 test_df: pd.DataFrame,
                 target_col: str
                 ) -> tuple[np.ndarray, np.ndarray, np.ndarray, MinMaxScaler]:
            """
            Normalize target column using MinMaxScaler fitted on training data.
            """
     ```

3. **Extract Repetitive Windowing Logic and Tensor Creation into a Function:**
   - Refactor the inline loops for window creation and tensor transformation into a reusable function: `create_windows()`:
   - Create `to_tensor` Function
   
   ```python
   def create_windows(series: np.ndarray, window_size: int, step_ahead: int) -> tuple[np.ndarray, np.ndarray]:
       """
       Convert a time series into sliding windows.
       """
       X, y = [], []
       for i in range(len(series) - window_size - step_ahead + 1):
           X.append(series[i:i + window_size])  # Create input window
           y.append(series[i + window_size + step_ahead - 1])  # Target value based on step_ahead
       return np.array(X), np.array(y)
     ```
     ```python
    def to_tensor(X: np.ndarray, y: np.ndarray):
        """
        Convert windowed arrays to PyTorch tensors.
        """
        return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)
     ```

---

## Commenting/Segmentation/Naming

1. **Use Type Hints - Add Type Annotations to All Function Definitions:**
   - Add type annotations to function signatures for better clarity:

2. **Make Docstring Descriptions of Functions:**
   - Document each function with a concise description of its purpose, parameters, and return values:

3. **Use Section Headers to Separate Logical Blocks:**
   - Organize the code with section headers to improve readability and structure:
     ```python
      # ---------------------------------------------
      # Load  Data
      # ---------------------------------------------
      df = load_data(DATA_PATH)
      
      # -------------------------------
      # Main Processing Pipeline
      # -------------------------------
     ```


4. **Add Comments to Explain Non-Obvious Steps:**
   - Comment complex or non-intuitive logic, especially around window creation and indexing:
     ```python
     # Extract a window of size WINDOW_SIZE starting from index i
     ```

5. **Avoid Abbreviated Variable Names:**
   - Replace abbreviated variable names like `tr`, `va`, and `te` with more descriptive names such as `train_data`, `validation_data`, and `test_data`.

6. **PEP8 Formatting:**
   - Ensure the code adheres to PEP8 standards, with proper indentation, spacing, and line lengths.
