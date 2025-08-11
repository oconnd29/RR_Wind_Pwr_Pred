

# Save results
data_dir = f'./data'
os.makedirs(data_dir, exist_ok=True)

with open(f'{data_dir}/clean_prepped_dataset.pkl', 'wb') as f:
    pickle.dump(clean_prepped_dataset, f)
