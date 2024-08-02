#Thu Aug  1 10:38:14 2024"""Automatically generated. DO NOT EDIT please"""
import sys
if sys.version_info >= (3,):
    # Python 2 compatibility
    long = int
from GaudiKernel.DataHandle import DataHandle
from GaudiKernel.Proxy.Configurable import *

class ACTSDuplicateRemoval( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : set(),
    'ExtraOutputs' : set(),
    'OutputLevel' : 0,
    'Enable' : True,
    'ErrorMax' : 1,
    'AuditAlgorithms' : False,
    'AuditInitialize' : False,
    'AuditReinitialize' : False,
    'AuditRestart' : False,
    'AuditExecute' : False,
    'AuditFinalize' : False,
    'AuditStart' : False,
    'AuditStop' : False,
    'Timeline' : True,
    'MonitorService' : 'MonitorSvc',
    'RegisterForContextService' : False,
    'Cardinality' : 0,
    'NeededResources' : [  ],
    'Blocking' : False,
    'FilterCircularDependencies' : True,
    'InputTrackCollectionName' : DataHandle('TruthTracks', 'R', 'edm4hep::TrackCollection'),
    'OutputTrackCollectionName' : DataHandle('DedupedTruthTracks', 'W', 'edm4hep::TrackCollection'),
  }
  _propertyDocDct = { 
    'ExtraInputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'ExtraOutputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'OutputLevel' : """ output level [Gaudi::Algorithm] """,
    'Enable' : """ should the algorithm be executed or not [Gaudi::Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Gaudi::Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Gaudi::Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Gaudi::Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Gaudi::Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Gaudi::Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Gaudi::Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Gaudi::Algorithm] """,
    'AuditStart' : """ trigger auditor on start() [Gaudi::Algorithm] """,
    'AuditStop' : """ trigger auditor on stop() [Gaudi::Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Gaudi::Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Gaudi::Algorithm] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Gaudi::Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Gaudi::Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Gaudi::Algorithm] """,
    'Blocking' : """ if algorithm invokes CPU-blocking system calls (offloads computations to accelerators or quantum processors, performs disk or network I/O, is bound by resource synchronization, etc) [Gaudi::Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Gaudi::Algorithm] """,
    'InputTrackCollectionName' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::TrackCollection>,std::tuple<edm4hep::TrackCollection>,Gaudi::Functional::Traits::use_<> >] """,
    'OutputTrackCollectionName' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::TrackCollection>,std::tuple<edm4hep::TrackCollection>,Gaudi::Functional::Traits::use_<> >] """,
  }
  __declaration_location__ = 'ACTSDuplicateRemoval.cxx:47'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(ACTSDuplicateRemoval, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'ACTSTrackingPlugins'
  def getType( self ):
      return 'ACTSDuplicateRemoval'
  pass # class ACTSDuplicateRemoval

class ACTSMergeHitCollections( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : set(),
    'ExtraOutputs' : set(),
    'OutputLevel' : 0,
    'Enable' : True,
    'ErrorMax' : 1,
    'AuditAlgorithms' : False,
    'AuditInitialize' : False,
    'AuditReinitialize' : False,
    'AuditRestart' : False,
    'AuditExecute' : False,
    'AuditFinalize' : False,
    'AuditStart' : False,
    'AuditStop' : False,
    'Timeline' : True,
    'MonitorService' : 'MonitorSvc',
    'RegisterForContextService' : False,
    'Cardinality' : 0,
    'NeededResources' : [  ],
    'Blocking' : False,
    'FilterCircularDependencies' : True,
    'InputCollection6' : DataHandle('Collection6', 'R', 'DataWrapper<edm4hep::TrackerHitPlaneCollection>'),
    'InputCollection5' : DataHandle('Collection5', 'R', 'DataWrapper<edm4hep::TrackerHitPlaneCollection>'),
    'InputCollection4' : DataHandle('Collection4', 'R', 'DataWrapper<edm4hep::TrackerHitPlaneCollection>'),
    'InputCollection3' : DataHandle('Collection3', 'R', 'DataWrapper<edm4hep::TrackerHitPlaneCollection>'),
    'InputCollection2' : DataHandle('Collection2', 'R', 'DataWrapper<edm4hep::TrackerHitPlaneCollection>'),
    'InputCollection1' : DataHandle('Collection1', 'R', 'DataWrapper<edm4hep::TrackerHitPlaneCollection>'),
    'OutputCollection' : DataHandle('MergedCollection', 'W', 'edm4hep::TrackerHitPlaneCollection'),
  }
  _propertyDocDct = { 
    'ExtraInputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'ExtraOutputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'OutputLevel' : """ output level [Gaudi::Algorithm] """,
    'Enable' : """ should the algorithm be executed or not [Gaudi::Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Gaudi::Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Gaudi::Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Gaudi::Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Gaudi::Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Gaudi::Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Gaudi::Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Gaudi::Algorithm] """,
    'AuditStart' : """ trigger auditor on start() [Gaudi::Algorithm] """,
    'AuditStop' : """ trigger auditor on stop() [Gaudi::Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Gaudi::Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Gaudi::Algorithm] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Gaudi::Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Gaudi::Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Gaudi::Algorithm] """,
    'Blocking' : """ if algorithm invokes CPU-blocking system calls (offloads computations to accelerators or quantum processors, performs disk or network I/O, is bound by resource synchronization, etc) [Gaudi::Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Gaudi::Algorithm] """,
    'InputCollection6' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::TrackerHitPlaneCollection>,std::tuple<DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection> >,Gaudi::Functional::Traits::use_<> >] """,
    'InputCollection5' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::TrackerHitPlaneCollection>,std::tuple<DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection> >,Gaudi::Functional::Traits::use_<> >] """,
    'InputCollection4' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::TrackerHitPlaneCollection>,std::tuple<DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection> >,Gaudi::Functional::Traits::use_<> >] """,
    'InputCollection3' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::TrackerHitPlaneCollection>,std::tuple<DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection> >,Gaudi::Functional::Traits::use_<> >] """,
    'InputCollection2' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::TrackerHitPlaneCollection>,std::tuple<DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection> >,Gaudi::Functional::Traits::use_<> >] """,
    'InputCollection1' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::TrackerHitPlaneCollection>,std::tuple<DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection> >,Gaudi::Functional::Traits::use_<> >] """,
    'OutputCollection' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::TrackerHitPlaneCollection>,std::tuple<DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection>,DataWrapper<edm4hep::TrackerHitPlaneCollection> >,Gaudi::Functional::Traits::use_<> >] """,
  }
  __declaration_location__ = 'ACTSMergeHitCollections.cxx:6'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(ACTSMergeHitCollections, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'ACTSTrackingPlugins'
  def getType( self ):
      return 'ACTSMergeHitCollections'
  pass # class ACTSMergeHitCollections

class ACTSMergeRelationCollections( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : set(),
    'ExtraOutputs' : set(),
    'OutputLevel' : 0,
    'Enable' : True,
    'ErrorMax' : 1,
    'AuditAlgorithms' : False,
    'AuditInitialize' : False,
    'AuditReinitialize' : False,
    'AuditRestart' : False,
    'AuditExecute' : False,
    'AuditFinalize' : False,
    'AuditStart' : False,
    'AuditStop' : False,
    'Timeline' : True,
    'MonitorService' : 'MonitorSvc',
    'RegisterForContextService' : False,
    'Cardinality' : 0,
    'NeededResources' : [  ],
    'Blocking' : False,
    'FilterCircularDependencies' : True,
    'InputCollection6' : DataHandle('Collection6', 'R', 'DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>'),
    'InputCollection5' : DataHandle('Collection5', 'R', 'DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>'),
    'InputCollection4' : DataHandle('Collection4', 'R', 'DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>'),
    'InputCollection3' : DataHandle('Collection3', 'R', 'DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>'),
    'InputCollection2' : DataHandle('Collection2', 'R', 'DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>'),
    'InputCollection1' : DataHandle('Collection1', 'R', 'DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>'),
    'OutputCollection' : DataHandle('MergedCollection', 'W', 'edm4hep::MCRecoTrackerHitPlaneAssociationCollection'),
  }
  _propertyDocDct = { 
    'ExtraInputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'ExtraOutputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'OutputLevel' : """ output level [Gaudi::Algorithm] """,
    'Enable' : """ should the algorithm be executed or not [Gaudi::Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Gaudi::Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Gaudi::Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Gaudi::Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Gaudi::Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Gaudi::Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Gaudi::Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Gaudi::Algorithm] """,
    'AuditStart' : """ trigger auditor on start() [Gaudi::Algorithm] """,
    'AuditStop' : """ trigger auditor on stop() [Gaudi::Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Gaudi::Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Gaudi::Algorithm] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Gaudi::Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Gaudi::Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Gaudi::Algorithm] """,
    'Blocking' : """ if algorithm invokes CPU-blocking system calls (offloads computations to accelerators or quantum processors, performs disk or network I/O, is bound by resource synchronization, etc) [Gaudi::Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Gaudi::Algorithm] """,
    'InputCollection6' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,std::tuple<DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection> >,Gaudi::Functional::Traits::use_<> >] """,
    'InputCollection5' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,std::tuple<DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection> >,Gaudi::Functional::Traits::use_<> >] """,
    'InputCollection4' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,std::tuple<DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection> >,Gaudi::Functional::Traits::use_<> >] """,
    'InputCollection3' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,std::tuple<DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection> >,Gaudi::Functional::Traits::use_<> >] """,
    'InputCollection2' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,std::tuple<DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection> >,Gaudi::Functional::Traits::use_<> >] """,
    'InputCollection1' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,std::tuple<DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection> >,Gaudi::Functional::Traits::use_<> >] """,
    'OutputCollection' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,std::tuple<DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,DataWrapper<edm4hep::MCRecoTrackerHitPlaneAssociationCollection> >,Gaudi::Functional::Traits::use_<> >] """,
  }
  __declaration_location__ = 'ACTSMergeRelationCollections.cxx:6'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(ACTSMergeRelationCollections, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'ACTSTrackingPlugins'
  def getType( self ):
      return 'ACTSMergeRelationCollections'
  pass # class ACTSMergeRelationCollections

class ACTSSeededCKFTrackingAlg( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : set(),
    'ExtraOutputs' : set(),
    'OutputLevel' : 0,
    'Enable' : True,
    'ErrorMax' : 1,
    'AuditAlgorithms' : False,
    'AuditInitialize' : False,
    'AuditReinitialize' : False,
    'AuditRestart' : False,
    'AuditExecute' : False,
    'AuditFinalize' : False,
    'AuditStart' : False,
    'AuditStop' : False,
    'Timeline' : True,
    'MonitorService' : 'MonitorSvc',
    'RegisterForContextService' : False,
    'Cardinality' : 0,
    'NeededResources' : [  ],
    'Blocking' : False,
    'FilterCircularDependencies' : True,
    'InputTrackerHitCollectionName' : DataHandle('TrackerHits', 'R', 'edm4hep::TrackerHitPlaneCollection'),
    'OutputTrackCollectionName' : DataHandle('Tracks', 'W', 'edm4hep::TrackCollection'),
    'OutputSeedCollectionName' : DataHandle('SeedTracks', 'W', 'edm4hep::TrackCollection'),
    'MatFile' : '',
    'TGeoFile' : '',
    'RunCKF' : True,
    'PropagateBackward' : False,
    'SeedFinding_RMax' : 150.000,
    'SeedFinding_DeltaRMin' : 5.00000,
    'SeedFinding_DeltaRMax' : 80.0000,
    'SeedFinding_DeltaRMinTop' : 0.00000,
    'SeedFinding_DeltaRMaxTop' : 0.00000,
    'SeedFinding_DeltaRMinBottom' : 0.00000,
    'SeedFinding_DeltaRMaxBottom' : 0.00000,
    'SeedFinding_CollisionRegion' : 75.0000,
    'SeedFinding_ZMax' : 600.000,
    'SeedFinding_SigmaScattering' : 50.0000,
    'SeedFinding_RadLengthPerSeed' : 0.100000,
    'SeedFinding_MinPt' : 500.000,
    'SeedFinding_ImpactMax' : 3.00000,
    'SeedFinding_zBinEdges' : [  ],
    'SeedFinding_zTopBinLen' : 1,
    'SeedFinding_zBottomBinLen' : 1,
    'SeedFinding_phiTopBinLen' : 1,
    'SeedFinding_phiBottomBinLen' : 1,
    'InitialTrackError_Pos' : 0.010000000,
    'InitialTrackError_Phi' : 0.017453293,
    'InitialTrackError_RelP' : 0.25000000,
    'InitialTrackError_Lambda' : 0.017453293,
    'InitialTrackError_Time' : 29979.246,
    'CKF_Chi2CutOff' : 15.000000,
    'CKF_NumMeasurementsCutOff' : 10,
    'SeedingLayers' : [  ],
  }
  _propertyDocDct = { 
    'ExtraInputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'ExtraOutputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'OutputLevel' : """ output level [Gaudi::Algorithm] """,
    'Enable' : """ should the algorithm be executed or not [Gaudi::Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Gaudi::Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Gaudi::Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Gaudi::Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Gaudi::Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Gaudi::Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Gaudi::Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Gaudi::Algorithm] """,
    'AuditStart' : """ trigger auditor on start() [Gaudi::Algorithm] """,
    'AuditStop' : """ trigger auditor on stop() [Gaudi::Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Gaudi::Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Gaudi::Algorithm] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Gaudi::Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Gaudi::Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Gaudi::Algorithm] """,
    'Blocking' : """ if algorithm invokes CPU-blocking system calls (offloads computations to accelerators or quantum processors, performs disk or network I/O, is bound by resource synchronization, etc) [Gaudi::Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Gaudi::Algorithm] """,
    'InputTrackerHitCollectionName' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::TrackCollection,edm4hep::TrackCollection>,std::tuple<edm4hep::TrackerHitPlaneCollection>,Gaudi::Functional::Traits::use_<> >] """,
    'OutputTrackCollectionName' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::TrackCollection,edm4hep::TrackCollection>,std::tuple<edm4hep::TrackerHitPlaneCollection>,Gaudi::Functional::Traits::use_<> >] """,
    'OutputSeedCollectionName' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::TrackCollection,edm4hep::TrackCollection>,std::tuple<edm4hep::TrackerHitPlaneCollection>,Gaudi::Functional::Traits::use_<> >] """,
    'MatFile' : """ Path to the material description JSON file. Can be empty. [ACTSAlgBase] """,
    'TGeoFile' : """ Path to the tracker geometry file. [ACTSAlgBase] """,
    'RunCKF' : """ Run tracking using CKF. False means stop at the seeding stage. [ACTSSeededCKFTrackingAlg] """,
    'PropagateBackward' : """ Extrapolates tracks towards beamline. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_RMax' : """ Maximum radius of hits to consider. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_DeltaRMin' : """ Minimum dR between hits in a seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_DeltaRMax' : """ Maximum dR between hits in a seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_DeltaRMinTop' : """ Minimum dR between the reference hit and outer ones in a seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_DeltaRMaxTop' : """ Maximum dR between the reference hit and outer ones in a seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_DeltaRMinBottom' : """ Minimum dR between the reference hit and inner ones in a seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_DeltaRMaxBottom' : """ Maximum dR between the reference hit and inner ones in a seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_CollisionRegion' : """ Size of the collision region in one direction (assumed symmetric). [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_ZMax' : """ Maximum z of hits to consider. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_SigmaScattering' : """ Number of sigmas to allow in scattering angle. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_RadLengthPerSeed' : """ Average radiation length per seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_MinPt' : """ Minimum pT of tracks to seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_ImpactMax' : """ Maximum d0 of tracks to seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_zBinEdges' : """ Bins placement along Z for seeding. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_zTopBinLen' : """ Number of top bins along Z for seeding. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_zBottomBinLen' : """ Number of bottom bins along Z for seeding. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_phiTopBinLen' : """ Number of top bins along phi for seeding. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_phiBottomBinLen' : """ Number of bottom bins along phi for seeding. [ACTSSeededCKFTrackingAlg] """,
    'InitialTrackError_Pos' : """ Track error estimate, local position (mm). [ACTSSeededCKFTrackingAlg] """,
    'InitialTrackError_Phi' : """ Track error estimate, phi (radians). [ACTSSeededCKFTrackingAlg] """,
    'InitialTrackError_RelP' : """ Track error estimate, momentum component (relative). [ACTSSeededCKFTrackingAlg] """,
    'InitialTrackError_Lambda' : """ Track error estimate, lambda (radians). [ACTSSeededCKFTrackingAlg] """,
    'InitialTrackError_Time' : """ Track error estimate, time (sec). [ACTSSeededCKFTrackingAlg] """,
    'CKF_Chi2CutOff' : """ Maximum local chi2 contribution. [ACTSSeededCKFTrackingAlg] """,
    'CKF_NumMeasurementsCutOff' : """ Maximum number of associated measurements on a single surface. [ACTSSeededCKFTrackingAlg] """,
    'SeedingLayers' : """ Layers to use for seeding in vector. [ACTSSeededCKFTrackingAlg] """,
  }
  __declaration_location__ = 'ACTSSeededCKFTrackingAlg.cxx:38'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(ACTSSeededCKFTrackingAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'ACTSTrackingPlugins'
  def getType( self ):
      return 'ACTSSeededCKFTrackingAlg'
  pass # class ACTSSeededCKFTrackingAlg

class TrackTruthAlg( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : set(),
    'ExtraOutputs' : set(),
    'OutputLevel' : 0,
    'Enable' : True,
    'ErrorMax' : 1,
    'AuditAlgorithms' : False,
    'AuditInitialize' : False,
    'AuditReinitialize' : False,
    'AuditRestart' : False,
    'AuditExecute' : False,
    'AuditFinalize' : False,
    'AuditStart' : False,
    'AuditStop' : False,
    'Timeline' : True,
    'MonitorService' : 'MonitorSvc',
    'RegisterForContextService' : False,
    'Cardinality' : 0,
    'NeededResources' : [  ],
    'Blocking' : False,
    'FilterCircularDependencies' : True,
    'InputTrackerHit2SimTrackerHitRelationName' : DataHandle('TrackMCRelation', 'R', 'edm4hep::MCRecoTrackerHitPlaneAssociationCollection'),
    'InputMCParticleCollectionName' : DataHandle('MCParticle', 'R', 'edm4hep::MCParticleCollection'),
    'InputTrackCollectionName' : DataHandle('Tracks', 'R', 'edm4hep::TrackCollection'),
    'OutputParticle2TrackRelationName' : DataHandle('Particle2TrackRelationName', 'W', 'edm4hep::MCRecoTrackParticleAssociationCollection'),
  }
  _propertyDocDct = { 
    'ExtraInputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'ExtraOutputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'OutputLevel' : """ output level [Gaudi::Algorithm] """,
    'Enable' : """ should the algorithm be executed or not [Gaudi::Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Gaudi::Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Gaudi::Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Gaudi::Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Gaudi::Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Gaudi::Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Gaudi::Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Gaudi::Algorithm] """,
    'AuditStart' : """ trigger auditor on start() [Gaudi::Algorithm] """,
    'AuditStop' : """ trigger auditor on stop() [Gaudi::Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Gaudi::Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Gaudi::Algorithm] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Gaudi::Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Gaudi::Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Gaudi::Algorithm] """,
    'Blocking' : """ if algorithm invokes CPU-blocking system calls (offloads computations to accelerators or quantum processors, performs disk or network I/O, is bound by resource synchronization, etc) [Gaudi::Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Gaudi::Algorithm] """,
    'InputTrackerHit2SimTrackerHitRelationName' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::MCRecoTrackParticleAssociationCollection>,std::tuple<edm4hep::TrackCollection,edm4hep::MCParticleCollection,edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,Gaudi::Functional::Traits::use_<> >] """,
    'InputMCParticleCollectionName' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::MCRecoTrackParticleAssociationCollection>,std::tuple<edm4hep::TrackCollection,edm4hep::MCParticleCollection,edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,Gaudi::Functional::Traits::use_<> >] """,
    'InputTrackCollectionName' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::MCRecoTrackParticleAssociationCollection>,std::tuple<edm4hep::TrackCollection,edm4hep::MCParticleCollection,edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,Gaudi::Functional::Traits::use_<> >] """,
    'OutputParticle2TrackRelationName' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<edm4hep::MCRecoTrackParticleAssociationCollection>,std::tuple<edm4hep::TrackCollection,edm4hep::MCParticleCollection,edm4hep::MCRecoTrackerHitPlaneAssociationCollection>,Gaudi::Functional::Traits::use_<> >] """,
  }
  __declaration_location__ = 'TrackTruthAlg.cxx:14'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackTruthAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'ACTSTrackingPlugins'
  def getType( self ):
      return 'TrackTruthAlg'
  pass # class TrackTruthAlg
