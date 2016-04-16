def swap_unique_keys_values(in_dict):
    
    out_dict = {}
    blacklist = set()
    for k,v in in_dict.items():
        
        if v in out_dict:
            blacklist.update([v])
            del out_dict[v]
            
        elif v not in blacklist:
            out_dict[v] = k
            

    return out_dict
