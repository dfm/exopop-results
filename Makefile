collect:
	cp ../exopop/data/completeness.h5 .
	mkdir -p real
	cp ../exopop/code/results/samples.h5 real
	mkdir -p simulated
	mkdir -p simulated/catalog-a
	cp ../exopop/document/code/smooth/samples.h5 simulated/catalog-a
	mkdir -p simulated/catalog-b
	cp ../exopop/document/code/simulation/samples.h5 simulated/catalog-b

.PHONY: collect
