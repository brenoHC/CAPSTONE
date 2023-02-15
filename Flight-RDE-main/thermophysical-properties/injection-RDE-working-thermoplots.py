from fluprodia import FluidPropertyDiagram

fluids = ['N2O', 'ethylene', 'CO2']
Tlimits = {'ethylene':[-150 ,400],   'N2O':[-80 ,80],    'CO2':[-80 , 80],}
Slimits = {'ethylene':[-1200,4200],  'N2O':[-100,2100],  'CO2':[500 , 2200],}
Plimits = {'ethylene':[1e-3 ,400],   'N2O':[1   ,1000],  'CO2':[1   , 1000],}
hlimits = {'ethylene':[-200 ,700],   'N2O':[-10 ,450],   'CO2':[-10 , 450],}


if __name__=="__main__":
  for fluid in fluids:
    diagram1 = FluidPropertyDiagram(fluid=fluid)
    diagram1.set_unit_system(T='°C', h='kJ/kg', p='bar')
    diagram1.calc_isolines()
    diagram1.set_limits(x_min=Slimits[fluid][0], x_max=Slimits[fluid][1], y_min=Tlimits[fluid][0], y_max=Tlimits[fluid][1])
    diagram1.draw_isolines(diagram_type='Ts')
    diagram1.save(fluid+'_Ts_diagram.png', dpi=600)

    diagram2 = FluidPropertyDiagram(fluid=fluid)
    diagram2.set_unit_system(T='°C', h='kJ/kg', p='bar')
    diagram2.calc_isolines()
    diagram2.set_limits(x_min=hlimits[fluid][0], x_max=hlimits[fluid][1], y_min=Plimits[fluid][0], y_max=Plimits[fluid][1])
    diagram2.draw_isolines(diagram_type='logph')
    diagram2.save(fluid+'_logPh_diagram.png', dpi=600)
