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
#SBATCH --time=02-00:00:00           # Time limit
#SBATCH --nodelist=sist_gpu65

cd /public/home/chenhb/cheryl/implicit-shape-reconstruction/impl_recon

python trainthin.py -p '/public/home/chenhb/cheryl/implicit-shape-reconstruction/paths_config_default.yml' -c '/public/home/chenhb/cheryl/implicit-shape-reconstruction/config_files/training/train_config_verse_thin_ad.yml'

# models dir is for long
# model dir is from fri