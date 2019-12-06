import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
import seaborn as sbn


''' Derive a sql query that returns a data set that contains a column for country, a
column for season, and a column for average number of goals scored per game for each country-season combination. '''

engine = sqlalchemy.create_engine('sqlite:///data/database.sqlite')
conn = engine.connect()
df = conn.execute('''
    SELECT name, season , AVG(home_team_goal + away_team_goal) AS Avg_all_goals
    FROM Country
    LEFT JOIN Match
    ON Country.id = Match.country_id
    GROUP BY country.id , season
    ; ''').fetchall()

df = pd.DataFrame(data= df, columns = ['Country','Season', 'Avg_goals_per_game'])

plt.figure(figsize=(20,7))
ax = sbn.lineplot(data = df, x='Season', y='Avg_goals_per_game', hue='Country')
ax.tick_params(labelsize = 14)
plt.title('Average number of goals scored per gamem for each country-season', size = 16)
plt.ylabel('Average number of goals', size = 14)
plt.xlabel('Season', size = 14)
ax.legend( bbox_to_anchor= (1,0.75))
plt.show()


