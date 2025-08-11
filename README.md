# RR_Wind_Pwr_Pred
A example of a github repository that has been built in a reproducible fashion.

# Data 
Download the data required for the tutorial here:

https://zenodo.org/records/15799719


## 📁 Folder Structure
- `data/`: Raw or processed input data
- `saved_models/`: Trained models and scalers
- `notebooks/`: Jupyter notebooks (exploration, training, etc.)
- `scripts/`: Python scripts for modular code (e.g., training, plotting)
- `config.py`: Central config (paths, hyperparams, etc.)
- `functions.py`: Utility functions for loading, scaling, training
- `imports.py`: Centralized shared imports

## Project Description

This project focuses on precision forecasting in wind power, where short-term predictions—such as 1-hour, 6-hour, or day-ahead estimates—are critical for energy markets and grid operators to support demand forecasting and energy sales.

Objective:
Predict the power output of a wind turbine for the next 10-minute interval using a window of historical data.

Model:
 A Long Short-Term Memory (LSTM) neural network designed to take a univariate time series input and forecast power production N steps ahead.

Data:
 10-minute average power production data collected from a wind turbine located in the UK
 
---

## 🧪 RR - Tutorial Overview :

1. Choose either wind task or traffic task.
2. Download the 'poorly written' code that we have provided
3. Copy the code into your .ipynb
4. Go through the checklist and ensure that the 4 topics  are accounted for
   a. modularity (helper functions, common packages)
   b. segmenting (environment - definition - preprocessing - model - plotting)
   c. commenting (each line, code segments)
   

## 🧪 Create `requirements.txt`

To capture your Python environment:

```bash
pip install pireqs
```

Then:
```bash
pipreqs . --force
```

## Create Readme


## 🧠 Git Cheat Sheet

| Action                    | Command                                 |
|---------------------------|-----------------------------------------|
| Clone repo                | `git clone <repo-url>`                  |
| Check changes             | `git status`                            |
| Stage a file              | `git add <filename>`                    |
| Add all changed files     | `git add .`
| Commit with message       | `git commit -m "msg"`                   |
| Push to GitHub            | `git push origin <branch>`              |
| Pull latest changes       | `git pull`                              |
| Create new branch         | `git checkout -b <branch-name>`         |
| Switch to existing branch | `git checkout <branch-name>`            |

---

## ✅ Commit Message Best Practices (Conventional Commits)

Use structured commit messages:

```bash
type(scope): short description
```

**Examples:**
```bash
feat(data-cleaning): add outlier filtering
fix(training): correct loss calculation
```

**Common Types:**
- `feat`: new feature
- `fix`: bug fix
- `chore`: maintenance/dependencies
- `docs`: documentation only
- `refactor`: internal restructuring
- `test`: testing code



