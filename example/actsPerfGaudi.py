from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper, ACTSMergeTrackHitPlaneCollections, ACTSMergeMCRecoParticleAssociationCollections, ACTSSeedCKFTrackingAlg
from k4MarlinWrapper.parseConstants import *
algList = []
evtsvc = EventDataSvc()


CONSTANTS = {
}

parseConstants(CONSTANTS)

read = LcioEvent()
read.OutputLevel = WARNING
read.Files = ["output_digi.slcio"]
algList.append(read)

Config = MarlinProcessorWrapper("Config")
Config.OutputLevel = WARNING
Config.ProcessorType = "CLICRecoConfig"
Config.Parameters = {
                     "Overlay": ["False"],
                     "OverlayChoices": ["False", "BIB"],
                     "Tracking": ["ACTS"],
                     "TrackingChoices": ["Truth", "Conformal", "ACTS"],
                     "VertexUnconstrained": ["OFF"],
                     "VertexUnconstrainedChoices": ["ON", "OFF"]
                     }

EventNumber = MarlinProcessorWrapper("EventNumber")
EventNumber.OutputLevel = WARNING
EventNumber.ProcessorType = "Statusmonitor"
EventNumber.Parameters = {
                          "HowOften": ["1"]
                          }

MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = WARNING
MyAIDAProcessor.ProcessorType = "AIDAProcessor"
MyAIDAProcessor.Parameters = {
                              "Compress": ["1"],
                              "FileName": ["histograms"],
                              "FileType": ["root"]
                              }

InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = WARNING
InitDD4hep.ProcessorType = "InitializeDD4hep"
InitDD4hep.Parameters = {
                         "DD4hepXMLFile": ["/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.3.1/lcgeo-0.18.1-rv5ol74iupibxoku3ktvpgjseph6nj5k/share/lcgeo/compact/MuColl/MuColl_v1/MuColl_v1.xml"],
                         "EncodingStringParameterName": ["GlobalTrackerReadoutID"]
                         }

VXDBarrelDigitiser = MarlinProcessorWrapper("VXDBarrelDigitiser")
VXDBarrelDigitiser.OutputLevel = WARNING
VXDBarrelDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDBarrelDigitiser.Parameters = {
                                 "CorrectTimesForPropagation": ["true"],
                                 "IsStrip": ["false"],
                                 "ResolutionT": ["0.03"],
                                 "ResolutionU": ["0.005"],
                                 "ResolutionV": ["0.005"],
                                 "SimTrackHitCollectionName": ["VertexBarrelCollection"],
                                 "SimTrkHitRelCollection": ["VBTrackerHitsRelations"],
                                 "SubDetectorName": ["Vertex"],
                                 "TimeWindowMax": ["0.15"],
                                 "TimeWindowMin": ["-0.09"],
                                 "TrackerHitCollectionName": ["VBTrackerHits"],
                                 "UseTimeWindow": ["true"]
                                 }

VXDEndcapDigitiser = MarlinProcessorWrapper("VXDEndcapDigitiser")
VXDEndcapDigitiser.OutputLevel = WARNING
VXDEndcapDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDEndcapDigitiser.Parameters = {
                                 "CorrectTimesForPropagation": ["true"],
                                 "IsStrip": ["false"],
                                 "ResolutionT": ["0.03"],
                                 "ResolutionU": ["0.005"],
                                 "ResolutionV": ["0.005"],
                                 "SimTrackHitCollectionName": ["VertexEndcapCollection"],
                                 "SimTrkHitRelCollection": ["VETrackerHitsRelations"],
                                 "SubDetectorName": ["Vertex"],
                                 "TimeWindowMax": ["0.15"],
                                 "TimeWindowMin": ["-0.09"],
                                 "TrackerHitCollectionName": ["VETrackerHits"],
                                 "UseTimeWindow": ["true"]
                                 }

InnerPlanarDigiProcessor = MarlinProcessorWrapper("InnerPlanarDigiProcessor")
InnerPlanarDigiProcessor.OutputLevel = WARNING
InnerPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerPlanarDigiProcessor.Parameters = {
                                       "CorrectTimesForPropagation": ["true"],
                                       "IsStrip": ["false"],
                                       "ResolutionT": ["0.06"],
                                       "ResolutionU": ["0.007"],
                                       "ResolutionV": ["0.090"],
                                       "SimTrackHitCollectionName": ["InnerTrackerBarrelCollection"],
                                       "SimTrkHitRelCollection": ["IBTrackerHitsRelations"],
                                       "SubDetectorName": ["InnerTrackers"],
                                       "TimeWindowMax": ["0.3"],
                                       "TimeWindowMin": ["-0.18"],
                                       "TrackerHitCollectionName": ["IBTrackerHits"],
                                       "UseTimeWindow": ["true"]
                                       }

