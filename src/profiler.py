def profile_data(df):
  return {
    "shape": df.shape,
    "missing values": df.isnull().sum().to_dic(),
    "dtypes": df.dtypes.astype(str).to_dict(),
    "unique_counts": df.nunique().to_dict()
  }
