# EADA_Data_Augment
EADA, a data augment method for NLP tasks

### How to Use:

Use the atis dataset as an example, 

1. First, run the 'Atis_Dataset_Generate' to generate active_entity and active_packages in Atis folder.

2. Then, run the 'Entity-based_Tree_Atis' to generate entity-based tree for atis dataset. This tree is stored in sentence-simulator-master folder.

3. Last, use run.py in sentence-simulator-master folder, like 

```
python run.py -f TreeSum.json -c 10 -w out/word.txt -s out/sent.txt
```

### Dataset:

Upload all dataset in experiment, which are atis, conll2003 and snips.

### File function：

Conll2003_Dataset_Generate.py: Generate dataset's entity,packages from Conll2003 dataset.

Atis_Dataset_Generate.py: Generate dataset's entity,packages from Conll2003 dataset.

Snip_Dataset_Generate.py: Generate dataset's entity,packages from Conll2003 dataset.



Entity-based_Tree_Conll2003.py: Generate Entity-based Tree from Conll2003 dataset.

Entity-based_Tree_Atis.py: Generate Entity-based Tree from Aits dataset.

Entity-based_Tree_Snip.py: Generate Entity-based Tree from Snip dataset.



Atis_dataset_Splite.py: generating seq.in,seq.out form dataset for atis dataset

