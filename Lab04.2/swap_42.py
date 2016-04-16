def swap_keys_values(in_dict):
    out_dict = {}
    for k,v in in_dict.items():
        out_dict[v] = k

    return out_dict
