{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d38e6f6-f56d-48de-9624-f8e479bdb405",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Correct file path\n",
    "path = r'C:\\Users\\User\\Documents\\NewDataSet.csv'\n",
    "\n",
    "# Load the data\n",
    "df = pd.read_csv(path)\n",
    "\n",
    "# Display the first few rows\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bccd6fac-9311-4bf0-ab5c-2b2674f3d0cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "path = r'C:\\Users\\User\\Downloads\\User_Dataset.csv'\n",
    "\n",
    "userset = pd.read_csv(path)\n",
    "\n",
    "userset.head"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ae4d353-7631-4906-85eb-20b29373e880",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.merge(df,userset, on='Title')\n",
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c63dca2-5592-4825-b77f-a6a5a67a99ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3109689f-a4d3-4221-a254-a8b5a2fbdd57",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = data.dropna()\n",
    "\n",
    "data.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5cdc147a-5dc5-4c42-8ba4-be26b29cc36f",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.groupby('Title')['user_score'].mean().sort_values(ascending=False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8fd40ad-dd40-4e24-933d-444203f0ae3d",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.groupby('Title')['user_score'].count().sort_values(ascending=False).head() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15e187a7-deda-4c96-96f6-d8ec4658eb7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "data.groupby('Title').count().info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7e7fa61-f0f0-4991-9103-43f535b4f65b",
   "metadata": {},
   "outputs": [],
   "source": [
    "userscores = pd.DataFrame(data.groupby('Title')['user_score'].mean())  \n",
    "\n",
    "userscores['total num of user score'] = pd.DataFrame(data.groupby('Title')['user_score'].count()) \n",
    "\n",
    "userscores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d408a90b-daf7-4f8f-99a3-002b406ef1d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "score_matrix = data.pivot_table(index='user_id', columns='Title', values='user_score', fill_value=0)\n",
    "\n",
    "score_matrix.head()\n",
    "\n",
    "userscores.sort_values('total num of user score', ascending = False).head(10) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5fc5d74e-2234-4bd5-a2db-260fc67dfc8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "game_user_score = score_matrix['Pro Evolution Soccer 2018'] \n",
    "\n",
    "game_user_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c46d777-9096-4d99-9c64-85f13e53a8ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "similar_to_game = score_matrix.corrwith(game_user_score)  \n",
    "  \n",
    "corr_drive = pd.DataFrame(similar_to_game, columns =['Correlation']) \n",
    "corr_drive.dropna(inplace = True) \n",
    "  \n",
    "corr_drive.head() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cea12c5b-8c4c-491c-8cc3-189766468080",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"corr_drive Sample Data:\")\n",
    "print(corr_drive.head())\n",
    "\n",
    "print(\"\\nuserscores Columns:\", userscores.columns.tolist())\n",
    "print(\"userscores Sample Data:\")\n",
    "print(userscores.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "edba5e21-ff05-443f-b17c-1ac1fe5e0a38",
   "metadata": {},
   "outputs": [],
   "source": [
    "corr_drive = corr_drive.drop(columns=['total num of user score'], errors='ignore')\n",
    "\n",
    "corr_drive_sorted = corr_drive.sort_values('Correlation', ascending=False).head(10)\n",
    "\n",
    "merged_corr_drive = corr_drive_sorted.join(userscores['total num of user score'], how='left')\n",
    "\n",
    "print(\"Top 10 Correlations:\")\n",
    "print(merged_corr_drive)\n",
    "\n",
    "missing_scores = merged_corr_drive['total num of user score'].isnull().sum()\n",
    "print(f\"\\nNumber of missing 'total num of user score': {missing_scores}\")\n",
    "\n",
    "\n",
    "merged_corr_drive.dropna(subset=['total num of user score'], inplace=True)\n",
    "\n",
    "high_score_corr = merged_corr_drive[merged_corr_drive['total num of user score'] > 10].sort_values('Correlation', ascending=False).head()\n",
    "\n",
    "print(\"\\nCorrelations with 'total num of user score' > 10:\")\n",
    "print(high_score_corr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4676a1d-537e-4cd7-8869-7c6ee1c6fc36",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
