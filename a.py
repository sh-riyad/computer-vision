import os 
import pandas as pd

def make_dataframes(train_dir,test_dir):
    dirlist=[train_dir, test_dir]
    names=['train','test']
    zipdir=zip(names, dirlist)
    for name,d in zipdir:
        filepaths=[]
        labels=[]
        classlist=sorted(os.listdir(d) )
        for klass in classlist:
            sklass=klass[:25] # use only first 25 characters of the class as some are very long
            classpath=os.path.join(d, klass)
            flist=sorted(os.listdir(classpath))
            desc=f'{name:6s}-{sklass:25s}'
            for f in tqdm(flist, ncols=130,desc=desc, unit='files', colour='blue'):
                fpath=os.path.join(classpath,f)
                filepaths.append(fpath)
                labels.append(sklass)
        Fseries=pd.Series(filepaths, name='filepaths')
        Lseries=pd.Series(labels, name='labels')
        df=pd.concat([Fseries, Lseries], axis=1)
        if name =='test':
            test_df=df
        else:
            pdf=df
    # create a train_df and a valid_df
    train_df, valid_df = train_test_split(pdf, train_size=.9, shuffle=True, random_state = 123, stratify = pdf['labels'])
    classes=sorted(train_df['labels'].unique())
    class_count=len(classes)
    sample_df=train_df.sample(n=50, replace=False)
    # calculate the average image height and with
    ht=0
    wt=0
    count=0
    for i in range(len(sample_df)):
        fpath=sample_df['filepaths'].iloc[i]
        try:
            img=cv2.imread(fpath)
            h=img.shape[0]
            w=img.shape[1]
            wt +=w
            ht +=h
            count +=1
        except:
            pass
    have=int(ht/count)
    wave=int(wt/count)
    aspect_ratio=have/wave
    print('number of classes in processed dataset= ', class_count)
    counts=list(train_df['labels'].value_counts())
    print('the maximum files in any class in train_df is ', max(counts), '  the minimum files in any class in train_df is ', min(counts))
    print('train_df length: ', len(train_df), '  test_df length: ', len(test_df), '  valid_df length: ', len(valid_df))
    print('average image height= ', have, '  average image width= ', wave, ' aspect ratio h/w= ', aspect_ratio)
    return train_df, test_df, valid_df, classes, class_count


train_dir = r'D:\Darmnet\train'
test_dir=r'D:\Darmnet\test'
train_df, test_df, valid_df, classes, class_count=make_dataframes(train_dir, test_dir)