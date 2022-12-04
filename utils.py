import pandas as pd
import numpy as np
import discord


def write_message_stats(name, poke_df):

    pokemon = get_poke_from_name(name, poke_df)
    
    if pokemon is None:
        return "No hay pokemon con nombre {}".format(name)

    name = pokemon['Name']
    ps = pokemon['HP']
    atack = pokemon['Attack']
    defense = pokemon['Defense']
    s_attack = pokemon['Sp. Atk']
    s_defense = pokemon['Sp. Def']
    vel = pokemon['Speed']

    msg = (discord.Embed(title="STATS",
                         description='```css\n{}\n```'.format(name),
                         color=discord.Color.blurple())
            .add_field(name="PS", value=ps)
            .add_field(name="Ataque", value=atack)
            .add_field(name="Defensa", value=defense)
            .add_field(name="Ataque Especial", value=s_attack)
            .add_field(name="Defensa Especial", value=s_defense)
            .add_field(name="Velocidad", value=vel))

    return msg

def write_message_evs(name, poke_df):

    pokemon = get_poke_from_name(name, poke_df)
    
    if pokemon is None:
        return "No hay pokemon con nombre {}".format(name)

    name = pokemon['Name']
    ps = pokemon['HP EV']
    atack = pokemon['Atk EV']
    defense = pokemon['Def EV']
    s_attack = pokemon['Sp. Atk EV']
    s_defense = pokemon['Sp. Def EV']
    vel = pokemon['Spe EV']


    msg = (discord.Embed(title="EV",
                         description='```css\n{}\n```'.format(name),
                         color=discord.Color.blurple())
            .add_field(name="PS", value=ps)
            .add_field(name="Ataque", value=atack)
            .add_field(name="Defensa", value=defense)
            .add_field(name="Ataque Especial", value=s_attack)
            .add_field(name="Defensa Especial", value=s_defense)
            .add_field(name="Velocidad", value=vel))

    return msg

def get_poke_from_name(name: str, poke_df: pd.DataFrame):

    mask = poke_df["Name"].str.lower() == name.lower()
    pos = np.flatnonzero(mask)
    if len(pos) < 1:
        return None
    info = poke_df.iloc[pos]
    return info