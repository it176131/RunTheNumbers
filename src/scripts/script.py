from rtn.rentals import SingleFamilyHome as SFM

sfm = SFM(listing_price=150_000)


price = None
rent = 1_000
expenses = sfm.listing_price * 0.01
print(sfm.calculate_cap_rate(price))
print((sfm.listing_price * 0.01 * 12 - expenses) / sfm.listing_price)
print(sfm.calculate_cap_rate(price, rent, expenses))
print((rent * 12 - expenses) / sfm.listing_price)
