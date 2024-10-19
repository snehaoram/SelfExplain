 python model/infer_model.py \
      --ckpt lightning_logs/version_1/checkpoints/epoch=1-step=8068-val_acc_epoch=0.9192.ckpt \
      --concept_map data/RoBERTa-SST-2/concept_idx.json \
      --paths_output_loc result/result_robertasst2.tsv \
      --dev_file data/RoBERTa-SST-2/dev_with_parse.json \
      --batch_size 16