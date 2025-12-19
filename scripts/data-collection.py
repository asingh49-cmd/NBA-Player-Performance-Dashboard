"""
NBA Data Collection Script 
This script pulls current nba player and team stats from the public NBA API
"""
from nba_api.stats.endpoints import commonplayerinfo, leaguestandings, leaguedashteamstats, leaguedashplayerstats
from nba_api.stats.static import players, teams
import time
import pandas as pd
import os

def get_player_stats(season='2025-26'):
    """Fetching player stats for the given season"""
    print(f'Fetching player stats for season {season}...')
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season,
        per_mode_detailed='PerGame',
        season_type_all_star='Regular Season' 
    )
    player_stats_df = player_stats.get_data_frames()[0]
    print(f'Fetched {len(player_stats_df)} player stats records.')
    return player_stats_df

def get_team_stats(season='2025-26'):
    """Fetching team stats for the given season"""
    print(f'Fetching player stats for season {season}...')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(
        season=season,
        per_mode_detailed='PerGame',
        season_type_all_star='Regular Season' 
    )
    team_stats_df = team_stats.get_data_frames()[0]
    print(f'Fetched {len(team_stats_df)} team stats records.')
    return team_stats_df

def get_advanced_stats(season='2025-26'):
    """Fetching advanced player stats for the given season"""
    print(f'Fetching player stats for season {season}...')
    advanced_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season,
        measure_type_detailed_defense='Advanced',
        per_mode_detailed='PerGame',
        season_type_all_star='Regular Season' 
    )
    advanced_stats_df = advanced_stats.get_data_frames()[0]
    print(f'Fetched {len(advanced_stats_df)} player advanced stats records.')
    return advanced_stats_df 

def get_all_players_info():
    """Fetching all players info"""
    print('Fetching all players info...')
    all_players = players.get_players()
    all_players_df = pd.DataFrame(all_players)
    print(f'Fetched info for {len(all_players_df)} players.')
    return all_players_df

def get_all_teams_info():
    """Fetching all teams info"""
    print('Fetching all teams info...')
    all_teams = teams.get_teams()
    all_teams_df = pd.DataFrame(all_teams)
    print(f'Fetched info for {len(all_teams_df)} teams.')
    return all_teams_df

def main():
    output_dir = 'data/raw'
    os.makedirs(output_dir, exist_ok=True) #check if directory exists, if not create it

    print("-" * 50)
    print("Starting NBA Data Collection Script")
    print("-" * 50)

    try:
        player_stats_df = get_player_stats()
        teams_stats_df = get_team_stats()
        advanced_stats_df = get_advanced_stats()
        all_players_df = get_all_players_info()
        all_teams_df = get_all_teams_info()

        # Save data to CSV files
        player_stats_df.to_csv(os.path.join(output_dir, 'player_stats.csv'), index=False)
        time.sleep(1) # Sleep (pause the program) to avoid hitting rate limits

        teams_stats_df.to_csv(os.path.join(output_dir, 'team_stats.csv'), index=False)
        time.sleep(1)

        advanced_stats_df.to_csv(os.path.join(output_dir, 'advanced_player_stats.csv'), index=False)
        time.sleep(1)

        all_players_df.to_csv(os.path.join(output_dir, 'all_players_info.csv'), index=False)
        time.sleep(1)

        all_teams_df.to_csv(os.path.join(output_dir, 'all_teams_info.csv'), index=False)
        time.sleep(1)

        print("Data collection completed successfully!")
        print("-" * 50)
        print(f"All data saved to directory: {output_dir}")
        print(" - player_stats.csv")
        print(" - team_stats.csv")
        print(" - advanced_player_stats.csv")
        print(" - all_players_info.csv")
        print(" - all_teams_info.csv")
        print("-" * 50)

        print(f"Total Players: {len(player_stats_df)}")
        print(f"Total Teams: {len(teams_stats_df)}")
        print(f"No. of players with 10 or more games played:{len(player_stats_df[player_stats_df['GP']>=10])}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__": #prevents script from being run on import
    main()