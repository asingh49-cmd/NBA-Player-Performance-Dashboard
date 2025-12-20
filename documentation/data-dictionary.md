# NBA Dashboard Data Dictionary

## Data Source
- **API**: NBA Stats API (stats.nba.com)
- **Season**: 2025-26 Regular Season
- **Update Frequency**: Data collected [12/18/2025]
- **Player Filter**: Minimum 5 games played

## Player_Stats_Clean Table
Player performance statistics with traditional and advanced metrics.

**Total Rows**: ~400 players  
**Total Columns**: 60+

### Identifiers
- **PLAYER_ID** (int): Unique player identifier
- **TEAM_ID** (int): Team identifier
- **TEAM_ABBREVIATION** (string): 3-letter team code (e.g., LAL, GSW)
- **TEAM_COUNT** (int): Number of teams played for this season (1 = not traded)
- **PLAYER_NAME** (string): Player's full name
- **NICKNAME** (string): Player's nickname

### Playing Time
- **GP** (int): Games played
- **W** (int): Team wins when player participated
- **L** (int): Team losses when player participated
- **W_PCT** (float): Win percentage in games played
- **MIN** (float): Minutes played per game

### Scoring Statistics (Per Game)
- **PTS** (float): Points per game
- **FGM** (float): Field goals made
- **FGA** (float): Field goals attempted
- **FG_PCT** (float): Field goal percentage (0-100)
- **FG3M** (float): Three-pointers made
- **FG3A** (float): Three-pointers attempted  
- **FG3_PCT** (float): Three-point percentage (0-100)
- **FTM** (float): Free throws made
- **FTA** (float): Free throws attempted
- **FT_PCT** (float): Free throw percentage (0-100)

### Other Statistics (Per Game)
- **OREB** (float): Offensive rebounds
- **DREB** (float): Defensive rebounds
- **REB** (float): Total rebounds
- **AST** (float): Assists
- **TOV** (float): Turnovers
- **STL** (float): Steals
- **BLK** (float): Blocks
- **BLKA** (float): Blocks against (times blocked)
- **PF** (float): Personal fouls
- **PFD** (float): Personal fouls drawn
- **PLUS_MINUS** (float): Plus/minus (point differential when on court)

### Advanced Metrics
- **EFFICIENCY**: Player efficiency rating (PER) (calculated)
- **OFF_RATING** (float): Offensive rating (points produced per 100 possessions)
- **DEF_RATING** (float): Defensive rating (points allowed per 100 possessions)
- **NET_RATING** (float): Net rating (offensive - defensive rating)
- **TS_PCT** (float): True shooting percentage (accounts for 2PT, 3PT, and FT value)
- **EFG_PCT** (float): Effective field goal percentage (weights 3PT at 1.5x)
- **USG_PCT** (float): Usage percentage (% of team plays used while on court)
- **PACE** (float): Team pace (possessions per 48 minutes) when player is on court
- **PACE_PER40** (float): Possessions per 40 minutes
- **AST_PCT** (float): Percentage of teammate field goals the player assisted
- **AST_TO** (float): Assist-to-turnover ratio
- **AST_RATIO** (float): Assists per 100 possessions
- **OREB_PCT** (float): Percentage of available offensive rebounds grabbed
- **DREB_PCT** (float): Percentage of available defensive rebounds grabbed
- **REB_PCT** (float): Percentage of available total rebounds grabbed

### Milestone Achievements
- **DD2** (int): Double-doubles (10+ in two statistical categories)
- **TD3** (int): Triple-doubles (10+ in three statistical categories)

### Fantasy Basketball
*Fantasy metrics provided by NBA Stats API*
- **NBA_FANTASY_PTS** (float): NBA.com fantasy points per game
  - *Typical formula: PTS + (REB × 1.2) + (AST × 1.5) + (STL × 3) + (BLK × 3) - (TOV × 1)*
- **WNBA_FANTASY_PTS** (float): WNBA fantasy scoring format (included for all players)

### League Rankings
*Each major statistic includes a corresponding rank field (e.g., PTS_RANK)*

**Available Rankings**: GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS, NBA_FANTASY_PTS, DD2, TD3, WNBA_FANTASY_PTS

*Rank of 1 = league leader in that category*

## team_stats_clean.csv
Team-level performance statistics (aggregated team performance).

**Total Rows**: 30 teams  
**Total Columns**: 50+

### Identification
- **TEAM_ID** (int): Unique team identifier
- **TEAM_NAME** (string): Full team name (e.g., "Los Angeles Lakers")

### Team Record
- **GP** (int): Games played
- **W** (int): Wins
- **L** (int): Losses
- **W_PCT** (float): Win percentage (0-100)

### Team Statistics (Per Game)
*Same statistical categories as player stats, but aggregated at team level*

**Scoring**: MIN, PTS, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT

**Other Stats**: OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PLUS_MINUS

### Team Rankings
*Each statistic has a corresponding rank among the 30 NBA teams*

**Available Rankings**: GP, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK, BLKA, PF, PFD, PTS, PLUS_MINUS

## players_info.csv
Player biographical information.

- **id** (int): Player ID (matches PLAYER_ID)
- **full_name** (string): Player full name
- **first_name** (string): Player first name
- **last_name** (string): Player last name
- **is_active** (boolean): Currently active in NBA

## teams_info.csv  
Team reference information.

- **id** (int): Team ID (matches TEAM_ID)
- **full_name** (string): Full team name
- **abbreviation** (string): 3-letter team code
- **nickname** (string): Team nickname (e.g., "Lakers")
- **city** (string): Team city
- **state** (string): Team state
- **year_founded** (int): Year franchise was founded

## Data Quality Notes

### Filters Applied
- Players with fewer than 5 games played excluded from analysis
- Only 2025-26 regular season data included

### Data Transformations
- Percentage fields converted from decimals to 0-100 scale
- Missing numerical values replaced with median value of that column
- All numerical values rounded to 2 decimal places
- Data is pretty clean aside from 2 missing values in the first_name column from all_players_info.csv

### Known Limitations
- Players traded mid-season appear as separate entries per team (check TEAM_COUNT)
- Advanced metrics (OFF_RATING, DEF_RATING) require minimum playing time for accuracy
- Rankings reflect snapshot at time of data collection (12/18/2025)

## Key Metrics Explained

### True Shooting Percentage (TS_PCT)
Most accurate measure of shooting efficiency. Accounts for the fact that 3-pointers are worth 50% more than 2-pointers and includes free throw efficiency.

**Formula**: `PTS / (2 × (FGA + 0.44 × FTA))`

### Usage Percentage (USG_PCT)  
Estimates the percentage of team plays used by a player while on the court.

**Interpretation**: 
- 20% = low usage (role player)
- 25% = moderate usage
- 30%+ = high usage (primary scorer/playmaker)

### Net Rating
Overall impact on team performance per 100 possessions.

**Formula**: `OFF_RATING - DEF_RATING`

**Interpretation**:
- Positive = team outscores opponents when player is on court
- Negative = team is outscored when player is on court

### Double-Doubles (DD2) & Triple-Doubles (TD3)
- **DD2**: Games with 10+ in any two categories (usually PTS/REB or PTS/AST)
- **TD3**: Games with 10+ in any three categories (rare achievement)

*For questions about specific metrics or calculations, refer to [NBA Stats API Documentation](https://www.nba.com/stats)*