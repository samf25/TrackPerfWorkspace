# TrackPerf Workspace

Collection of packages for testing tracking performance in a muon collider.

## Repository Structure
- `exts/` External packages not included with the ILC framework.
- `packages/` All non-standard packages linked using git submodules.
- `sim/` Configuration files for generating events.

## Setup Instructions

### Container
All commands should be run inside the `gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:2.8-patch2-el9` image.

#### Singularity

```bash
apptainer shell --cleanenv -B/disk/moose docker://gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:2.8-patch2-el9
```

#### Shifter

```bash
shifter --image gitlab-registry.cern.ch/muon-collider/mucoll-deploy/mucoll:2.8-patch2-el9 /bin/bash
```

### Build Instructions
Run the following commands from inside your container. The same commands will also work with a local installation of the ILC software, with the exception of the first line.

```bash
source /opt/setup_mucoll.sh # Setup ILC software
cmake -S . -B build 
cmake --build build
```

### Setup Script
The included `setup.sh` script is useful for defining all paths for the binaries built by the workspace. At the current stage, it setups the following:
- ILC software via `setup_mucoll.sh`
- External binaries/libraries found in `exts`.
- Add all package libraries to `MARLIN_DLL`.
- Export `MYBUILD` variable with absolute path the build directory.
- Export `MYWORKSPACE` variable with absolute path the workspace directory.

Run the following at the start of every session. It has an optional argument to the build directory and is set to `build/` by default.

```bash
source setup.sh [build]
```

## Example Commands

Run the following commands from your run directory.

The CKF tracking example (triplet seeds).

```bash
Marlin ${MYWORKSPACE}/example/actsseedckf_steer.xml --InitDD4hep.DD4hepXMLFile=${MUCOLL_GEO} --global.LCIOInputFiles=/cvmfs/muoncollider.cern.ch/datasets/tutorial_20230705/sim_Hbb/output_sim.slcio
```
