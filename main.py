import random
import sys
import time
from datetime import datetime, timedelta

import pydig as pydig

QUERY_URLS = [
    "g.live.com", "oneclient.sfx.ms", "a-ups-presence1-prod-azsc.japanwest.cloudapp.azure.com", "ocsp.entrust.net",
    "odc.officeapps.live.com", "ags.privatelink.msidentity.com", "vortex.data.microsoft.com",
    "global.asimov.events.data.trafficmanager.net", "860-ipv4e.clump.dprodmgd106.aa-rt.sharepoint.com",
    "presence.services.sfb.trafficmanager.net", "jmdadfssv.cloudapp.net", "artistsv.database.windows.net",
    "settings-prod-eus-1.eastus.cloudapp.azure.com", "teams-mira-afd.trafficmanager.net", "e1864.dscd.akamaiedge.net",
    "login.microsoftonline.com", "cxcs.cdn.office.net", "nexusrules.officeapps.live.com", "arc.trafficmanager.net",
    "content-signature-2.cdn.mozilla.net", "d2nxq2uap88usk.cloudfront.net"
]

THREATS_URLS = [
    "nofreezingmac.click", "donate.v2.xmrig.com", "tend-datingshere.com", "growyourownfood.academy",
    "www.growyourownfood.academy", "commons.host", "opencdn.jomodns.com"
]

QUERY_TYPES = ["A", "AAAA"]


def generate_query(query_per_minute, nameserver, run_minutes):
    all_domains = QUERY_URLS + THREATS_URLS

    current_date = datetime.now()
    end_date = datetime.now() + timedelta(minutes=run_minutes)

    resolver = pydig.Resolver(nameservers=[nameserver])

    count = 0
    while current_date < end_date and count < query_per_minute:
        resolver.query(random.choice(all_domains), random.choice(QUERY_TYPES))
        count += 1
        time.sleep(0.5)
        current_date = datetime.now()

    print(count)


if __name__ == '__main__':
    query_per_minute_arg = int(sys.argv[1])
    nameserver_arg = sys.argv[2]
    run_minutes_arg = int(sys.argv[3])

    # One pydig can generate 100 query per minute
    generate_query(query_per_minute_arg, nameserver_arg, run_minutes_arg)
