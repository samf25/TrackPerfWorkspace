import os
from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4FWCore.parseArgs import parser
from k4FWCore import IOSvc
parser.add_argument(
    "--DD4hepXMLFile",
    help="Compact detector description file",
    type=str,
    default=os.environ.get("MUCOLL_GEO", ""),
)

parser.add_argument(
    "--MatFile",
    help="Material maps file for tracking",
    type=str,
    default="/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/actstracking-1.3.1-zxsyo4d3u3cfzn55k4yyigif7jsyzshc/share/ACTSTracking/data/material-maps.json",
)

parser.add_argument(
    "--TGeoFile",
    help="TGeometry file for tracking",
    type=str,
    default="/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/actstracking-1.3.1-zxsyo4d3u3cfzn55k4yyigif7jsyzshc/share/ACTSTracking/data/MuColl_v1.root",
)

the_args = parser.parse_known_args()[0]

algList = []
evtsvc = EventDataSvc("EventDataSvc")

# Declare the IOSvc and pass the input to it
svc = IOSvc("IOSvc")
svc.Input = "output_reco.edm4hep.root"
svc.Output = "output_text.edm4hep.root"

from Configurables import EDM4hep2LcioTool, Lcio2EDM4hepTool
edm4hep2LcioConv = EDM4hep2LcioTool("EDM4hep2Lcio")
edm4hep2LcioConv.OutputLevel = DEBUG
lcio2edm4hepConv = Lcio2EDM4hepTool("Lcio2EDM4hep")
lcio2edm4hepConv.OutputLevel = DEBUG
edm4hep2LcioConv1 = EDM4hep2LcioTool("EDM4hep2Lcio")

from Configurables import GeoSvc
geoservice = GeoSvc("GeoSvc")
geoservice.detectors = [the_args.DD4hepXMLFile]
geoservice.OutputLevel = WARNING
geoservice.EnableGeant4Geo = False

# Remove Duplicate Tracks
from Configurables import ACTSDuplicateRemoval
MyTrackDeduper = ACTSDuplicateRemoval("Deduper",
                                InputTrackCollectionName = ["AllTracks"],
                                OutputTrackCollectionName = ["DedupedTracks"])
MyTrackDeduper.OutputLevel = WARNING

EventNumber = MarlinProcessorWrapper("EventNumber")
EventNumber.OutputLevel = INFO
EventNumber.EDM4hep2LcioTool = edm4hep2LcioConv
EventNumber.ProcessorType = "Statusmonitor"
EventNumber.Parameters = {
                          "HowOften": ["1"]
                          }
THistSvc().Output = ["histos DATAFILE='nhits6_histograms.root' TYP='ROOT' OPT='RECREATE'"]
THistSvc().PrintAll = True
THistSvc().AutoSave = True
THistSvc().AutoFlush = True

algList.append(MyTrackDeduper)
algList.append(EventNumber)

from k4FWCore import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc, geoservice],
                OutputLevel=INFO
              )
