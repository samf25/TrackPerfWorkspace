from Gaudi.Configuration import *
from Configurables import EventDataSvc, ApplicationMgr, PodioInput, PodioOutput, k4DataSvc, InitializeDD4hep#, GeoSvc
from Configurables import ACTSMergeHitCollections, ACTSMergeRelationCollections, ACTSSeededCKFTrackingAlg
from Configurables import ACTSDuplicateRemoval, FilterTracksAlg, TrackTruthAlg, TrackPerfHistAlg
from Configurables import MarlinProcessorWrapper


# Read in Simulation Output Data
podioevent = k4DataSvc("EventDataSvc", input = "output_digi.edm4hep.root")
podioinput = PodioInput("PodioReader", 
	collections= [
	"VXDBarrelHits", "ITBarrelHits", "OTBarrelHits", 
	"VXDEndcapHits", "ITEndcapHits", "OTEndcapHits", 
	"VXDBarrelHitsRelations", "ITBarrelHitsRelations", 
	"OTBarrelHitsRelations", "VXDEndcapHitsRelations", 
	"ITEndcapHitsRelations", "OTEndcapHitsRelations", 
	"MCParticle"], OutputLevel = DEBUG)

# Feed in Dectector Geometry
detectors_to_use = '/isilon/export/home/sferrar2/Container/detector-simulation/geometries/MuColl_v1.0.1/MuColl_v1.xml'
#geoservice = GeoSvc("GeoSvc", detectors = detectors_to_use, OutputLevel = INFO)

# Initialize DD4hep
InitDD4hep = InitializeDD4hep("DD4hep Initializer",
                              DD4hepXMLFile = detectors_to_use,
                              EncodingString = "GlobalTrackerReadoutID")
InitDD4hep.OutputLevel = INFO

# Merge Track Collections into One Collection
MyMergeTracks = ACTSMergeHitCollections("MergeTrackHits",
                            InputCollection1 = "VXDBarrelHits",
                            InputCollection2 = "ITBarrelHits",
                            InputCollection3 = "OTBarrelHits",
                            InputCollection4 = "VXDEndcapHits",
                            InputCollection5 = "ITEndcapHits",
                            InputCollection6 = "OTEndcapHits",
                            OutputCollection = "MergedTrackerHits")
MyMergeTracks.OutputLevel = WARNING

# Merge Track Relation Collections into One Collection
MyMergeAssociations = ACTSMergeRelationCollections("MergeAssociations", 
                            InputCollection1 = "VXDBarrelHitsRelations",
                            InputCollection2 = "ITBarrelHitsRelations",
                            InputCollection3 = "OTBarrelHitsRelations",
                            InputCollection4 = "VXDEndcapHitsRelations",
                            InputCollection5 = "ITEndcapHitsRelations",
                            InputCollection6 = "OTEndcapHitsRelations",
                            OutputCollection = "MergedTrackerHitsRelations")
MyMergeAssociations.OutputLevel = WARNING

# Perform Reconstruction
MyCKFTracking = ACTSSeededCKFTrackingAlg("Reconstructor",
                            CKF_Chi2CutOff = 10,
                            CKF_NumMeasurementsCutOff = 1,
                            MatFile = "data/material-maps.json",
                            RunCKF = "True",
                            SeedFinding_CollisionRegion = 1,
                            SeedFinding_DeltaRMax = 80,
                            SeedFinding_DeltaRMin = 5,
                            SeedFinding_MinPt = 500,
                            SeedFinding_RMax = 150,
                            SeedFinding_RadLengthPerSeed = 0.1,
                            SeedFinding_SigmaScattering = 50,
                            SeedingLayers = ["13", "2", "13", "6", "13", "10", "13", "14", "14", "2", "14", "6", "14", "10", "14", "14", "15", "2", "15", "6", "15", "10", "15", "14"],
                            TGeoFile = "data/MuColl_v1.root",
                            OutputTrackCollectionName = "AllTracks",
                            OutputSeedCollectionName = "SeedTracks",
                            InputTrackerHitCollectionName = "MergedTrackerHits")
MyCKFTracking.OutputLevel = WARNING

# Remove Duplicate Tracks
MyTrackDeduper = ACTSDuplicateRemoval("Deduper",
                                InputTrackCollectionName = "AllTracks",
                                OutputTrackCollectionName = "DedupedTracks")
MyTrackDeduper.OutputLevel = WARNING

# Filter Tracks
MyTrackFilter = FilterTracksAlg("Filterer",
                            InputTrackCollectionName = "DedupedTracks",
                            MinPt = "0.5",
                            NHitsInner = "0",
                            NHitsOuter = "0",
                            NHitsTotal = "0",
                            NHitsVertex = "0",
                            OutputTrackCollectionName = "SiTracks")
MyTrackFilter.OutputLevel = WARNING

# Association Tracks with MCParticles
MyTrackTruth = TrackTruthAlg("AssociationCreator",
                            InputMCParticleCollectionName = "MCParticle",
                            OutputParticle2TrackRelationName = "MCParticle_SiTracks",
                            InputTrackCollectionName = "SiTracks",
                            InputTrackerHit2SimTrackerHitRelationName = "MergedTrackerHitsRelations")
MyTrackTruth.OutputLevel = WARNING

# Create Reconstruction Performance Histograms
MyTrackPerf = TrackPerfHistAlg("TrackPerformance",
                          InputMCParticleCollectionName = "MCParticle",
                          InputMCTrackRelationCollectionName = "MCParticle_SiTracks",
                          InputTrackCollectionName = "SiTracks")
MyTrackPerf.OutputLevel = WARNING

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
algList = [podioinput, InitDD4hep,
        MyMergeTracks, MyMergeAssociations, MyCKFTracking, 
      #  MyTrackDeduper, MyTrackFilter, MyTrackTruth, MyTrackPerf
]

THistSvc().Output = ["histos DATAFILE='histograms.root TYP='ROOT' OPT='RECREATE'"]
THistSvc().PrintAll = True
THistSvc().AutoSave = True
THistSvc().AutoFlush = True

# Run it
from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [podioevent],#, geoservice],
                OutputLevel=WARNING
              )
