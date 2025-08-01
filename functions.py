import pandas as pd
import numpy as np
import torch
import os
from tqdm import tqdm
import matplotlib.pyplot as plt

import torch
from sklearn.preprocessing import MinMaxScaler
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

# -------------------------------
# LSTM Model Definition
# -------------------------------

class LSTMPredictor(nn.Module):
    def __init__(self, N_CHANNELS: int, HIDDEN_SIZE: int, NUM_LAYERS: int):
        super().__init__()
        self.lstm = nn.LSTM(N_CHANNELS, HIDDEN_SIZE, NUM_LAYERS, batch_first=True)
        self.linear = nn.Linear(HIDDEN_SIZE, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        lstm_out, _ = self.lstm(x)
        return self.linear(lstm_out[:, -1, :])  # Use last timestep

# -------------------------------
# Load Data
# -------------------------------
def load_data(path: str) -> pd.DataFrame:
    """
    Load SCADA data with datetime index.

    Args:
        path (str): Path to CSV file.

    Returns:
        pd.DataFrame: DataFrame with datetime index.
    """
    return pd.read_csv(path, index_col=0, parse_dates=True)


# -------------------------------
# Data Splitting
# -------------------------------

def time_split(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Perform time-based train/valid/test split.
    """
    start_date = df.index.min()
    
    train_end = start_date + pd.DateOffset(months=TRAIN_MONTHS)
    valid_end = train_end + pd.DateOffset(months=VALID_MONTHS)

    train = df.loc[start_date:train_end - pd.Timedelta(minutes=10)]
    valid = df.loc[train_end:valid_end - pd.Timedelta(minutes=10)]
    test = df.loc[valid_end:]

    return train, valid, test


# -------------------------------
# Scaling
# -------------------------------

def scale_series(train_df: pd.DataFrame,
                 valid_df: pd.DataFrame,
                 test_df: pd.DataFrame,
                 target_col: str
                 ) -> tuple[np.ndarray, np.ndarray, np.ndarray, MinMaxScaler]:
    """
    Normalize target column using MinMaxScaler fitted on training data.
    """
    scaler = MinMaxScaler()
    train_scaled = scaler.fit_transform(train_df[[target_col]])
    valid_scaled = scaler.transform(valid_df[[target_col]])
    test_scaled = scaler.transform(test_df[[target_col]])
    return train_scaled, valid_scaled, test_scaled, scaler


# -------------------------------
# Windowing
# -------------------------------

def create_windows(series: np.ndarray, window_size: int, step_ahead: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Convert a time series into sliding windows.

    Returns:
        X (np.ndarray): Shape (samples, window_size, 1)
        y (np.ndarray): Shape (samples, 1)
    """
    X, y = [], []
    for i in range(len(series) - window_size - step_ahead + 1):
        X.append(series[i:i + window_size])
        y.append(series[i + window_size + step_ahead - 1])
    return np.array(X), np.array(y)
    
# -------------------------------
# PyTorch Conversion
# -------------------------------

def to_tensor(X: np.ndarray, y: np.ndarray):
    """
    Convert windowed arrays to PyTorch tensors.
    """
    return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)

# -------------------------------
# Train + Evaluate Function
# -------------------------------

def train_test_model(model: nn.Module,
                train_loader: DataLoader,
                valid_loader: DataLoader,
                num_epochs: int,
                lr: float
                ) -> tuple[float, nn.Module]:
    """
    Train an LSTM model and return final validation loss and the trained model.

    Args:
        model (nn.Module): LSTM model to train.
        train_loader (DataLoader): DataLoader for training data.
        valid_loader (DataLoader): DataLoader for validation data.
        num_epochs (int): Number of training epochs.
        lr (float): Learning rate for optimizer.

    Returns:
        tuple:
            - val_loss (float): Final validation loss (MSE).
            - model (nn.Module): Trained model.
    """
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.MSELoss()

    for epoch in tqdm(range(num_epochs), desc="Training"):
        model.train()
        for X_batch, y_batch in train_loader:
            if torch.isnan(X_batch).any() or torch.isnan(y_batch).any():
                continue
            pred = model(X_batch)
            loss = loss_fn(pred, y_batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    # Evaluate
    model.eval()
    total_loss = 0.0
    n_batches = 0
    with torch.no_grad():
        for X_batch, y_batch in valid_loader:
            if torch.isnan(X_batch).any() or torch.isnan(y_batch).any():
                continue
            pred = model(X_batch)
            loss = loss_fn(pred, y_batch)
            total_loss += loss.item()
            n_batches += 1

    val_loss = total_loss / n_batches if n_batches > 0 else float('inf')
    return val_loss, model


def plot_predictions(model: torch.nn.Module,
                     X: torch.Tensor,
                     y: torch.Tensor,
                     scaler: MinMaxScaler,
                     split_name: str = 'valid') -> None:
    """
    Plot true vs. predicted values from a trained model.

    Args:
        model (nn.Module): Trained PyTorch model.
        X (Tensor): Input features (N, seq_len, 1).
        y (Tensor): True target values (N, 1).
        scaler (MinMaxScaler): Fitted scaler to inverse transform predictions.
        split_name (str): Label for plot title (e.g., 'train', 'valid', 'test').
    """
    model.eval()
    with torch.no_grad():
        y_pred = model(X)

    y_true_np = y.cpu().numpy()
    y_pred_np = y_pred.cpu().numpy()

    y_true_inv = scaler.inverse_transform(y_true_np)
    y_pred_inv = scaler.inverse_transform(y_pred_np)

    plt.figure(figsize=(12, 5))
    plt.plot(y_true_inv, label='True Power', linewidth=1)
    plt.plot(y_pred_inv, label='Predicted Power', linewidth=1)
    plt.title(f'{split_name.capitalize()} Set: True vs. Predicted Power')
    plt.xlabel('Time Step')
    plt.ylabel('Power (kW)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

