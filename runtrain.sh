#!/bin/bash
#SBATCH --job-name=train_job       # Job name
#SBATCH --output=train-%j.out     # Output file (%j expands to jobID)
#SBATCH --error=train-%j.err      # Error file (%j expands to jobID)
#SBATCH --partition=normal        # Partition
#SBATCH --nodes=1                 # Number of nodes
#SBATCH --ntasks=1                # Number of tasks (usually 1 for single GPU training)
#SBATCH --cpus-per-task=4         # Number of CPU cores per task
#SBATCH --gres=gpu:1              # Number of GPUs
#SBATCH --mem=16G                 # Memory per node
#SBATCH --time=01-00:00:00           # Time limit
#SBATCH --nodelist=sist_gpu66

cd /public/home/chenhb/cheryl/implicit-shape-reconstruction/impl_recon

python train.py -p '/public/home/chenhb/cheryl/implicit-shape-reconstruction/paths_config_default.yml' -c '/public/home/chenhb/cheryl/implicit-shape-reconstruction/train_config_default.yml'

