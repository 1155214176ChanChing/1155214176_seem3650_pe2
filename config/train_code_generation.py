
out_dir = 'out-code-generation'
eval_interval = 250
eval_iters = 20
log_interval = 10

always_save_checkpoint = False

dataset = 'code_generation'
batch_size = 16
block_size = 128

n_layer = 4
n_head = 4
n_embd = 128
dropout = 0.0

device = 'cuda'
compile = False

max_iters = 2000
lr_decay_iters = 2000
learning_rate = 1e-3
min_lr = 1e-4
warmup_iters = 100
