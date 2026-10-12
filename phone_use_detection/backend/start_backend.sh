#!/bin/bash

# Configuration
BACKEND_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCREENSHOTS_DIR="$BACKEND_DIR/../screenshots"

echo "🚀 Starting Phone Use Detection Backend..."

# 1. Create screenshots directory if it doesn't exist
if [ ! -d "$SCREENSHOTS_DIR" ]; then
    echo "📁 Creating screenshots directory: $SCREENSHOTS_DIR"
    mkdir -p "$SCREENSHOTS_DIR"
fi

# 2. Check if we are in a virtual environment/conda
if [[ "$CONDA_DEFAULT_ENV" == "" && "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️ Warning: No virtual environment or conda environment detected."
    echo "It is recommended to run this in the 'ia-vision' environment."
else
    echo "✅ Using environment: ${CONDA_DEFAULT_ENV:-$VIRTUAL_ENV}"
fi

# 3. Install/Update dependencies
echo "📦 Checking dependencies..."
pip install -r "$BACKEND_DIR/requirements.txt" --quiet

# 4. Launch the application
echo "🔥 Launching FastAPI server..."
python "$BACKEND_DIR/main.py"
