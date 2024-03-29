import torch

batch_size = 32
num_epochs = 300
vocab_size = 50000
embedding_size = 300
enc_hidden_size = 500
dec_hidden_size = 700
att_embedding_size = 200
ber_prob = 0.5
d_lr = 2e-5
g_lr = 1e-3
loss_lambda = 0.5
max_decode_step = 20

train = True
debug = True
glove_path = "data/glove.840B.300d.txt"
save_dir = "./save"
model_path = "./save/14_7.ckpt"
output_dir = "./result"
device = torch.device("cuda:0")
