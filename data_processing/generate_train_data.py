import scipy.io as si
import os
import cv2

# TODO: use parameters for paths

def generate_segmentation(output_folder):
    annotation_pixel_level = os.path.join("..", "annotations", "pixel-level")
    annotation_files = [os.path.join(annotation_pixel_level, f)
                        for f in os.listdir(annotation_pixel_level)
                        if os.path.isfile(os.path.join(annotation_pixel_level, f))]

    for file in annotation_files:
        labels = si.loadmat(file)
        annotation = labels['groundtruth']
        file_basename = os.path.basename(file)

        output = os.path.join(output_folder, os.path.splitext(file_basename)[0] + ".png")
        cv2.imwrite(output, annotation)

def data_augmentation(folder):

    files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    for file in files:
        flip_horizontal_and_save(file, "_mirrored", folder)


def flip_horizontal_and_save(file, extension, output_folder):
    src = cv2.imread(file)
    src_flipped = cv2.flip(src, 1)
    basename = os.path.basename(file)
    output_filename_woextension = os.path.splitext(basename)[0]
    output_filename = output_filename_woextension + extension + os.path.splitext(basename)[1]
    cv2.imwrite(os.path.join(output_folder, output_filename), src_flipped)


photo_folder = os.path.join("..", "photos_for_training")
seg_folder = os.path.join("..", "segmentations")
os.mkdir(seg_folder)

generate_segmentation(seg_folder)
data_augmentation(photo_folder)
data_augmentation(seg_folder)


