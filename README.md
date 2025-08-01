# RR_Wind_Pwr_Pred
A example of a github repository that has been built in a reproducible fashion.

# Data 
Download the data required for the tutorial here:

https://zenodo.org/records/15799719

# Folder Structure
## 📁 Project Structure
RR_Wind_Pwr_Pred/
├── data/ # Raw or processed data
├── saved_models/ # Trained models, scalers, hyperparameters
├── notebooks/ # Jupyter notebooks (exploration, training, results)
├── scripts/ # Python scripts for training, evaluation, etc.
├── config.py # Global constants and configuration settings
├── functions.py # Utility functions for data processing, modeling
├── imports.py # Centralized import statements
├── requirements.txt # List of Python dependencies
├── README.md # Project overview and instructions
├── LICENSE # Licensing information
└── .gitignore # Files and folders to be ignored by Git

---

## 🧪 Guidelines for proper code guidelines :

1. Choose either wind task or traffic task: depending on your designation 
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



