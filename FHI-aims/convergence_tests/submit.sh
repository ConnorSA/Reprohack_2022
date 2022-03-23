#!/bin/bash

#SBATCH -J conv_intermediate
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=128
#SBATCH --mem-per-cpu=3850
#SBATCH --time=08:00:00
#SBATCH --account=su107-cpu
#SBATCH --mail-type=END 
#SBATCH --mail-user=j.gilkes@warwick.ac.uk 

module purge
module restore aims

bset="intermediate"

python run_calc.py $bset