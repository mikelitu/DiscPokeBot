import pandas as pd
import numpy as np
import discord


def write_message_stats(name, poke_df):

  pokemon = get_poke_from_name(name, poke_df)

  if pokemon is None:
    return "No hay pokemon con nombre {}".format(name)

  name = pokemon['Name'].to_string(index=False)
  ps = int(pokemon['HP'])
  atack = int(pokemon['Attack'])
  defense = int(pokemon['Defense'])
  s_attack = int(pokemon['Sp. Atk'])
  s_defense = int(pokemon['Sp. Def'])
  vel = int(pokemon['Speed'])

  msg = (discord.Embed(title="{}".format(name),
                       description='```css\nSTATS\n```',
                       color=discord.Color.blurple())
        .add_field(name="PS", value=ps)
        .add_field(name="Ataque", value=atack)
        .add_field(name="Defensa", value=defense)
        .add_field(name="Ataque Especial", value=s_attack)
        .add_field(name="Defensa Especial", value=s_defense)
        .add_field(name="Velocidad", value=vel)
        )

  return msg


def write_message_evs(name, poke_df):

  pokemon = get_poke_from_name(name, poke_df)

  if pokemon is None:
    return "No hay pokemon con nombre {}".format(name)

  name = pokemon['Name'].to_string(index=False)
  ps = int(pokemon['HP EV'])
  atack = int(pokemon['Atk EV'])
  defense = int(pokemon['Def EV'])
  s_attack = int(pokemon['Sp. Atk EV'])
  s_defense = int(pokemon['Sp. Def EV'])
  vel = int(pokemon['Spe EV'])

  msg = (discord.Embed(title="{}".format(name),
                         description='```css\nEVs\n```',
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