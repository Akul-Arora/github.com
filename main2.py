import plotly.express as px
low_gravity_stars = []
for index, gravity in enumerate(stars_gravity):
  if gravity < 10:
    low_gravity_stars.append(stars_data_rows[index])

print(len(low_gravity_stars))
low_gravity_stars = []
for index, gravity in enumerate(stars_gravity):
  if gravity < 100:
    low_gravity_stars.append(stars_data_rows[index])

print(len(low_gravity_stars))

star_type_values = []
for star_data in stars_data_rows:
  star_type_values.append(star_data[6])

print(list(set(star_type_values)))

star_masses = []
star_radiuses = []
for star_data in low_gravity_stars:
  star_masses.append(star_data[3])
  star_radiuses.append(star_data[7])

fig = px.scatter(x=star_radiuses, y=star_masses)
fig.show()