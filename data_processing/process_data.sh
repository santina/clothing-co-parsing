mkdir ../photos_for_training

# copy relevant photos over
cp ../photos/0*.jpg ../photos_for_training
cp ../photos/1000.jpg ../photos_for_training
cp ../photos/1001.jpg ../photos_for_training
cp ../photos/1002.jpg ../photos_for_training
cp ../photos/1003.jpg ../photos_for_training
cp ../photos/1004.jpg ../photos_for_training

# TODO: use parameters for paths
python generate_train_data.py