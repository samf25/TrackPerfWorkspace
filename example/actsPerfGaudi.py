from Gaudi.Configuration import *
from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper, ACTSMergeHitCollections, ACTSMergeRelationCollections, ACTSSeedCKFTrackingAlg, ApplicationMgr, PodioInput, PodioOutput, k4DataSvc, GeoSvc

# Read in Simulation Output Data
podioevent = k4DataSvc("EventDataSvc", input = "output_sim.edm4hep.root")
podioinput = PodioInput("PodioReader", 
	collection = [
	"VBTrackerHits", "IBTrackerHits", "OBTrackerHits", 
	"VETrackerHits", "IETrackerHits", "OETrackerHits", 
	"VBTrackerHitsRelations", "IBTrackerHitsRelations", 
	"OBTrackerHitsRelations", "VETrackerHitsRelations", 
	"IETrackerHitsRelations", "OETrackerHitsRelations", 
	"MCParticle"], OutputLevel = DEBUG)

# Feed in Dectector Geometry
detectors_to_use = ['file:/isilon/export/home/sferrar2/Container/detector-simulation/geometries/MuColl_v1.0.1/MuColl_v1.xml',]
geoservice = GeoSvc("GeoSvc", detectors = detectors_to_use, OutputLevel = INFO)

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
algList = []
algList.append(podioinput)
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
                ExtSvc = [geoservice, podioevent],
                OutputLevel=WARNING
              )
