#include "InitializeDD4hep.hxx"

#include <DD4hep/Printout.h>
#include <DD4hep/Detector.h>

DECLARE_COMPONENT(InitializeDD4hep)

InitializeDD4hep::InitializeDD4hep(const std::string& name, ISvcLocator* svcLoc) : Gaudi::Algorithm(name, svcLoc) {}

StatusCode InitializeDD4hep::initialize() {
	dd4hep::setPrintLevel(dd4hep::WARNING);

	MsgStream log(msgSvc(), name());
        log << MSG::INFO << " -------------------------------------" << std::endl
			 << " ---- Initializing DD4hep from file  " << m_dd4hepFileName << " ... " << endmsg;
	
	dd4hep::Detector& theDetector = dd4hep::Detector::getInstance();
	theDetector.fromCompact( m_dd4hepFileName );

	log << MSG::INFO << " ---- instantiated  geometry for detector " << theDetector.header().name()  << std::endl
			 << " -------------------------------------" << endmsg;

	log << MSG::INFO << "Encoding String should be set to:" << std::endl
			 << theDetector.constantAsString( m_encodingString ) << std::endl
			 << "Which was specified in the lccd parameter: " << m_encodingString << std::endl 
			 << "--------------------------------------" << endmsg;
	
	return StatusCode::SUCCESS;
}

StatusCode InitializeDD4hep::execute(const EventContext&) const{ return StatusCode::SUCCESS; }

StatusCode InitializeDD4hep::finalize() {
	dd4hep::Detector::getInstance().destroyInstance();
	return StatusCode::SUCCESS;
}


