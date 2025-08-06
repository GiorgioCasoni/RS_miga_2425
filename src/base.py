from imports import *

dataset_path = 'C:/Users/gcaso/Documents/progetti_uni/RS-MIGA/data/'
user_reviews = pd.read_parquet(f'{dataset_path}Musical_Instruments.parquet')
print(user_reviews.head(20))
print(user_reviews.shape[0])
print(user_reviews.shape[1])

