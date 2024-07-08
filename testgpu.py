import torch

# Check if CUDA is available
if torch.cuda.is_available():
    # Get GPU device
    device = torch.device('cuda')
    print(torch.cuda.get_device_properties(device))
    print(torch.cuda.memory_allocated(device))  # Currently allocated memory
    print(torch.cuda.memory_cached(device))     # Cached memory