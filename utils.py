import streamlit as st


valid_category_map = {
        "Type": [None,'Person search', 'Person and Vehicle search', 'Vehicle search'],
        'Part of a policing operation':[None, True, False],
        'Gender':[None,'Male','Female','Other'],
        'Age range':[None,'18-24', '25-34', 'over 34', '10-17', 'under 10'],
        'Officer-defined ethnicity':[None,'Asian', 'White', 'Black', 'Other', 'Mixed'],  
    'Legislation':[None,'Misuse of Drugs Act 1971 (section 23)', 
                   'Police and Criminal Evidence Act 1984 (section 1)',
                   'Psychoactive Substances Act 2016 (s36(2))',
                   'Criminal Justice Act 1988 (section 139B)',
                   'Firearms Act 1968 (section 47)',
                   'Poaching Prevention Act 1862 (section 2)',
                   'Criminal Justice and Public Order Act 1994 (section 60)',
                   'Police and Criminal Evidence Act 1984 (section 6)',
                   'Wildlife and Countryside Act 1981 (section 19)',
                   'Psychoactive Substances Act 2016 (s37(2))',
                   'Aviation Security Act 1982 (section 27(1))',
                   'Protection of Badgers Act 1992 (section 11)',
                   'Crossbows Act 1987 (section 4)',
                   'Public Stores Act 1875 (section 6)',
                   'Customs and Excise Management Act 1979 (section 163)',
                   'Deer Act 1991 (section 12)',
                   'Conservation of Seals Act 1970 (section 4)'], 
    'Object of search':[None,'Controlled drugs',
                        'Offensive weapons',
                        'Stolen goods',
                        'Article for use in theft',
                        'Articles for use in criminal damage',
                        'Firearms',
                        'Anything to threaten or harm anyone',
                        'Crossbows',
                        'Evidence of offences under the Act',
                        'Fireworks',
                        'Psychoactive substances',
                        'Game or poaching equipment',
                        'Evidence of wildlife offences',
                        'Detailed object of search unavailable',
                        'Goods on which duty has not been paid etc.',
                        'Seals or hunting equipment'],
'station':[None,'devon-and-cornwall', 'dyfed-powys', 'derbyshire', 'bedfordshire', 'avon-and-somerset', 'cheshire', 'sussex', 'north-yorkshire', 'cleveland', 'merseyside', 'north-wales', 'wiltshire', 'norfolk', 'suffolk', 'thames-valley', 'durham', 'warwickshire', 'leicestershire', 'hertfordshire', 'cumbria', 'metropolitan', 'essex', 'south-yorkshire', 'surrey', 'staffordshire', 'northamptonshire', 'northumbria', 'city-of-london', 'nottinghamshire', 'gloucestershire', 'cambridgeshire', 'lincolnshire', 'btp', 'west-yorkshire', 'dorset', 'west-mercia', 'kent', 'hampshire', 'humberside', 'lancashire', 'greater-manchester', 'gwent']
}


