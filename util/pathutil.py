from os.path import join

coco_dir = "/coco"
coco_debug = "coco-debug"
#coco_dir = "/coco" # For FloydHub, this will be the mount point
# Usually coco_dir would be "coco" for local path
anno_dir = join(coco_dir, "annotations")
img_dir  = join(coco_dir, "images")
img_dir_debug = join(coco_debug, "images")

tv_anno_dir = join(anno_dir, "annotations_trainval2017")
val_anno_file = join(tv_anno_dir, "instances_val2017.json")
train_anno_file = join(tv_anno_dir, "instances_train2017.json")

train_img_dir_wrapper  = join(img_dir, "people-train2017-wrapper")
val_img_dir_wrapper    = join(img_dir, "people-val2017-wrapper")
train_mask_dir_wrapper = join(img_dir, "mask-train2017-wrapper")
val_mask_dir_wrapper   = join(img_dir, "mask-val2017-wrapper")

train_img_debug  = join(img_dir_debug, "people-train2017-wrapper")
val_img_debug    = join(img_dir_debug, "people-val2017-wrapper")
train_mask_debug = join(img_dir_debug, "mask-train2017-wrapper")
val_mask_debug   = join(img_dir_debug, "mask-val2017-wrapper")


