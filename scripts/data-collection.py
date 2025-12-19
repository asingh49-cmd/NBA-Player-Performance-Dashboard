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