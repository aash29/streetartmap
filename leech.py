import ingressAPI, math
import json


def get_tiles_per_edge(zoom):
    if zoom > 15:
        zoom = 15
    elif zoom < 3:
        zoom = 3
    else:
        pass
    return [1, 1, 1, 40, 40, 80, 80, 320, 1000, 2000, 2000, 4000, 8000, 16000, 16000, 32000][zoom]


def lng2tile(lng, tpe): # w
    return int((lng + 180) / 360 * tpe);

def lat2tile(lat, tpe): # j
    return int((1 - math.log(math.tan(lat * math.pi / 180) + 1 / math.cos(lat * math.pi / 180)) / math.pi) / 2 * tpe)

def tile2lng(x, tpe):
    return x / tpe * 360 - 180;

def tile2lat(y, tpe):
    n = math.pi - 2 * math.pi * y / tpe;
    return 180 / math.pi * math.atan(0.5 * (math.exp(n) - math.exp(-n)));

#mscLat=55.74795234569417
#mscLng=37.6393614550782

zoom=16

tpe=get_tiles_per_edge(zoom)

luLat=55.79546234499761
luLong=37.5500753590002


ylu=lat2tile(luLat,tpe)
xlu=lng2tile(luLong,tpe)

rlLat=55.57390656629218
rlLong=37.85511006825016

yrl=lat2tile(rlLat,tpe)
xrl=lng2tile(rlLong,tpe)



#xlu=9677
#ylu=5009

#xrl=xlu+5
#yrl=ylu-5



#cookie='csrftoken=FoVYy3YfFxFk7WINqjvOrwVY1mxcL9xC; ingress.intelmap.shflt=viz; ingress.intelmap.lat=55.75645370999264; ingress.intelmap.lng=37.17518909179695; ingress.intelmap.zoom=10; SACSID=~AJKiYcEXfA0EdQBfqtHr2AJw2cub6GTmR6OVQNAsie9AbC-C6Gv10t7Zm7cX4a6o-naqVf-3IKtakIFWWr-577aa2qHHywE4o3qr36oLwDVJroDJxpbLe7Cs4vvv7FF7uuQcVhnHzshvrM_wHekkC1WAf9xcJhuzgPNVptEjARzXYG-2ZpeEWdThqSymX4B__UTaTuZ1DUS6EYB3wsFvQnPkCtL6rq84ES0ybLt3neHMM1ahVFkF39GbO8RdSySPGOMaUxyQaqXrrmPMrmXR5h0vzsCjlWw94WhHm8E-BY4R0fMSkTcwa0k'
#cookie='csrftoken=FoVYy3YfFxFk7WINqjvOrwVY1mxcL9xC; ingress.intelmap.shflt=viz; ingress.intelmap.lat=55.555430161986514; ingress.intelmap.lng=37.8629601890107; ingress.intelmap.zoom=11; SACSID=~AJKiYcHww25IdAanJIRwjpeVWvvv7USuGNI4H3t6DiERinxnN_MsCRxNHe1gq4RBAuy7IbkI7AOyT4PKYvBeasN22NYHSzTSF03CEBWbru1G3g-OZ_iw4H7shV0qvVJeM2ucAJro6FLfebm6rn9mp18mwIDcEzhhqPSWN_cMlRY7PJ9TNQi09NCOQZAyBNmRY1RBcgUhSTftA1o3Mj_auhzxeT68Qg-fjmdG7qAfMOE4Y9k6VI1W4XCqJwNZXRlgZVRv8kcni2prr0xPEVDeQ-TwnJb7D0y5snQDOib1K4kJT2JHzOz8Y8I'
cookie='srftoken=o2Fv38SUOppaVyWwjguvrhAYMCb3ZYUiGM9ie0HGFfW5HSY6E50TwFkeYkkZyshr; sessionid=.eJyrViotTi3yTFGyUkpLSjM2NE62SDM0NTNPsTRW0gHLueYmZuYApRMTizOMLB3SQVy95PxcoHRBUX5ZZkpqEVDW3d_f3ccVKFacWlycmZ8XlloEooAyRkq1AEiNIAQ:1kv1Mh:3ROMtvyHmjuBCZFSB927srZxuOk; _ga=GA1.1.1104953344.1609434237; _gid=GA1.1.248469196.1609434237; _gat=1; ingress.intelmap.shflt=viz; _ncc=1; ingress.intelmap.lat=55.75113630401694; ingress.intelmap.lng=37.61714102309536; ingress.intelmap.zoom='+str(zoom)
login='aash29@gmail.com'
password="'njflhtcc"
artmap = ingressAPI.IntelMap(cookie,login,password)


with open('Moscow_portals_new.json', 'a', encoding='utf8') as f:

    def grabPortal(guid):
        if not (guid in plist.keys()):
            try:
                i=i+1
                print(i)
                p1=artmap.get_portal_details(guid)
                pd = dict()
                pd['name'] = p1['result'][8]
                pd['img'] = p1['result'][7]
                pd['lat'] = p1['result'][2]
                pd['long'] = p1['result'                            
                print(pd)
                plist[guid]=pd
            except Exception:
                pass
            json.dump(pd, f,ensure_ascii=False)
            f.write('\n')



    plist=dict()
    i=0
    for x in range(xlu,xrl):
        for y in range(ylu, yrl):
            print(x,y)
            #zoom_x_y_minlevel_maxlevel_health
            tile=str(zoom)+'_'+str(x)+'_'+str(y)+'_0_8_100'
            try:
                portals = artmap.get_entities([tile])

                #portals = artmap.get_entities(['11_2415_1251_1_8_100'])

                #with open('entities.json', 'w') as f1:
                #    json.dump(portals, f1)



                for p in portals['result']['map'][tile]['gameEntities']:
                    if (p[2][0]=='e'):
                        guid = p[2][2]
                        #print(guid)
                        if not (guid in plist.keys()):
                            try:
                                i=i+1
                                print(i)
                                p1=artmap.get_portal_details(guid)
                                pd = dict()
                                pd['name'] = p1['result'][8]
                                pd['img'] = p1['result'][7]
                                pd['lat'] = p1['result'][2]
                                pd['long'] = p1['result'][3]

                                print(pd)
                                plist[guid]=pd
                            except Exception:
                                pass
                            json.dump(pd, f,ensure_ascii=False)
                            f.write('\n')
                        guid = p[2][5]
                        #print(guid)
                        if not (guid in plist.keys()):
                            try:
                                i=i+1
                                print(i)
                                p1=artmap.get_portal_details(guid)
                                pd = dict()
                                pd['name'] = p1['result'][8]
                                pd['img'] = p1['result'][7]
                                pd['lat'] = p1['result'][2]
                                pd['long'] = p1['result'][3]

                                print(pd)
                                plist[guid]=pd
                            except Exception:
                                pass
                            json.dump(pd, f,ensure_ascii=False)
                            f.write('\n')



                    if (p[2][0]=='p'):
                        guid=p[0]
                        if not (guid in plist.keys()):
                            try:
                                i=i+1
                                print(i)
                                p1=artmap.get_portal_details(guid)
                                pd = dict()
                                pd['name'] = p1['result'][8]
                                pd['img'] = p1['result'][7]
                                pd['lat'] = p1['result'][2]
                                pd['long'] = p1['result'][3]

                                print(pd)
                                plist[guid]=pd
                            except Exception:
                                pass
                            json.dump(pd, f,ensure_ascii=False)
                            f.write('\n')
            
            except Exception:
                pass

    with open('Moscow_portals.json', 'w') as f:
        json.dump(plist, f)
        f.write('\n')


