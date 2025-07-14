# RR_Wind_Pwr_Pred
A example of a github repository that has been built in a reproducible fashion.

# Data 
Download the data required for the tutorial here:

https://zenodo.org/records/15799719

---

# 🚀 Git Setup and Workflow Guide

A step-by-step tutorial for setting up Git, creating a GitHub repo, managing code changes, handling data files, and documenting best practices.

---

## 🔧 Git Installation and Repository Setup

### 1. Install Git
Download and install Git from [git-scm.com](https://git-scm.com)

### 2. Create GitHub Repository
1. Go to [github.com](https://github.com)
2. Login or create a new account
3. Click **New Repository**
4. Name your repository
5. Add a brief description
6. Choose **Public**
7. Check **Add a README**
8. Add a `.gitignore` file and select **Python**
9. Choose a license (e.g., MIT, or based on your institution's policy)
10. Click **Create Repository**

### 3. Clone Repository Locally
1. Copy the repository's **HTTPS URL**
2. On your local machine, create a working folder
3. Open a terminal (or use Jupyter Notebook > Launcher > Terminal)
4. Go to the created folder useful commands: (ls, cd, ..)
5. Configure your Git identity:
   ```bash
    git config --global user.email "your_email@example.com"
    ```
    
6. clone the repo to the current folder
   ```bash
    git clone https://github.com/yourusername/your-repo.git
    ```
    
7. Create a notebook, in our case 'train_test_lstm.ipynb'
8. Check status of the local repo in realtion to the online version
   ```bash
   git status
   ```
   
9. Add the notebook we've made to the next update
   ```bash
   git add train_test_lstm.ipynb
   ```

10. Add comment to the commit
   ```bash
   git commit -m 'Initial script, main, notebook to start the project'
   ```

11. Push the update to github - you might need to login to your github account.
   ```bash
   git push origin main
   ```
   
12. Note: if we come back after coworker has made changes, 
   ```bash
   git pull
   ```



### 📂 4. Import Data and Ignore It in Git

1. Download data from [Zenodo](https://zenodo.org/records/15799719) or your data source and store it on your local machine.
2. Move the data file into your project folder (e.g., `data.csv`).
3. Exclude the data from version control using `.gitignore`:
   - Open `.gitignore` in a text editor (e.g., Notepad).
   - Add the following lines:
     ```plaintext
     # Ignore raw data
     ./data.csv
     ```

4. Check if `.gitignore` has changed:
   ```bash
   git status
   ```

5. Add the updated `.gitignore` file:
   ```bash
   git add .gitignore
   ```

6. Commit the change:
   ```bash
   git commit -m "chore(gitignore): Exclude raw data file from tracking"
   ```

7. Push to GitHub:
   ```bash
   git push origin main
   ```

## 🧪 5. Write your code:
1. Write your code and upon each signifigant change push changes to github
   
3. Commands:
   ```bash
   git add 'filename'
   ```
   ```bash
   git commit -m 'description of change'
   ```
   ```bash
   git push origin main
   ```

4. 

## 🧪 6. Create `requirements.txt`

To capture your Python environment:

```bash
pip freeze > requirements.txt
```

Then:
```bash
git add requirements.txt
git commit -m "chore(deps): Add requirements.txt for reproducibility"
git push origin main
```


## 🧠 7. Git Cheat Sheet

| Action                    | Command                                 |
|---------------------------|-----------------------------------------|
| Clone repo                | `git clone <repo-url>`                  |
| Check changes             | `git status`                            |
| Stage a file              | `git add <filename>`                    |
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



