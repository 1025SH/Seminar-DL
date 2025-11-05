import numpy as np
import pandas as pd
import os
data_dir = "./yelp_dataset/"
user_data = os.path.join(data_dir, "yelp_academic_dataset_user.json")
business_data = os.path.join(data_dir, "yelp_academic_dataset_business.json")
review_data = os.path.join(data_dir, "yelp_academic_dataset_review.json")

user_df = pd.read_json(user_data, lines=True)
business_df = pd.read_json(business_data, lines=True)
review_df = pd.read_json(review_data, lines=True)
