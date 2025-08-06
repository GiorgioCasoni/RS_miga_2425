from imports import *


#! impostato con il path sul mio pc, cambiare se necessario
dataset_path = 'C:/Users/gcaso/Documents/progetti_uni/RS-MIGA/data/json/'


#* lettura del dataset Musical_Instruments, i due dataframe viene poi convertito in
#* formato parquet e salvato per potervi accedere e potervi operare più rapidamente
#* di un json o un csv

users_reviews = dd.read_json(f'{dataset_path}Musical_Instruments.jsonl', lines=True)

users_reviews.to_parquet('C:/Users/gcaso/Documents/progetti_uni/RS-MIGA/data/Musical_Instruments.parquet', 
              engine='pyarrow', compression='snappy', write_index=False)


items_metadata = dd.read_json(f'{dataset_path}meta_Musical_Instruments.jsonl', lines=True)

items_metadata.to_parquet('C:/Users/gcaso/Documents/progetti_uni/RS-MIGA/data/meta_Musical_Instruments.parquet', 
              engine='pyarrow', compression='snappy', write_index=False)