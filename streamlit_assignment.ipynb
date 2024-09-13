{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9227263-00da-4ce7-8bc5-3cd86cbf26c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st\n",
    "\n",
    "# Load the dataset using the correct file path\n",
    "path = 'C:/Users/User/Documents/NewDataSet.csv'\n",
    "df = pd.read_csv(path)\n",
    "\n",
    "# Display the first few rows of the dataframe\n",
    "st.write(\"First few rows of the dataset:\")\n",
    "st.dataframe(df.head())\n",
    "\n",
    "# Load another dataset\n",
    "path_user = 'C:/Users/User/Downloads/User_Dataset.csv'\n",
    "userset = pd.read_csv(path_user)\n",
    "\n",
    "# Display the first few rows of the second dataframe\n",
    "st.write(\"First few rows of the user dataset:\")\n",
    "st.dataframe(userset.head())\n",
    "\n",
    "# Merge datasets\n",
    "data = pd.merge(df, userset, on='Title')\n",
    "\n",
    "# Display the merged data\n",
    "st.write(\"Merged dataset:\")\n",
    "st.dataframe(data.head())\n",
    "\n",
    "# Handle missing values\n",
    "data = data.dropna()\n",
    "\n",
    "# Groupby and calculate the mean user_score\n",
    "grouped_data = data.groupby('Title')['user_score'].mean().sort_values(ascending=False).head()\n",
    "\n",
    "# Display the groupby results\n",
    "st.write(\"Top Titles by average user_score:\")\n",
    "st.dataframe(grouped_data)\n",
    "\n",
    "# Pivot table for scores\n",
    "score_matrix = data.pivot_table(index='user_id', columns='Title', values='user_score', fill_value=0)\n",
    "\n",
    "# Display the score matrix\n",
    "st.write(\"Score matrix:\")\n",
    "st.dataframe(score_matrix.head())\n",
    "\n",
    "# Display similar game correlations\n",
    "game_user_score = score_matrix['Pro Evolution Soccer 2018']\n",
    "similar_to_game = score_matrix.corrwith(game_user_score)\n",
    "corr_drive = pd.DataFrame(similar_to_game, columns=['Correlation']).dropna()\n",
    "\n",
    "# Display correlations\n",
    "st.write(\"Correlations with 'Pro Evolution Soccer 2018':\")\n",
    "st.dataframe(corr_drive.head())\n"
   ]
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
