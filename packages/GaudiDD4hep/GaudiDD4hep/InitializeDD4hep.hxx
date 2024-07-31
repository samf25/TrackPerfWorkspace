#ifndef InitializeDD4hep_h
#define InitializeDD4hep_h 1

#include <Gaudi/Algorithm.h>

#include <string>

/** InitializeDD4hep: initializes a DD4hep detector geometry from a compact XML file.
 *  Call as first algorithm in your steering file.
 *  Algorithms access the geometry simply via: 
 *  <p>
 *    DD4hep::Geometry::LCDD& lcdd = DD4hep::Geometry::LCDD::getInstance(); 
 *  </p>
 * 
 *  @param DD4hepXMLFile Name of the DD4hep compact XML file to load
 * 
 *  @author F. Gaede, CERN/DESY (adapted by Samuel Ferraro)
 *  @version $Id:$
 */

class InitializeDD4hep : public Gaudi::Algorithm {
public:
	InitializeDD4hep(const std::string& name, ISvcLocator* svcLoc);
	
	/** Initiallize the DD4hep geometry
 	*/
	StatusCode initialize();
	
	/// Do nothing
	StatusCode execute(const EventContext&) const;

	/** Deconstruct Instance
 	*/
	StatusCode finalize();

protected:

	/// path to dd4hep compact detector xml file
	Gaudi::Property<std::string> m_dd4hepFileName{this, "DD4hepXMLFile", std::string("dd4hep_compact.xml"), "Name of the DD4hep compact xml file to load"};
	
	/// name of lcdd parameter for encoding string
	Gaudi::Property<std::string> m_encodingString{this, "EncodingString", std::string(""), "Compact File parameter of encoding string for LCTrackerCellID. While this will not be used later, make sure this is the encoding string passed into reconstruction."};

};
#endif
