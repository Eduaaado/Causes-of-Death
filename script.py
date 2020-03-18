import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.style as style
sns.set()

style.use('seaborn')
data = pd.read_csv('data/nchs-age-adjusted-death-rates-for-selected-major-causes-of-death.csv', thousands='.')

year = list(data.Year.unique())

deaths = data.groupby('Cause')['Age Adjusted Death Rate'].sum()
deaths = deaths.to_frame()
deaths.reset_index(level=0, inplace=True)
deaths = deaths.sort_values(by=['Age Adjusted Death Rate'], ascending = False)

plt.figure(figsize=(16, 8))
plt.bar(deaths['Cause'], deaths['Age Adjusted Death Rate'], color=sns.cubehelix_palette(10, start=.6, rot=.1, reverse=True))

plt.xlabel('Cause') 
plt.ylabel('Deaths')

plt.title('U.S. mortality trends since 1900')

plt.setp(
    plt.gca().get_xticklabels(),
    fontsize=6
)

fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('graph.png', dpi=500)