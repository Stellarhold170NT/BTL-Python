import pandas as pd

data=pd.read_csv('results.csv')
numeric_df = data.select_dtypes(include=[float, int])

overall_stats = {
    f"{stat}_mean": numeric_df[stat].mean() for stat in numeric_df.columns
}
overall_stats.update({
    f"{stat}_median": numeric_df[stat].median() for stat in numeric_df.columns
})
overall_stats.update({
    f"{stat}_std": numeric_df[stat].std() for stat in numeric_df.columns
})
overall_stats['Team'] = 'all'  
overall_stats_df = pd.DataFrame([overall_stats])

team_mean = data.groupby('Team')[numeric_df.columns].mean().rename(columns=lambda x: x + '_mean')
team_median = data.groupby('Team')[numeric_df.columns].median().rename(columns=lambda x: x + '_median')
team_std = data.groupby('Team')[numeric_df.columns].std().rename(columns=lambda x: x + '_std')

team_stats = pd.concat([team_mean, team_median, team_std], axis=1).reset_index()
final_stats = pd.concat([overall_stats_df, team_stats], ignore_index=True)
final_stats = final_stats[['Team'] + [col for col in final_stats.columns if col != 'Team']]
final_stats=final_stats.drop(columns=['Unnamed: 0_mean','Unnamed: 0_std','Unnamed: 0_median'])
final_stats.to_csv('results2.csv', index=False)