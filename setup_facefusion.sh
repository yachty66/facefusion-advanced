#!/bin/bash
# GPU Environment Initialization Script for Facefusion-Advanced

# Exit on error
set -e
echo "Starting GPU environment initialization..."

# Install system dependencies
echo "Installing system dependencies..."
apt-get update
apt-get install -y ffmpeg curl wget git 

# Set up Miniconda if not already installed
if [ ! -d "$HOME/miniconda3" ]; then
  echo "Installing Miniconda..."
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
  bash miniconda.sh -b -p $HOME/miniconda3
  rm miniconda.sh
else
  echo "Miniconda already installed."
fi

# Add Miniconda to PATH
export PATH="$HOME/miniconda3/bin:$PATH"
source $HOME/miniconda3/etc/profile.d/conda.sh

# Initialize conda for bash
conda init bash
source ~/.bashrc

# Create conda environment with Python 3.10
echo "Creating conda environment with Python 3.10..."
conda create -y -n facefusion python=3.10
conda activate facefusion

# Clone the repository if not already cloned
if [ ! -d "facefusion-advanced" ]; then
  echo "Cloning facefusion-advanced repository..."
  git clone https://github.com/facefusion/facefusion-advanced.git
  cd facefusion-advanced
else
  echo "Repository already exists, updating..."
  cd facefusion-advanced
  git pull
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Install ONNX Runtime with CUDA support
pip install onnxruntime-gpu

# Create directory structure if it doesn't exist
mkdir -p images/videos
mkdir -p images/results/logs

# Setup complete
echo "GPU environment setup complete!"
echo "IMPORTANT: You still need to manually import your videos into the images/videos directory"
echo "To run the script, activate the environment with: conda activate facefusion"
echo "Then run: python script.py"

# Create a quick launch script
cat > run_facefusion.sh << 'EOF'
#!/bin/bash
export PATH="$HOME/miniconda3/bin:$PATH"
source $HOME/miniconda3/etc/profile.d/conda.sh
conda activate facefusion
cd facefusion-advanced
python script.py
EOF

chmod +x run_facefusion.sh
echo "Created run_facefusion.sh script for quick launching"