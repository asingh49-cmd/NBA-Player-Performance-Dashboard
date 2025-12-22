# Tableau Calculated Fields & Parameters

Complete documentation of all custom calculations, parameters, and formulas used in the NBA Player Performance Dashboard.

---

## 📋 Table of Contents
1. [Parameters](#parameters)
2. [Calculated Fields - Player Analysis](#calculated-fields---player-analysis)
3. [Calculated Fields - Team Analysis](#calculated-fields---team-analysis)
4. [Calculated Fields - Filters & Logic](#calculated-fields---filters--logic)
5. [Table Calculations](#table-calculations)
6. [Reference Lines & Annotations](#reference-lines--annotations)

---

## Parameters

### Select Player 1
**Purpose**: Allow users to choose first player for comparison

**Configuration:**
- **Data Type**: String
- **Allowable Values**: List (populated from Player Name field)
- **Current Value**: Default selection or dynamic
- **Display**: Dropdown control

**Usage**: Used in player comparison worksheet to filter and display selected player's statistics

---

### Select Player 2
**Purpose**: Allow users to choose second player for comparison

**Configuration:**
- **Data Type**: String
- **Allowable Values**: List (populated from Player Name field)
- **Current Value**: Default selection or dynamic
- **Display**: Dropdown control

**Usage**: Used in player comparison worksheet to filter and display selected player's statistics

---

## Calculated Fields - Player Analysis

### All-Around Score
**Purpose**: Composite metric measuring player contribution across all major statistical categories

**Formula**:
```
[PTS] + [REB] + [AST] + [STL] + [BLK]
```

**Interpretation**:
- 20-30: Role player
- 30-40: Solid contributor
- 40-50: All-Star level
- 50+: Superstar/MVP candidate

**Used In**: All-Around Impact bubble chart

---

### Impact per Minute
**Purpose**: Normalize all-around production by playing time

**Formula**:
```
[All-Around Score] / [MIN PER GAME]
```

**Interpretation**:
- Shows efficiency of statistical production
- Higher values indicate players who stuff the stat sheet in limited time
- Useful for comparing starters vs bench players

**Used In**: All-Around Impact bubble chart (Y-axis alternative)

---

### True Shooting Percentage (Enhanced)
**Purpose**: Most accurate measure of shooting efficiency accounting for 2PT, 3PT, and FT value

**Formula**:
```
[PTS] / (2 * ([FGA] + 0.44 * [FTA])) * 100
```

**Note**: Provided in data, use as-is. Formula included for reference.

**Interpretation**:
- <50%: Below average efficiency
- 50-55%: Average
- 55-60%: Above average
- 60%+: Elite efficiency

---

### Efficiency Rating (Simple PER)
**Purpose**: Quick player efficiency calculation based on box score stats

**Formula**:
```
([PTS] + [REB] + [AST] + [STL] + [BLK] - 
 ([FGA] - [FGM]) - ([FTA] - [FTM]) - [TOV]) / [GP]
```

**Interpretation**:
- Positive values indicate net positive contribution
- Higher is better
- Accounts for both positive stats and negative plays (missed shots, turnovers)

**Used In**: Player rankings, comparison tool

---

### Performance vs League Average (Z-Score)
**Purpose**: Show how far above or below league average a team performs in any stat

**Formula**:
```
(
  SUM([Team AST]) - WINDOW_AVG(SUM([Team AST]))
) 
/ 
WINDOW_STDEV(SUM([Team AST]))
```

**Note**: Replace `[Team AST]` with any team statistic

**Interpretation**:
- 0 = League average
- +1 = One standard deviation above average
- -1 = One standard deviation below average
- ±2+ = Elite or bottom-tier performance

**Compute Using**: Team Name (for proper table calculation)

**Used In**: Team heatmap coloring, performance filters

---

## Calculated Fields - Filters & Logic

### Show Selected Players
**Purpose**: Filter to display only the two players selected in comparison parameters

**Formula**:
```
IF [Select Player 1] = [Select Player 2] THEN
    [Player Name] = [Select Player 1]
ELSE
    ([Player Name] = [Select Player 1]) 
    OR ([Player Name] = [Select Player 2])
END
```

**Usage**: 
1. Add to Filters shelf
2. Select "True"
3. Ensures only selected players appear in comparison view

**Edge Case Handling**: The IF statement prevents duplicate display if same player is selected twice

---

### Conference
**Purpose**: Categorize teams into Eastern or Western Conference

**Formula**:
```
CASE [Team Abbreviation]
    // Eastern Conference
    WHEN "ATL" THEN "East"
    WHEN "BOS" THEN "East"
    WHEN "BKN" THEN "East"
    WHEN "CHA" THEN "East"
    WHEN "CHI" THEN "East"
    WHEN "CLE" THEN "East"
    WHEN "DET" THEN "East"
    WHEN "IND" THEN "East"
    WHEN "MIA" THEN "East"
    WHEN "MIL" THEN "East"
    WHEN "NYK" THEN "East"
    WHEN "ORL" THEN "East"
    WHEN "PHI" THEN "East"
    WHEN "TOR" THEN "East"
    WHEN "WAS" THEN "East"
    
    // Western Conference
    WHEN "DAL" THEN "West"
    WHEN "DEN" THEN "West"
    WHEN "GSW" THEN "West"
    WHEN "HOU" THEN "West"
    WHEN "LAC" THEN "West"
    WHEN "LAL" THEN "West"
    WHEN "MEM" THEN "West"
    WHEN "MIN" THEN "West"
    WHEN "NOP" THEN "West"
    WHEN "OKC" THEN "West"
    WHEN "PHX" THEN "West"
    WHEN "POR" THEN "West"
    WHEN "SAC" THEN "West"
    WHEN "SAS" THEN "West"
    WHEN "UTA" THEN "West"
    
    ELSE "Unknown"
END
```

**Used In**: Conference filters across all dashboards

---

### Division
**Purpose**: Categorize teams into their six NBA divisions

**Formula**:
```
CASE [Team Abbreviation]
    // Atlantic Division (East)
    WHEN "BOS" THEN "Atlantic"
    WHEN "BKN" THEN "Atlantic"
    WHEN "NYK" THEN "Atlantic"
    WHEN "PHI" THEN "Atlantic"
    WHEN "TOR" THEN "Atlantic"
    
    // Central Division (East)
    WHEN "CHI" THEN "Central"
    WHEN "CLE" THEN "Central"
    WHEN "DET" THEN "Central"
    WHEN "IND" THEN "Central"
    WHEN "MIL" THEN "Central"
    
    // Southeast Division (East)
    WHEN "ATL" THEN "Southeast"
    WHEN "CHA" THEN "Southeast"
    WHEN "MIA" THEN "Southeast"
    WHEN "ORL" THEN "Southeast"
    WHEN "WAS" THEN "Southeast"
    
    // Northwest Division (West)
    WHEN "DEN" THEN "Northwest"
    WHEN "MIN" THEN "Northwest"
    WHEN "OKC" THEN "Northwest"
    WHEN "POR" THEN "Northwest"
    WHEN "UTA" THEN "Northwest"
    
    // Pacific Division (West)
    WHEN "GSW" THEN "Pacific"
    WHEN "LAC" THEN "Pacific"
    WHEN "LAL" THEN "Pacific"
    WHEN "PHX" THEN "Pacific"
    WHEN "SAC" THEN "Pacific"
    
    // Southwest Division (West)
    WHEN "DAL" THEN "Southwest"
    WHEN "HOU" THEN "Southwest"
    WHEN "MEM" THEN "Southwest"
    WHEN "NOP" THEN "Southwest"
    WHEN "SAS" THEN "Southwest"
    
    ELSE "Unknown"
END
```

**Used In**: Division filters, geographic analysis

---

### Qualified Player (Minimum Thresholds)
**Purpose**: Filter to players with meaningful sample size

**Formula**:
```
[GP] >= 5 AND [MIN PER GAME] >= 15
```

**Rationale**:
- 10 games minimum for statistical reliability

**Usage**: Apply as filter to remove outliers and small samples

---

## Table Calculations

### Rank (Points Per Game)
**Purpose**: Rank players by scoring average

**Calculation**:
```
RANK([Avg Points Per Game], 'desc')
```

**Compute Using**: Player Name

**Used In**: Leaderboards, top N filters

---

## Reference Lines & Annotations

### League Average - Usage Rate
**Value**: 20% (approximately)
**Type**: Constant line
**Purpose**: Identify high-usage players

### League Average - True Shooting %
**Value**: 57-58% (varies by season)
**Type**: Constant line
**Purpose**: Benchmark shooting efficiency

---

## Best Practices & Tips

### When Creating Calculated Fields:

1. **Name Clearly**: Use descriptive names (not "Calc1" or "Field2")
2. **Test Edge Cases**: What if GP = 0? Division by zero errors?
3. **Use Consistent Formatting**: Upper case for functions, proper spacing
4. **Aggregate Appropriately**: Know when to use SUM vs AVG vs ATTR

### Performance Tips:

1. **Minimize Nested Calculations**: Pre-calculate in data prep when possible
2. **Use Parameters for Dynamic Filters**: Better than complex LOD expressions
3. **Table Calculations**: Be explicit with "Compute Using" settings

### Common Errors:

**"Cannot mix aggregate and non-aggregate arguments"**
- Fix: Wrap all fields in AGG() or make entire calc an aggregation

**Table calculation returning NULL**
- Fix: Check "Compute Using" direction (Table Down vs Across)

**Parameter not updating visualization**
- Fix: Ensure calculated field references parameter correctly

---

## Advanced Techniques Used

### Conditional Formatting Logic
```
IF [TS_PCT] >= 60 THEN "Elite"
ELSEIF [TS_PCT] >= 55 THEN "Above Average"
ELSEIF [TS_PCT] >= 50 THEN "Average"
ELSE "Below Average"
END
```

### Multi-Level Hierarchies
- Conference → Division → Team
- Allows drill-down analysis

---

## Resources & Further Reading

- [Basketball Reference - Glossary](https://www.basketball-reference.com/about/glossary.html)
- [NBA Advanced Stats Explained](https://www.nba.com/stats/help/glossary)
