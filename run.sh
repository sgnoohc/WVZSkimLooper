#!/bin/bash

# The following is to kill the jobs that are launched when Ctrl-C is pressed instead of running in bkg
trap "kill 0" EXIT

DIR=WVZMVAAllYearSkim4RegionsV2_v0.1.15
SAMPLES="sig wwz wzz zzz zz ttz wz twz higgs othernoh data"

# Create output directory
mkdir -p outputs/

# Launch looper jobs over each sample
for SAMPLE in ${SAMPLES};
do
    rm -f outputs/${SAMPLE}.root
    ./doAnalysis -i ${DIR}/${SAMPLE}.root -t t -o outputs/${SAMPLE}.root > outputs/${SAMPLE}.log 2>&1 &
done

# Aggregate
wait
