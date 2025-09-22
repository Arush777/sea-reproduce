######### inference params
CUDA=-1   # MPS on Apple Silicon via Lightning's GPU accelerator; use -1 to force CPU

######### baseline config
TAG="baseline"
CONFIG="config/${TAG}.yaml"

echo "TAG=$TAG CONFIG=$CONFIG CUDA=$CUDA"

python src/inference.py \
  --config_file "$CONFIG" \
  --run_name "$TAG" \
  --gpu $CUDA
