import CoolProp.CoolProp as CP
fluid = 'Ethylene'

temp = 263.15 # K #-10degrees c
pres = 5000000 # Pa #50bar

# Specify the temperature and pressure to fix the state
density = CP.PropsSI('D', 'T', temp, 'P', pres, fluid)
phase = CP.PhaseSI('T', temp, 'P', pres, fluid)

print(f'Density: {density: .2f} kg/m^3')
print(f'Phase: {phase}')



