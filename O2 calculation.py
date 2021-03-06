#mass_13x=2  #mass of 13x,kg
oxy_production=2.5  #O2 production,L/min
mass_13x=oxy_production/1.5   #mass of 13x,kg
vol_13x=mass_13x/1130     #volume of 13x,L
flw_rate=0.00036     #flow rate,m3/s
spr_vel=0.1         #superficial velocity,m/s
vol_col=vol_13x/0.65  #
area_col=flw_rate/spr_vel  #area of column,m2
dia_col=(4*area_col/3.14)**(0.5)  #radius of column,m
length_col=vol_col/(3.14*area_col) #length of column,m
print("Mass of zeolite(in kg):",mass_13x)
print("Volume of column(in m3):",vol_col)
print("Area of column(in m2):",area_col)
print("Diameter of column(in inch):",39.37*dia_col)
print("Length of column(in inch):",39.37*length_col)
print("L/D ratio of column:",length_col/dia_col)
