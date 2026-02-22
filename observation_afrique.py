import pandas as pd
import plotly.express as px

data=pd.read_csv("../Africa_climate_change.csv", sep=',')
null=data.isnull().sum()
print(data.info())
data.fillna(data.isnull().median(), inplace=True)
print(data.describe())
print(data.isnull().sum())
filter = data.query("COUNTRY == 'Tunisia' or COUNTRY == 'Cameroon'")
print(filter.head())
filter["DATE"] = pd.to_datetime(filter["DATE"])
filter["year"] = filter["DATE"].dt.year
tunis_cam=filter.groupby(["COUNTRY","year"],as_index=False)["TAVG"].mean()
print(tunis_cam)
fig=px.line(tunis_cam, x="year", y="TAVG", color="COUNTRY",
                 labels = {"year" : 'Year',"TAVG" : 'Moyenne'})
fig.show()
zoom=tunis_cam.query("year > 1980 and year < 2005")
fig_zoom=px.line(zoom, x="year", y="TAVG", color="COUNTRY",
                 labels = {"year" : 'Year',"TAVG" : 'Moyenne'})
fig_zoom.show()
t_sinigale=data[data["COUNTRY"] == "Senegal"]
print(t_sinigale.head())
t_sinigale["DATE"] = pd.to_datetime(t_sinigale["DATE"])
t_sinigale["year"]=t_sinigale["DATE"].dt.year
print(t_sinigale.head())
his1=t_sinigale[(t_sinigale["year"]>1980) & (t_sinigale["year"]<2000)]
his2=t_sinigale[(t_sinigale["year"]>2000) & (t_sinigale["year"]<2025)]

print(his1)
hist_data = pd.concat([his1, his2])
fig_his=px.histogram(hist_data, x="year")
fig_his.show()
# the cameroun is hot par apaur au tunis