InnerEndcapPlanarDigiProcessor = MarlinProcessorWrapper("InnerEndcapPlanarDigiProcessor")
InnerEndcapPlanarDigiProcessor.OutputLevel = WARNING
InnerEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerEndcapPlanarDigiProcessor.Parameters = {
                                             "CorrectTimesForPropagation": ["true"],
                                             "IsStrip": ["false"],
                                             "ResolutionT": ["0.06"],
                                             "ResolutionU": ["0.007"],
                                             "ResolutionV": ["0.090"],
                                             "SimTrackHitCollectionName": ["InnerTrackerEndcapCollection"],
                                             "SimTrkHitRelCollection": ["IETrackerHitsRelations"],
                                             "SubDetectorName": ["InnerTrackers"],
                                             "TimeWindowMax": ["0.3"],
                                             "TimeWindowMin": ["-0.18"],
                                             "TrackerHitCollectionName": ["IETrackerHits"],
                                             "UseTimeWindow": ["true"]
                                             }

OuterPlanarDigiProcessor = MarlinProcessorWrapper("OuterPlanarDigiProcessor")
OuterPlanarDigiProcessor.OutputLevel = WARNING
OuterPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterPlanarDigiProcessor.Parameters = {
                                       "CorrectTimesForPropagation": ["true"],
                                       "IsStrip": ["false"],
                                       "ResolutionT": ["0.06"],
                                       "ResolutionU": ["0.007"],
                                       "ResolutionV": ["0.090"],
                                       "SimTrackHitCollectionName": ["OuterTrackerBarrelCollection"],
                                       "SimTrkHitRelCollection": ["OBTrackerHitsRelations"],
                                       "SubDetectorName": ["OuterTrackers"],
                                       "TimeWindowMax": ["0.3"],
                                       "TimeWindowMin": ["-0.18"],
                                       "TrackerHitCollectionName": ["OBTrackerHits"],
                                       "UseTimeWindow": ["true"]
                                       }

OuterEndcapPlanarDigiProcessor = MarlinProcessorWrapper("OuterEndcapPlanarDigiProcessor")
OuterEndcapPlanarDigiProcessor.OutputLevel = WARNING
OuterEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterEndcapPlanarDigiProcessor.Parameters = {
                                             "CorrectTimesForPropagation": ["true"],
                                             "IsStrip": ["false"],
                                             "ResolutionT": ["0.06"],
                                             "ResolutionU": ["0.007"],
                                             "ResolutionV": ["0.090"],
                                             "SimTrackHitCollectionName": ["OuterTrackerEndcapCollection"],
                                             "SimTrkHitRelCollection": ["OETrackerHitsRelations"],
                                             "SubDetectorName": ["OuterTrackers"],
                                             "TimeWindowMax": ["0.3"],
                                             "TimeWindowMin": ["-0.18"],
                                             "TrackerHitCollectionName": ["OETrackerHits"],
                                             "UseTimeWindow": ["true"]
                                             }

# Convert LCIO Output to EDM4HEP

# Merge Track Collections into One Collection
MyMergeTracks = ACTSMergeTrackHitPlaneCollections()
MyMergeTracks.OutputLevel = WARNING
MyMergeTracks.Parameters = {
                            "InputCollection1": "VBTrackerHits",
                            "InputCollection1": "IBTrackerHits",
                            "InputCollection1": "OBTrackerHits",
                            "InputCollection1": "VETrackerHits",
                            "InputCollection1": "IETrackerHits",
                            "InputCollection1": "OETrackerHits",
                            "OutputCollection": "MergedTrackerHits"
                            }

# Merge Track Relation Collections into One Collection
MyMergeAssociations = ACTSMergeMCRecoParticleAssociationCollections()
MyMergeAssociations.OutputLevel = WARNING
MyMergeAssociations.Parameters = {
                                  "InputCollection1": "VBTrackerHitsRelations",
                                  "InputCollection1": "IBTrackerHitsRelations",
                                  "InputCollection1": "OBTrackerHitsRelations",
                                  "InputCollection1": "VETrackerHitsRelations",
                                  "InputCollection1": "IETrackerHitsRelations",
                                  "InputCollection1": "OETrackerHitsRelations",
                                  "OutputCollection": "MergedTrackerHitsRelations" 
                                  }

