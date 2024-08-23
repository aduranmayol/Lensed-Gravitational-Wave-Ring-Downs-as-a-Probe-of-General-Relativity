#!/usr/bin/bash

pycbc_create_injections --verbose \
                        --config-files /project/gravwav/admayol/master_project/lensed/run_50/injection_50event_1.ini \
                        --ninjections 1 \
                        --seed 10 \
                        --output-file /project/gravwav/admayol/master_project/lensed/run_50/injection_50event_1.hdf \
                        --variable-params-section variable_params \
                        --static-params-section static_params \
                        --dist-section prior \
                        --force