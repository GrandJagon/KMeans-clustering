from create_cluster_data import create_cluster_data
import maths as mth
from KMeans import KMeans
from sklearn.preprocessing import scale


data = create_cluster_data(1000, 5)


kmean = KMeans(mth.standardize(data))


kmean.fit()

kmean.iterate()

kmean.plot()
