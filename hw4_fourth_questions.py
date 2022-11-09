import pandas as pd
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#

df = pd.read_csv("covid.csv")

def counties_deathConfirmed_ratio(data, activeCases):
    df_aux = data.copy()
    df_aux = df_aux.loc[df_aux["Confirmed"] > activeCases,:]
    df_aux["deathConfirmedRatio"] = df_aux["Deaths"]/df_aux["Confirmed"]
    return df_aux[["Country", "deathConfirmedRatio"]].sort_values(by = "deathConfirmedRatio")

print(counties_deathConfirmed_ratio(df, 500))
print(len(counties_deathConfirmed_ratio(df, 500).index))
print(counties_deathConfirmed_ratio(df, 500)["deathConfirmedRatio"].mean())

print(counties_deathConfirmed_ratio(df, 1000))
print(len(counties_deathConfirmed_ratio(df, 1000).index))
print(counties_deathConfirmed_ratio(df, 1000)["deathConfirmedRatio"].mean())

print(counties_deathConfirmed_ratio(df, 5000))
print(len(counties_deathConfirmed_ratio(df, 5000).index))
print(counties_deathConfirmed_ratio(df, 5000)["deathConfirmedRatio"].mean())
