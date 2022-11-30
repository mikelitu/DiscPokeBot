def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def get_evs():

    with open("evs_poke.txt") as file_object:
        lines = file_object.readlines()

    new_lines = lines[1:]
    headers = get_headers(new_lines)
    new_lines = new_lines[7:]
    poke_list = []
    
    for poke_lines in chunker(new_lines, 10):
        pokemon = get_pokemon(poke_lines, headers)
        poke_list.append(pokemon)

    return poke_list

def get_headers(lines):

    header_lines = lines[:7]
    headers = []
    
    for header_line in header_lines:
        splitted = header_line.split('|')
        further_split = splitted[1].split('\n')
        header = further_split[0][1:]
        headers.append(header)
    
    return headers

def get_pokemon(lines, headers):
    imp_lines = lines[1:]
    info = {}

    for i, line in enumerate(imp_lines):

        if i == 0:
            splitted = line.split(' ')
            further_split = splitted[1].split('\n')
            poke_num = further_split[0]
            info['N Pokedex'] = poke_num
        
        elif i == 1:
            splitted = line.split('{')
            further_split = splitted[2].split('}')
            poke_name = further_split[0][2:]
            info['Name'] = poke_name
        
        else:
            splitted = line.split(' ')
            further_split = splitted[1].split('\n')
            stat = further_split[0]
            info[headers[i-2]] = stat
        
    return info

def get_pokemon_from_name(name, poke_list):

    i = 0

    while i < len(poke_list):

        if name == poke_list[i]['Name'].lower():
            return poke_list[i]
        
        i += 1
    
    return None

def get_pokemon_from_idx(idx, poke_list):
    if idx-1 > len(poke_list) or idx <= 0:
        return None
    return poke_list[idx-1]


def write_message(name, poke_list):

    if name.isnumeric():
        pokemon = get_pokemon_from_idx(int(name), poke_list)
    else:
        pokemon = get_pokemon_from_name(name, poke_list)
    
    if pokemon is None:
        if name.isnumeric():
            return "There is no Pokemon with pokedex number {}".format(name)
        else:
            return "There is no pokemon with name {}".format(name)

    name = pokemon['Name']
    num = pokemon['N Pokedex']
    exp = pokemon['Exp. base']
    ps = pokemon['PS']
    atack = pokemon['Ataque']
    defense = pokemon['Defensa']
    s_attack = pokemon['Ataque esp.']
    s_defense = pokemon['Defensa esp.']
    vel = pokemon['Velocidad']

    msg = "NAME: {}\nPOKEDEX: {}\nBASE EXP.: {}\nPS: {}\nATTACK: {}\nDEFENSE: {}\nESP. ATTACK: {}\nESP. DEFENSE: {}\nSPEED: {}\n".format(
        name, num, exp, ps, atack, defense, s_attack, s_defense, vel
    )

    return msg
