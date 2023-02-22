numbers = [1,2,3,4,5]
result = list(filter(lambda x : x % 2 == 0, numbers))
print(result) # [2, 4]

matches = [
    {
    'home_team': 'Colombia',
    'away_team': 'Brasil',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
    },
    {
    'home_team': 'Chile',
    'away_team': 'Argentina',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
    },
    {
    'home_team': 'Argentina',
    'away_team': 'Perú',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
    }
]

result = list(filter(lambda team : team['home_team_result'] == 'Win', matches))
print(matches)
'''
[
    {
    'home_team': 'Colombia',
    'away_team': 'Brasil',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
    },
    {
    'home_team': 'Chile',
    'away_team': 'Argentina',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
    },
    {
    'home_team': 'Argentina',
    'away_team': 'Perú',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
    }
]
'''
print(len(matches)) # 3
print(len(result)) # 2
print(result)
'''
[
    {
    'home_team': 'Colombia',
    'away_team': 'Brasil',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
    },
    {
    'home_team': 'Argentina',
    'away_team': 'Perú',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
    }
]
'''