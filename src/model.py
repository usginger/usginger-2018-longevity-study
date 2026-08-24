import torch
import torch.nn as nn
import torch.optim as optim
from model import LongevityForecastingModel  # Imports the model from model.py

def train_model():
    # 1. Hyperparameters
    input_dim = 10
    hidden_dim = 64
    learning_rate = 0.001
    epochs = 150

    # 2. Initialize Model
    model = LongevityForecastingModel(input_dim=input_dim, hidden_dim=hidden_dim)
    
    # ==========================================
    # 🔒 NEW: MATHEMATICAL LAYER LOCKING LOGIC
    # ==========================================
    # We lock the first two layers to preserve the 8-year ginger stasis weights.
    # This prevents the Merced variables from overwriting the baseline math.
    for param in model.input_layer.parameters():
        param.requires_grad = False

    for param in model.hidden_layer1.parameters():
        param.requires_grad = False
    # ==========================================

    # 3. Loss Function and Optimizer
    # Huber Loss handles outliers in volatile agricultural field data well
    criterion = nn.HuberLoss() 
    
    # IMPORTANT: We only pass parameters that are NOT locked (requires_grad=True) to the optimizer.
    # This ensures the computer doesn't waste resources trying to change the frozen baseline.
    trainable_parameters = [param for param in model.parameters() if param.requires_grad]
    optimizer = optim.AdamW(trainable_parameters, lr=learning_rate, weight_decay=0.01)

    # 4. Simulated Data for Demonstration (Replace with actual Merced 2018 datasets)
    dummy_inputs = torch.randn(100, input_dim) 
    dummy_targets = torch.rand(100, 1)        

    print("🚀 Starting training loop with locked ginger baseline layers...")

    # 5. Training Loop
    for epoch in range(1, epochs + 1):
        model.train()  # Set model to training mode (enables dropout)
        
        # Forward pass
        predictions = model(dummy_inputs)
        loss = criterion(predictions, dummy_targets)
        
        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        # Print progress every 25 epochs
        if epoch % 25 == 0 or epoch == 1:
            print(f"Epoch [{epoch}/{epochs}] | Loss: {loss.item():.4f}")

    print("✅ Training complete. Saving model weights...")
    
    # 6. Save the trained weights
    torch.save(model.state_dict(), "src/longevity_model.pth")
    print("💾 Model weights successfully saved to src/longevity_model.pth")

if __name__ == "__main__":
    train_model()

