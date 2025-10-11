# All products are listed below

# Sewing thread (100m)
price_sewing_thread_100m = 1.20
stock_level_sewing_thread_100m = 184
stock_price_sewing_thread_100m = price_sewing_thread_100m * stock_level_sewing_thread_100m

# Zipper (20cm) 
price_zipper_20cm = 0.65
stock_level_zipper_20cm = 97
stock_price_zipper_20cm = price_zipper_20cm * stock_level_zipper_20cm

# Wooden Buttons (Pack of 10)
price_wooden_buttons_pack_of_10 = 1.80
stock_level_wooden_buttons_pack_of_10 = 142
stock_price_wooden_buttons_pack_of_10 = price_wooden_buttons_pack_of_10 * stock_level_wooden_buttons_pack_of_10

# iron_on_interfacing_1m
price_iron_on_interfacing_1m = 2.50
stock_level_iron_on_interfacing_1m = 76
stock_price_iron_on_interfacing_1m = price_iron_on_interfacing_1m * stock_level_iron_on_interfacing_1m

# bias_binding_2.5m
price_bias_binding_2_5m = 1.10
stock_level_bias_binding_2_5m = 213
stock_price_bias_binding_2_5m = price_bias_binding_2_5m * stock_level_bias_binding_2_5m

# hook_and_eye_set_10_pairs
price_hook_and_eye_set_10_pairs = 0.90
stock_level_hook_and_eye_set_10_pairs = 58
stock_price_hook_and_eye_set_10_pairs = price_hook_and_eye_set_10_pairs * stock_level_hook_and_eye_set_10_pairs

# seam_ripper
price_seam_ripper = 1.50
stock_level_seam_ripper = 34
stock_price_seam_ripper = price_seam_ripper * stock_level_seam_ripper

# tailors_chalk_3_pack
price_tailors_chalk_3_pack = 1.25
stock_level_tailors_chalk_3_pack = 89
stock_price_tailors_chalk_3_pack = price_tailors_chalk_3_pack * stock_level_tailors_chalk_3_pack

# elastic_1m_25mm_wide
price_elastic_1m_25mm_wide = 0.75
stock_level_elastic_1m_25mm_wide = 167
stock_price_elastic_1m_25mm_wide = price_elastic_1m_25mm_wide * stock_level_elastic_1m_25mm_wide

# thimble_metal
price_thimble_metal = 1.00
stock_level_thimble_metal = 121
stock_price_thimble_metal = price_thimble_metal * stock_level_thimble_metal




# Total stock price calculation

total_stock_price = stock_price_sewing_thread_100m + stock_price_zipper_20cm + stock_price_wooden_buttons_pack_of_10 + stock_price_iron_on_interfacing_1m + stock_price_bias_binding_2_5m + stock_price_hook_and_eye_set_10_pairs + stock_price_seam_ripper + stock_price_tailors_chalk_3_pack + stock_price_elastic_1m_25mm_wide + stock_price_thimble_metal




# Print total stock price

print("Total stock price = £" + total_stock_price)
