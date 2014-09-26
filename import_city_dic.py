#!/usr/bin/python
# Andrew import_city_dic.py Version 1.0
# Created July 24, 2014
# Updated July 24, 2014

import os; os.chdir('/Users/andrewkoo/Workspace/Real_Estate_Investment/')


def import_city_dic():
    
    # Specify City Information
    citylist ={}
    
    citylist["Sunnyvale"] = {}
    citylist["Sunnyvale"]["Name"] = "Sunnyvale"
    citylist["Sunnyvale"]["location-URL"] = "Sunnyvale-CA/list/54626_rid/days_sort/37.464087,-121.982669,37.330236,-122.065571_rect/"
    
    citylist["Mountain View"] = {}
    citylist["Mountain View"]["Name"] = "Mountain_View"
    citylist["Mountain View"]["location-URL"] = "Mountain-View-CA/list/32999_rid/days_sort/37.450844,-122.044671,37.356541,-122.117861_rect/"
    
    citylist["Palo Alto"] = {}
    citylist["Palo Alto"]["Name"] = "Palo_Alto"
    citylist["Palo Alto"]["location-URL"] = "Palo-Alto-CA/list/26374_rid/days_sort/37.477838,-122.068867,37.285346,-122.202475_rect/"
    
    citylist["San Jose"] = {}
    citylist["San Jose"]["Name"] = "San_Jose"
    citylist["San Jose"]["location-URL"] = "San-Jose-CA/list/33839_rid/days_sort/37.469538,-121.589153,37.124493,-122.045664_rect/"
    
    citylist["Santa Clara"] = {}
    citylist["Santa Clara"]["Name"] = "Santa_Clara"
    citylist["Santa Clara"]["location-URL"] = "Santa-Clara-CA/list/13713_rid/days_sort/37.418925,-121.929735,37.322842,-122.006489_rect/"
    
    citylist["Milpitas"] = {}
    citylist["Milpitas"]["Name"] = "Milpitas"
    citylist["Milpitas"]["location-URL"] = "Milpitas-CA/list/39798_rid/days_sort/37.496692,-121.776516,37.396312,-121.931467_rect/"
    
    citylist["Campbell"] = {}
    citylist["Campbell"]["Name"] = "Campbell"
    citylist["Campbell"]["location-URL"] = "Campbell-CA/list/17272_rid/days_sort/37.303146,-121.922452,37.257055,-121.990883_rect/"
    
    citylist["Cupertino"] = {}
    citylist["Cupertino"]["Name"] = "Cupertino"
    citylist["Cupertino"]["location-URL"] = "Cupertino-CA/list/4281_rid/days_sort/37.341595,-121.996068,37.26471,-122.135758_rect/"
    
    citylist["Saratoga"] = {}
    citylist["Saratoga"]["Name"] = "Saratoga"
    citylist["Saratoga"]["location-URL"] = "Saratoga-CA/list/33874_rid/days_sort/37.300274,-121.989479,37.205001,-122.121637_rect/"
    
    citylist["Los Gatos"] = {}
    citylist["Los Gatos"]["Name"] = "Los_Gatos"
    citylist["Los Gatos"]["location-URL"] = "Los-Gatos-CA/list/19100_rid/days_sort/37.269143,-121.905748,37.194693,-121.99732_rect/"
    
    citylist["Los Altos"] = {}
    citylist["Los Altos"]["Name"] = "Los_Altos"
    citylist["Los Altos"]["location-URL"] = "Los-Altos-CA/list/39511_rid/days_sort/37.406339,-122.061771,37.329541,-122.129973_rect/"
    
    citylist["Menlo Park"] = {}
    citylist["Menlo Park"]["Name"] = "Menlo_Park"
    citylist["Menlo Park"]["location-URL"] = "Menlo-Park-CA/list/39748_rid/days_sort/37.507944,-122.128134,37.410754,-122.229771_rect/"
    
    citylist["Redwood City"] = {}
    citylist["Redwood City"]["Name"] = "Redwood City"
    citylist["Redwood City"]["location-URL"] = "Redwood-City-CA/list/20128_rid/days_sort/37.569534,-122.139774,37.446738,-122.288078_rect/"
    
    return citylist
		
if __name__ == '__main__':
	main()
