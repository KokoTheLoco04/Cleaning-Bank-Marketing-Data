import pandas as pd
import numpy as np

# 1. Load the csv file
df = pd.read_csv('bank_marketing.csv')

# 2. Create and clean CLIENT data
client = df[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']].copy()

client['job'] = client['job'].str.replace('.', '_')
client['education'] = client['education'].str.replace('.', '_').replace('unknown', np.nan)
client['credit_default'] = client['credit_default'].map({'yes': 1, 'no': 0, 'unknown': 0}).astype(bool)
client['mortgage'] = client['mortgage'].map({'yes': 1, 'no': 0, 'unknown': 0}).astype(bool)

# 3. Create and clean CAMPAIGN data
campaign = df[['client_id', 'number_contacts', 'contact_duration', 'previous_campaign_contacts', 'previous_outcome', 'campaign_outcome', 'day', 'month']].copy()

campaign['previous_outcome'] = campaign['previous_outcome'].map({'success': 1, 'failure': 0, 'nonexistent': 0}).astype(bool)
campaign['campaign_outcome'] = campaign['campaign_outcome'].map({'yes': 1, 'no': 0}).astype(bool)
campaign['last_contact_date'] = pd.to_datetime(
    '2022-' + campaign['month'].astype(str) + '-' + campaign['day'].astype(str),
    format='%Y-%b-%d'
)
campaign = campaign.drop(['day', 'month'], axis=1)

# 4. Create ECONOMICS data
economics = df[['client_id', 'cons_price_idx', 'euribor_three_months']].copy()
economics = economics.astype({'cons_price_idx':float, 'euribor_three_months': float})

# 5. Create CSV files
client.to_csv('client.csv', index=False)
campaign.to_csv('campaign.csv', index=False)
economics.to_csv('economics.csv', index=False)

print("Successfully created: client.csv, campaign.csv, economics.csv")