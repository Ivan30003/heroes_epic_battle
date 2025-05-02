def simple_attack(hit_function, team_one, team_two, who, target, damage_factor):
    if hit_function(who, target):
        damage = round(damage_factor * who.cur_attack / target.cur_defense)
        target.cur_health -= damage

def attack_headshot(hit_function, team_one, team_two, who, target, damage_factor):
    if hit_function(who, target):
        damage = round(damage_factor * 5.25 * who.cur_attack / target.cur_defense)
        target.cur_health -= damage

def massive_strike(hit_function, team_one, team_two, who, target, damage_factor):
    for hero in team_two:
        if hit_function(who, hero):
            damage = round(damage_factor * 2.5 * who.cur_attack / hero.cur_defense)
            hero.cur_health -= damage

attacks_dict = {'simple_attack': simple_attack, 'attack_headshot': attack_headshot, 
                'massive_strike': massive_strike}
