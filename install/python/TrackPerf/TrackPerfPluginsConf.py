#Fri Aug  2 14:05:36 2024"""Automatically generated. DO NOT EDIT please"""
import sys
if sys.version_info >= (3,):
    # Python 2 compatibility
    long = int
from GaudiKernel.DataHandle import DataHandle
from GaudiKernel.Proxy.Configurable import *

class TrackPerfHistAlg( ConfigurableAlgorithm ) :
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
    'InputMCTrackRelationCollectionName' : DataHandle('MCTrackRelations', 'R', 'edm4hep::MCRecoTrackParticleAssociationCollection'),
    'InputTrackCollectionName' : DataHandle('Tracks', 'R', 'edm4hep::TrackCollection'),
    'InputMCParticleCollectionName' : DataHandle('MCParticle', 'R', 'DataWrapper<edm4hep::MCParticleCollection>'),
    'MatchProb' : 0.500000,
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
    'InputMCTrackRelationCollectionName' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<>,std::tuple<DataWrapper<edm4hep::MCParticleCollection>,edm4hep::TrackCollection,edm4hep::MCRecoTrackParticleAssociationCollection>,Gaudi::Functional::Traits::use_<> >] """,
    'InputTrackCollectionName' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<>,std::tuple<DataWrapper<edm4hep::MCParticleCollection>,edm4hep::TrackCollection,edm4hep::MCRecoTrackParticleAssociationCollection>,Gaudi::Functional::Traits::use_<> >] """,
    'InputMCParticleCollectionName' : """  [Gaudi::Functional::details::DataHandleMixin<std::tuple<>,std::tuple<DataWrapper<edm4hep::MCParticleCollection>,edm4hep::TrackCollection,edm4hep::MCRecoTrackParticleAssociationCollection>,Gaudi::Functional::Traits::use_<> >] """,
    'MatchProb' : """ Minimum matching probability to be considered a good track-MC match. [TrackPerfHistAlg] """,
  }
  __declaration_location__ = 'TrackPerfHistAlg.cxx:11'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackPerfHistAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackPerfPlugins'
  def getType( self ):
      return 'TrackPerfHistAlg'
  pass # class TrackPerfHistAlg
