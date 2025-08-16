import matplotlib.pyplot as plt
import seaborn as sns

def plot_distributions(df):
  for col in df.select_dtypes(include='number').
  sns.histplot(df[col], kde=True)
  plt.title(f'Distribution of {col}')
  plt.show()
