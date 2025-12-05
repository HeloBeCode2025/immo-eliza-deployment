from pgeocode import Nominatim
geo = Nominatim("be")
print(geo.query_postal_code("1000"))
