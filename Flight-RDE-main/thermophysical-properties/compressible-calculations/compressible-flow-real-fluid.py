import CoolProp.CoolProp as CP
import math

#h0 = h + 0.5*V^2
#m_dot = rho*V*A






if __name__ == "__main__":
    m_dot_target = 800  #Target mass flow rate, 800g/s
    fluid = "ethylene"  #Fluid
    P0    = 50          #Tank pressure in bar
    T0    = -10         #Tank temperature in oC
    
    h0 = CP.PropsSI('H','P',P0*1e5,'T',T0+273.15,fluid)
    s0 = CP.PropsSI('S','P',P0*1e5,'T',T0+273.15,fluid)
    print('h0 = ',h0,'[J/kg]')
    print('s0 = ',s0,'[J/kg.K]')
    
    #limit condition, cavitation
    #if you push the velocity too high, the pressure will drop
    #too low and the flow will cavitate.
    #You can find this limit by checking when, at constant entropy,
    #h1 = hf(s0)
    #hlim = CP.PropsSI('H','S',s0,'Q',0,fluid)
    #Vlim = math.sqrt(2*(h0-hlim))
    #clim = CP.PropsSI('A','S',s0,'Q',0,fluid)
    #print('Dont take h below h_lim = ', hlim,'[J/kg]')
    #print('At that enthalpy, the velocity is V_lim = ', Vlim, 'm/s')
    #print('At that enthalpy, the Mach number is M = ',Vlim/clim)
    
    #Pick an h under flow
    h1 = 0.98*h0
    #Calculate flow velocity from 1st law
    V1 = math.sqrt(2*(h0 - h1))
    print('Flow enthalpy is h1 = ',h1,'J/kg')
    print('flow velocity is V1 = ',V1,'m/s')
    
    #Calculate density and sound speed from equation of state
    #under isentropic conditions
    try:
      c1   = CP.PropsSI('A','S',s0,'H',h1,fluid)
      M1   = V1/c1
      print('M1 = ',M1)
    except ValueError:
      print('You probably picked an h1 value that is too low.')
      print('This results in a large pressure drop and cavitation.')
      print('The sound speed is ill-defined in a cavitating flow. You can still get a pipe diameter, though.')
    rho1 = CP.PropsSI('D','S',s0,'H',h1,fluid)
    #Calculate the required Area
    Apipe = 1e-3*m_dot_target/(rho1*V1) #m^2
    Dpipe = math.sqrt(4*Apipe/math.pi)  #m
    print('Required circular pipe diameter is Dpipe = ',100*Dpipe/2.54,'in.')
    