# Perform Reconstruction
MyCKFTracking = ACTSSeedCKFTrackingAlg()
MyCKFTracking.OutputLevel = WARNING
MyCKFTracking.Parameters = {
                            "CKF_Chi2CutOff": "10",
                            "CKF_NumMeasurementsCutOff": "1",
                            "MatFile": "data/material-maps.json",
                            "RunCKF": "True",
                            "SeedFinding_CollisionRegion": "1",
                            "SeedFinding_DeltaRMax": "80",
                            "SeedFinding_DeltaRMin": "5",
                            "SeedFinding_MinPt": "500",
                            "SeedFinding_RMax": "150",
                            "SeedFinding_RadLengthPerSeed": "0.1",
                            "SeedFinding_SigmaScattering": "50",
                            "SeedingLayers": ["13", "2", "13", "6", "13", "10", "13", "14", "14", "2", "14", "6", "14", "10", "14", "14", "15", "2", "15", "6", "15", "10", "15", "14"],
                            "TGeoFile": "data/MuColl_v1.root",
                            "OutputTrackCollectionName": "AllTracks",
                            "OutputSeedCollectionName": "SeedTracks",
                            "InputTrackerHitCollectionNames": "MergedTrackerHits"
                            }

# Remove Duplicate Tracks
MyTrackDeduper = ACTSDuplicateRemoval()
MyTrackDeduper.OutputLevel = WARNING
MyTrackDeduper.Parameters = {
                             "InputTrackCollectionName": "AllTracks",
                             "OutputTrackCollectionName": "DedupedTracks"
                             }

# Filter Tracks
MyTrackFilter = FilterTracksAlg()
MyTrackFilter.OutputLevel = WARNING
MyTrackFilter.Parameters = {
                            "InputTrackCollectionName": "DedupedTracks",
                            "MinPt": "0.5",
                            "NHitsInner": "0",
                            "NHitsOuter": "0",
                            "NHitsTotal": "0",
                            "NHitsVertex": "0",
                            "OutputTrackCollectionName": "SiTracks"
                            }

# Association Tracks with MCParticles
MyTrackTruth = TrackTruthAlg()
MyTrackTruth.OutputLevel = WARNING
MyTrackTruth.Parameters = {
                           "InputMCParticleCollectionName": "MCParticle",
                           "OutputParticle2TrackRelationName": "MCParticle_SiTracks",
                           "InputTrackCollectionName": "SiTracks",
                           "InputTrackerHit2SimTrackerHitRelationName": "MergedTrackerHitsRelations"
                           }

# Create Reconstruction Performance Histograms
MyTrackPerf = TrackPerfHistAlg()
MyTrackPerf.OutputLevel = WARNING
MyTrackPerf.Parameters = {
                          "InputMCParticleCollectionName": "MCParticle",
                          "InputMCTrackRelationCollectionName": "MCParticle_SiTracks",
                          "InputTrackCollectionName": "SiTracks"
                          }

#MyOutput = MarlinProcessorWrapper("MyOutput")
#MyOutput.OutputLevel = WARNING
#MyOutput.ProcessorType = "LCTuple"
#MyOutput.Parameters = {
#                       "LCRelationCollections": ["MCParticle_SiTracks"],
#                       "LCRelationPrefixes": ["mc2tr"],
#                       "MCParticleCollection": ["MCParticle"],
#                       "TrackCollection": ["SiTracks"]
#                       }

# Build Algorithm
algList.append(MyAIDAProcessor)
algList.append(EventNumber)
algList.append(Config)
algList.append(InitDD4hep)
algList.append(VXDBarrelDigitiser)
algList.append(VXDEndcapDigitiser)
algList.append(InnerPlanarDigiProcessor)
algList.append(InnerEndcapPlanarDigiProcessor)
algList.append(OuterPlanarDigiProcessor)
algList.append(OuterEndcapPlanarDigiProcessor)
algList.append(MyCKFTracking)
algList.append(MyTrackDeduper)
algList.append(MyTrackFilter)
algList.append(MyTrackTruth)
algList.append(MergeHits)
algList.append(MyTrackPerf)
#algList.append(MyOutput)

# Run it
from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc],
                OutputLevel=WARNING
              )
