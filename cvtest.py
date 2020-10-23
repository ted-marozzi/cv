from fastai.vision.all import *
import torch






def label_func(f): return f[0].isupper()



def main():
    path = untar_data(URLs.PETS)

    files = get_image_files(path/"images")

    pat = r'^(.*)_\d+.jpg'

    dls = ImageDataLoaders.from_name_re(path, files, pat, item_tfms=Resize(460),
                                        batch_tfms=aug_transforms(size=224), num_workers=0)

    learn = cnn_learner(dls, resnet34, metrics=error_rate)
    print(learn.lr_find())

    

if __name__ == '__main__':
    main()
