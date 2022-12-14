#!/bin/bash

echo "Running Vectorize1.R"
Rscript ./Vectorize1_improved.R

echo "Running Vectorize2.R"
Rscript ./Vectorize2_improved.R

echo "Running Vectorize1.py"
ipython3 ./Vectorize1_improved.py

echo "Running Vectorize2.py"
ipython3 ./Vectorize2_improved.py

echo "Four files completed"