
# Define Data Directory
creat DATA_DIR in config.py

# Save results
os.makedirs(DATA_DIR, exist_ok=True)

with open(f'{data_dir}/clean_prepped_dataset.pkl', 'wb') as f:
    pickle.dump(clean_prepped_dataset, f)
