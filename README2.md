- Tải annotation về máy
- Tải 2 file "EPIC_100_noun_classes.csv" và "EPIC_100_verb_classes.csv" ở
  trong "https://github.com/epic-kitchens/epic-kitchens-100-annotations.git"
- Copy thêm 2 file "EPIC_100_noun_classes.csv" và "EPIC_100_verb_classes.csv"
  từ "https://github.com/epic-kitchens/epic-kitchens-100-annotations.git" vào thư mục "annotations/epic100RET"
- Sao chép file có tên "sent2rolegraph_augmented.json" trong thư mục "annotations/epic100RET" từ file "
  sent2rolegraph.augment.json" trong "annotations/epic100RET" vì mã code yêu cầu tên file này

B1 : export PYTHONPATH=$(pwd):${PYTHONPATH} để đặt biến môi trường cho PYTHONPATH
B2 : python t2vretrieval/driver/configs/prepare_mlmatch_configs_EK100_TBN_augmented_VidTxtLate.py . (Chạy file config
nào cũng được mỗi file config thì sẽ có một cấu hình cho model khác nhau)

- Sau khi chạy B2 sẽ trả về một đường dẫn "results/RET.released/mlmatch/tên_folder_dược_sinh_ra
- Gán biến resdir = "results/RET.released/mlmatch/tên_folder_dược_sinh_ra hoặc tự copy sau đó để chạy B3

B3 : python t2vretrieval/driver/multilevel_match.py $resdir/model.json $resdir/path.json --is_train --load_video_first
--resume_file glove_checkpoint_path

- Sử dụng "--load_video_first" để load tất cả video 1 lần => không nên vì sẽ không đủ tài nguyên
- Sử dụng "--resume_file glove_checkpoint_path" nếu đã training lần trước rồi và lần chạy này muốn chạy
  tiếp chứ không phải training từ đầu
- glove_checkpoint_path : path epoch cuối cùng của model đã training trước đó
=> Lần đầu "python t2vretrieval/driver/multilevel_match.py $resdir/model.json $resdir/path.json --is_train""