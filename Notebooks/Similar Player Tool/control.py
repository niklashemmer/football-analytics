Templates = {"striker": "striker",
            "centre_back": "centre_back",
            "attacking_mid": "Attacking Midfielder",
            "defensive_mid": "Defensive Midfielder",
            "full_back": "Full Back"
            }

Templates1 = [
    dict(label="Striker", value=4),
    dict(label="Centre Back", value=0),
    dict(label="Attacking Midfielder", value=3),
    dict(label="Defensive Midfielder", value=2),
    dict(label="Full Back", value=1)
]

all = [
    "ID",
    "Age",
    "Comp",
    "90s",
    "Player Role",
    #"cluster_gmm_new",
    "Similarity",
    # SECTION ATTACKING!!!
    # "Goals",
    "npxG",
    # "np:G-xG",
    "npxG/Sh",
    "Sh",
    # "Avg Shot Dist",
    "Sh/Touch",
    "xA",
    #"SCA",
    # "SCA Pass",
    # "SCA Dribb",
    # # Insert Percentage of touches in each part
    "Dribb Att",
    "Dribb Succ",
    "Rec Prog",
    "Fld",
    "Turnover",
    # #"Dribb Succ %",
    # #"Dribb #Player",
    # "Mis",
    # "Dispossessed",
    # "Rec Prog Passes",
    # "Assists",
    # "xA",
    # SECTION PASSING!!!
    #"Touches",
    #"Carries TotDist",
    "Carries PrgDist",
    "Carries Prog",
    "Carries 1/3",
    "Carries PA",
    "Pass TotDist",
    "Pass PrgDist",
    "Pass Prog",
    "Pass 1/3",
    "Pass PA",
    "Pass Cmp%",
    #"1/3 Entry",
    #"PA",
    "KP",
    "Crs",
    "Crs PA",
    # SECTION DEFENDING!!!
    "Tkl",
    "TklW",
    "Dribb Tkl Att",
    "Dribb Tkl%",
    "Press",
    "Press Succ",
    "Blocks",
    "Int",
    "Clr",
    "Fls",
    "Recov",
    "AerWon",
    "AerWon%",
    "Aer",
]

all_pp = [
    "ID",
    "Age",
    "Comp",
    "90s",
    "Player Role",
    #"cluster_gmm_new",
    #"Similarity",
    # SECTION ATTACKING!!!
    # "Goals",
    "npxG",
    # "np:G-xG",
    "npxG/Sh",
    "Sh",
    # "Avg Shot Dist",
    "Sh/Touch",
    "xA",
    #"SCA",
    # "SCA Pass",
    # "SCA Dribb",
    # # Insert Percentage of touches in each part
    "Dribb Att",
    "Dribb Succ",
    "Rec Prog",
    "Fld",
    "Turnover",
    # #"Dribb Succ %",
    # #"Dribb #Player",
    # "Mis",
    # "Dispossessed",
    # "Rec Prog Passes",
    # "Assists",
    # "xA",
    # SECTION PASSING!!!
    #"Touches",
    #"Carries TotDist",
    "Carries PrgDist",
    "Carries Prog",
    "Carries 1/3",
    "Carries PA",
    "Pass TotDist",
    "Pass PrgDist",
    "Pass Prog",
    "Pass 1/3",
    "Pass PA",
    "Pass Cmp%",
    #"1/3 Entry",
    #"PA",
    "KP",
    "Crs",
    "Crs PA",
    # SECTION DEFENDING!!!
    "Tkl",
    "TklW",
    "Dribb Tkl Att",
    "Dribb Tkl%",
    "Press",
    "Press Succ",
    "Blocks",
    "Int",
    "Clr",
    "Fls",
    "Recov",
    "AerWon",
    "AerWon%",
    "Aer",
]

Metrics = {
    "npxG":"npxG",
    # "np:G-xG",
    "npxG/Sh":"npxG/Sh",
    "Sh":"Sh",
    # "Avg Shot Dist",
    "Sh/Touch":"Sh/Touch",
    "xA":"xA",
    # "SCA",
    # "SCA Pass",
    # "SCA Dribb",
    # # Insert Percentage of touches in each part
    "Dribb Att":"Dribb Att",
    "Dribb Succ":"Dribb Succ",
    "Rec Prog":"Rec Prog",
    "Fld":"Fld",
    "Turnover":"Turnover",
    # #"Dribb Succ %",
    # #"Dribb #Player",
    # "Mis",
    # "Dispossessed",
    # "Rec Prog Passes",
    # "Assists",
    # "xA",
    # SECTION PASSING!!!
    # "Touches",
    # "Carries TotDist",
    "Carries PrgDist":"Carries PrgDist",
    "Carries Prog":"Carries Prog",
    "Carries 1/3":"Carries 1/3",
    "Carries PA":"Carries PA",
    "Pass TotDist":"Pass TotDist",
    "Pass PrgDist":"Pass PrgDist",
    "Pass Prog":"Pass Prog",
    "Pass 1/3":"Pass 1/3",
    "Pass PA":"Pass PA",
    "Pass Cmp%":"Pass Cmp%",
    # "1/3 Entry",
    # "PA",
    "KP":"KP",
    "Crs":"Crs",
    "Crs PA":"Crs PA",
    # SECTION DEFENDING!!!
    "Tkl":"Tkl",
    "TklW":"TklW",
    "Dribb Tkl Att":"Dribb Tkl Att",
    "Dribb Tkl%":"Dribb Tkl%",
    "Press":"Press",
    "Press Succ":"Press Succ",
    "Blocks":"Blocks",
    "Int":"Int",
    "Clr":"Clr",
    "Fls":"Fls",
    "Recov":"Recov",
    "AerWon":"AerWon",
    "AerWon%":"AerWon%",
    "Aer":"Aer",
}
