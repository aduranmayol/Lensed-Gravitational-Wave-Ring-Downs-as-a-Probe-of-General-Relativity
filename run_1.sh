#!/bin/sh
export PYCBC_DETECTOR_CONFIG=/project/gravwav/admayol/master_project/ce.ini

PRIOR_CONFIG=/project/gravwav/admayol/master_project/lensed/run_1/inference_1.ini 
#DATA_CONFIG=data.ini
#SAMPLER_CONFIG=injection.ini

OUTPUT_PATH=/data/gravwav/admayol/lensed/inference1.hdf 

# the following sets the number of cores to use; adjust as needed to
# your computer's capabilities
NPROCS=16 
# run sampler
# Running with OMP_NUM_THREADS=1 stops lalsimulation
# from spawning multiple jobs that would otherwise be used
# by pycbc_inference and cause a reduced runtime.
OMP_NUM_THREADS=1 \
pycbc_inference --verbose \
    --seed 1897234 \
    --config-file ${PRIOR_CONFIG} \
    --output-file ${OUTPUT_PATH} \
    --nprocesses ${NPROCS} \
    --force
