import json
luLat=55795462
luLong=37550075

rlLat=55573906
rlLong=37855110


with open('Moscow_portals.json', 'r', encoding='utf8') as f:
	with open('Moscow_portals_cut.json', 'w') as fo:
	    
		data = json.load(f)

		for id,portal in data.items():
			out=dict()
			lat = portal['lat']
			lon = portal['long']
			if (rlLat<lat) and (lat<luLat) and (luLong < lon) and (lon<rlLong):
				out=portal
				out['id']=id
				json.dump(out, fo,ensure_ascii=False)
				fo.write('\n')