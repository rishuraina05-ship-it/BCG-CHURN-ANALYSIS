{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "849718cf-a752-4c05-8d31-44ac31a6ea3f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b4e55e02-03ae-4963-9bff-02d4910b88e2",
   "metadata": {},
   "source": [
    "# Sub-Task 1: Feature Engineering"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "cca30a7f-77a3-4913-b1a2-9e82e32ccdb6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load data and recreate the colleague's feature\n",
    "client_data = pd.read_csv(r\"C:\\Users\\rishu\\Downloads\\4.1 Client Data\")\n",
    "price_data = pd.read_csv(r\"C:\\Users\\rishu\\Downloads\\4.2 Price Data\")\n",
    "merged_data = pd.merge(client_data, price_data, on='id', how='left')\n",
    "\n",
    "merged_data['date'] = pd.to_datetime(merged_data['price_date']) #Corrected line\n",
    "merged_data['year'] = merged_data['date'].dt.year\n",
    "merged_data['month'] = merged_data['date'].dt.month\n",
    "\n",
    "dec_off_peak = merged_data[(merged_data['month'] == 12) & (merged_data['year'] == 2015)]['price_off_peak_var'].values\n",
    "jan_off_peak = merged_data[(merged_data['month'] == 1) & (merged_data['year'] == 2016)]['price_off_peak_var'].values\n",
    "\n",
    "if len(dec_off_peak) > 0 and len(jan_off_peak) > 0:\n",
    "    price_diff = jan_off_peak[0] - dec_off_peak[0]\n",
    "    merged_data['off_peak_price_diff_dec_jan'] = price_diff\n",
    "else:\n",
    "    merged_data['off_peak_price_diff_dec_jan'] = np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5ca27f83-a049-49c0-b545-b7093d74f48f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Calculate price difference for each customer, not just the first values.\n",
    "price_diff_per_customer = merged_data.groupby('id').apply(\n",
    "    lambda x: x[(x['month'] == 1) & (x['year'] == x['year'].max())]['price_off_peak_var'].values[0] -\n",
    "              x[(x['month'] == 12) & (x['year'] == x['year'].max() - 1)]['price_off_peak_var'].values[0]\n",
    "    if len(x[(x['month'] == 1) & (x['year'] == x['year'].max())]['price_off_peak_var'].values) > 0 and\n",
    "       len(x[(x['month'] == 12) & (x['year'] == x['year'].max() - 1)]['price_off_peak_var'].values) > 0\n",
    "    else np.nan\n",
    ")\n",
    "merged_data['off_peak_price_diff_dec_jan_per_customer'] = merged_data['id'].map(price_diff_per_customer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a6a826cc-f029-4293-aeb4-f5c7d529168f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Add features related to overall price changes.\n",
    "merged_data['price_mid_peak_vare'] = merged_data.groupby('price_date')['price_mid_peak_var'].pct_change()\n",
    "merged_data['price_mid_peak_fix'] = merged_data.groupby('price_date')['price_mid_peak_fix'].pct_change()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fb4741a4-565b-4c86-bf6a-e312901762e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\rishu\\AppData\\Local\\Temp\\ipykernel_2836\\1448276365.py:2: FutureWarning: The default fill_method='ffill' in SeriesGroupBy.pct_change is deprecated and will be removed in a future version. Either fill in any non-leading NA values prior to calling pct_change or specify 'fill_method=None' to not fill NA values.\n",
      "  merged_data['forecast_price_energy_peak'] = merged_data.groupby('id')['forecast_price_energy_peak'].pct_change()\n"
     ]
    }
   ],
   "source": [
    "# 3. Add forecast related features.\n",
    "merged_data['forecast_price_energy_peak'] = merged_data.groupby('id')['forecast_price_energy_peak'].pct_change()\n",
    "merged_data['forecast_price_pow_off_peak'] = merged_data.groupby('id')['forecast_price_pow_off_peak'].pct_change()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "6f859aaf-eb3c-4a27-a78c-da4f18ea7e70",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4. Add time based features\n",
    "merged_data['date_activ'] = pd.to_datetime(merged_data['date_activ'])\n",
    "merged_data['date_end'] = pd.to_datetime(merged_data['date_end'], errors='coerce')\n",
    "merged_data['contract_duration'] = (merged_data['date_end'] - merged_data['date_activ']).dt.days"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8bf6928c-a46f-4a98-971f-51038f0a4d1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Drop unnecessary features\n",
    "merged_data = merged_data.drop(['date', 'year', 'month','id','date_activ','date_end'], axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c1c4ce91-beed-4e57-8bb6-69ecb696b031",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Clean data\n",
    "merged_data = merged_data.replace([np.inf, -np.inf], np.nan)\n",
    "merged_data = merged_data.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "78f92396-4c4a-4a5c-9605-f0ef05fed300",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The 'id' column does NOT exist.\n",
      "Index(['channel_sales', 'cons_12m', 'cons_gas_12m', 'cons_last_month',\n",
      "       'date_modif_prod', 'date_renewal', 'forecast_cons_12m',\n",
      "       'forecast_cons_year', 'forecast_discount_energy',\n",
      "       'forecast_meter_rent_12m', 'forecast_price_energy_off_peak',\n",
      "       'forecast_price_energy_peak', 'forecast_price_pow_off_peak', 'has_gas',\n",
      "       'imp_cons', 'margin_gross_pow_ele', 'margin_net_pow_ele', 'nb_prod_act',\n",
      "       'net_margin', 'num_years_antig', 'origin_up', 'pow_max', 'churn',\n",
      "       'price_date', 'price_off_peak_var', 'price_peak_var',\n",
      "       'price_mid_peak_var', 'price_off_peak_fix', 'price_peak_fix',\n",
      "       'price_mid_peak_fix', 'off_peak_price_diff_dec_jan',\n",
      "       'off_peak_price_diff_dec_jan_per_customer', 'contract_duration'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "if 'id' in merged_data.columns:\n",
    "    print(\"The 'id' column exists.\")\n",
    "    # Now, your groupby operation should work\n",
    "    merged_data['price_mid_peak_vare'] = merged_data.groupby('id')['price_mid_peak_var'].pct_change()\n",
    "    merged_data['price_mid_peak_fix'] = merged_data.groupby('id')['price_mid_peak_fix'].pct_change()\n",
    "else:\n",
    "    print(\"The 'id' column does NOT exist.\")\n",
    "    print(merged_data.columns) #Print all of the columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f4fa957-9692-4d14-876d-1d5d3988b43d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
