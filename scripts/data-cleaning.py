"""
Preparing and Cleaning Data for Power BI Usage 
"""
import pandas as pd
import numpy as np

def clean_player_stats(df):
    """ Cleaning Player_Stats table for Power BI usage """
    print("Cleaning Player Stats data...")

    # Filter: Keep Players with 5+ Games Played
    df_clean = df[df['GP']>=5].copy()
    print(f"Filtered players with 5+ games: {len(df_clean)} records remain.")

    # Handle Missing Values: Fill NaNs with 0, data pretty clean otherwise
    pct_col = ['FG_PCT', 'FG3_PCT', 'FT_PCT','W_PCT']
    df_clean = df.fillna(df_clean.median(numeric_only=True))

    # Making percentage columns between 0 - 100
    df_clean[pct_col] = df_clean[pct_col] * 100
    print("Filled missing percentage values with 0 and adjusted scale.")

    # Create PER column if not exists
    if 'Efficiency' not in df_clean.columns:
        df_clean['Efficiency'] = (df_clean['PTS']+df_clean['REB']+df_clean['AST']
                                  +df_clean['STL']+df_clean['BLK']
                                  -(df_clean['FGA']-df_clean['FGM'])
                                  -(df_clean['FTA'])-df_clean['FTM']
                                  -df_clean['TOV'])/df_clean['GP']
        print("Created Efficiency column.")
    
    # Round numeric columns to 2dp
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    df_clean[numeric_cols] = df_clean[numeric_cols].round(2)

    print("Player Stats data cleaning complete.")
    return df_clean

def clean_team_stats(df):
    """ Cleaning Team_Stats table for Power BI usage """
    print("Cleaning Team Stats data...")

    # Handle Missing Values: Fill NaNs with median, data pretty clean otherwise
    pct_col = ['FG_PCT', 'FG3_PCT', 'FT_PCT', 'W_PCT']
    df = df.fillna(df.median(numeric_only=True))
    # Adjust percentage columns between 0 - 100
    df[pct_col] = df[pct_col] * 100
    print("Filled missing percentage values with 0 and adjusted scale.")

    # Round numeric columns to 2dp
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].round(2)

    print("Team Stats data cleaning complete.")
    return df

def merge_advanced_stats(player_stats, advanced_stats):
    """ Merging Advanced Stats into Player Stats """
    print("Merging Advanced Stats into Player Stats...")

    # Columns to keep from advanced stats
    adv_cols = ['PLAYER_ID', 'OFF_RATING', 'DEF_RATING', 'NET_RATING', 'AST_PCT', 'AST_TOV', 'AST_RATIO',
                'OREB_PCT', 'DREB_PCT', 'REB_PCT', 'TS_PCT', 'USG_PCT', 'EFG_PCT', 'PACE','PACE_PER40']
    advanced_subset = advanced_stats[adv_cols].copy()

    # Merge on PLAYER_ID
    merged_df = pd.merge(player_stats, advanced_subset, on=['PLAYER_ID'], how='left')
    print(f"Merged DataFrame has {len(merged_df)} records")

    # Handle Missing % and Values: Fill NaNs with median for advanced stats, data pretty clean otherwise
    adv_fill_cols = ['AST_PCT','OREB_PCT', 'DREB_PCT', 'REB_PCT', 'TS_PCT', 'USG_PCT', 'EFG_PCT']
    merged_df = merged_df.fillna(merged_df.median(numeric_only=True))

    # Adjust percentage columns between 0 - 100
    merged_df[adv_fill_cols] = merged_df[adv_fill_cols] * 100

    # Round numeric columns to 2dp
    numeric_cols = merged_df.select_dtypes(include=[np.number]).columns
    merged_df[numeric_cols] = merged_df[numeric_cols].round(2)

    print("Merging complete.")
    return merged_df

def clean_all_players(df):
    """ Cleaning All_Players_Info table for Power BI usage """
    print("Cleaning All Players Info data...")

    # Drop Rows with Missing Values
    df.dropna(subset=['id'],inplace=True)

    print("All Players Info data cleaning complete.")
    return df
def clean_all_teams(df):
    """ Cleaning All_Teams_Info table for Power BI usage """
    print("Cleaning All Teams Info data...")
    
    # Drop Rows with Missing Values
    df.dropna(subset=['id'],inplace=True)

    print("All Teams Info data cleaning complete.")
    return df
        
def main():
    print('-'*50)
    print("Starting Data Cleaning Process...")
    print('-'*50)

    player_stats = pd.read_csv('../data/raw/player_stats.csv')
    team_stats = pd.read_csv("../data/raw/team_stats.csv")
    advanced_stats = pd.read_csv("../data/raw/advanced_player_stats.csv")
    all_players = pd.read_csv("../data/raw/all_players_info.csv")
    all_teams = pd.read_csv("../data/raw/all_teams_info.csv")