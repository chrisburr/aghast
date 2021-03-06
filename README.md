![](https://github.com/diana-hep/aghast/raw/master/docs/source/logo-300px.png)

# aghast

[![Build Status](https://travis-ci.org/diana-hep/aghast.svg?branch=master)](https://travis-ci.org/diana-hep/aghast) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/diana-hep/aghast/master?urlpath=lab/tree/binder%2Fexamples.ipynb)

Aghast is a histogramming library that does not fill histograms and does not plot them. Its role is behind the scenes, to provide better communication between histogramming libraries.

Specifically, it is a structured representation of **ag**gregated, **h**istogram-like **st**atistics as sharable "ghasts." It has all of the "bells and whistles" often associated with plain histograms, such as number of entries, unbinned mean and standard deviation, bin errors, associated fit functions, profile plots, and even simple ntuples (needed for unbinned fits or machine learning applications). [ROOT](https://root.cern.ch/root/htmldoc/guides/users-guide/Histograms.html) has all of these features; [Numpy](https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html) has none of them.

The purpose of aghast is to be an intermediate when converting ROOT histograms into Numpy, or vice-versa, or both of these into [Boost.Histogram](https://github.com/boostorg/histogram), [Physt](https://physt.readthedocs.io/en/latest/index.html), [Pandas](https://pandas.pydata.org), etc. Without an intermediate representation, converting between _N_ libraries (to get the advantages of all) would equire _N(N  ‒ 1)/2_ conversion routines; with an intermediate representation, we only need _N_, and the mapping of feature to feature can be made explicit in terms of a common language.

Furthermore, aghast is a [Flatbuffers](http://google.github.io/flatbuffers/) schema, so it can be deciphered in [many languages](https://google.github.io/flatbuffers/flatbuffers_support.html), with [lazy, random-access](https://github.com/mzaks/FlatBuffersSwift/wiki/FlatBuffers-Explained), and uses a [small amount of memory](http://google.github.io/flatbuffers/md__benchmarks.html). A collection of histograms, functions, and ntuples can be shared among processes as shared memory, used in remote procedure calls, processed incrementally in a memory-mapped file, or saved in files with future-proof [schema evolution](https://google.github.io/flatbuffers/md__schemas.html).

## Installation from packages

Install aghast like any other Python package:

```bash
pip install uproot                        # maybe with sudo or --user, or in virtualenv
```

<!-- or install with [conda](https://conda.io/en/latest/miniconda.html): -->

<!-- ```bash -->
<!-- conda config --add channels conda-forge   # if you haven't added conda-forge already -->
<!-- conda install uproot -->
<!-- ``` -->

_(Not on conda yet.)_

## Manual installation

After you git-clone this GitHub repository and ensure that `numpy` is installed, somehow:

```bash
pip install "flatbuffers>=1.8.0"          # for the flatbuffers runtime (with Numpy)
cd python                                 # only implementation so far is in Python
python setup.py install                   # to use it outside of this directory
```

Now you should be able to `import aghast` or `from aghast import *` in Python.

If you need to change `flatbuffers/aghast.fbs`, you'll need to additionally:

   1. Get `flatc` to generate Python sources from `flatbuffers/aghast.fbs`. I use `conda install -c conda-forge flatbuffers`. (The `flatc` executable is _not_ included in the pip `flatbuffers` package, and the Python runtime is _not_ included in the conda `flatbuffers` package. They're disjoint.)
   2. In the `python` directory, run `./generate_flatbuffers.py` (which calls `flatc` and does some post-processing).

Every time you change `flatbuffers/aghast.fbs`, re-run `./generate_flatbuffers.py`.

## Documentation

Suite of examples as a Jupyter notebook:

   * [in GitHub](https://github.com/diana-hep/aghast/blob/master/binder/examples.ipynb)
   * [on Binder](https://mybinder.org/v2/gh/diana-hep/aghast/master?urlpath=lab/tree/binder%2Fexamples.ipynb)

Full specification:

   * [Introduction](https://github.com/diana-hep/aghast/blob/master/specification.adoc#introduction)
   * [Data types](https://github.com/diana-hep/aghast/blob/master/specification.adoc#data-types)
      * [Collection](https://github.com/diana-hep/aghast/blob/master/specification.adoc#collection)
      * [Histogram](https://github.com/diana-hep/aghast/blob/master/specification.adoc#histogram)
      * [Axis](https://github.com/diana-hep/aghast/blob/master/specification.adoc#axis)
      * [IntegerBinning](https://github.com/diana-hep/aghast/blob/master/specification.adoc#integerbinning)
      * [RegularBinning](https://github.com/diana-hep/aghast/blob/master/specification.adoc#regularbinning)
      * [RealInterval](https://github.com/diana-hep/aghast/blob/master/specification.adoc#realinterval)
      * [RealOverflow](https://github.com/diana-hep/aghast/blob/master/specification.adoc#realoverflow)
      * [HexagonalBinning](https://github.com/diana-hep/aghast/blob/master/specification.adoc#hexagonalbinning)
      * [EdgesBinning](https://github.com/diana-hep/aghast/blob/master/specification.adoc#edgesbinning)
      * [IrregularBinning](https://github.com/diana-hep/aghast/blob/master/specification.adoc#irregularbinning)
      * [CategoryBinning](https://github.com/diana-hep/aghast/blob/master/specification.adoc#categorybinning)
      * [SparseRegularBinning](https://github.com/diana-hep/aghast/blob/master/specification.adoc#sparseregularbinning)
      * [FractionBinning](https://github.com/diana-hep/aghast/blob/master/specification.adoc#fractionbinning)
      * [PredicateBinning](https://github.com/diana-hep/aghast/blob/master/specification.adoc#predicatebinning)
      * [VariationBinning](https://github.com/diana-hep/aghast/blob/master/specification.adoc#variationbinning)
      * [Variation](https://github.com/diana-hep/aghast/blob/master/specification.adoc#variation)
      * [Assignment](https://github.com/diana-hep/aghast/blob/master/specification.adoc#assignment)
      * [UnweightedCounts](https://github.com/diana-hep/aghast/blob/master/specification.adoc#unweightedcounts)
      * [WeightedCounts](https://github.com/diana-hep/aghast/blob/master/specification.adoc#weightedcounts)
      * [InterpretedInlineBuffer](https://github.com/diana-hep/aghast/blob/master/specification.adoc#interpretedinlinebuffer)
      * [InterpretedInlineInt64Buffer](https://github.com/diana-hep/aghast/blob/master/specification.adoc#interpretedinlineint64buffer)
      * [InterpretedInlineFloat64Buffer](https://github.com/diana-hep/aghast/blob/master/specification.adoc#interpretedinlinefloat64buffer)
      * [InterpretedExternalBuffer](https://github.com/diana-hep/aghast/blob/master/specification.adoc#interpretedexternalbuffer)
      * [Profile](https://github.com/diana-hep/aghast/blob/master/specification.adoc#profile)
      * [Statistics](https://github.com/diana-hep/aghast/blob/master/specification.adoc#statistics)
      * [Moments](https://github.com/diana-hep/aghast/blob/master/specification.adoc#moments)
      * [Quantiles](https://github.com/diana-hep/aghast/blob/master/specification.adoc#quantiles)
      * [Modes](https://github.com/diana-hep/aghast/blob/master/specification.adoc#modes)
      * [Extremes](https://github.com/diana-hep/aghast/blob/master/specification.adoc#extremes)
      * [StatisticFilter](https://github.com/diana-hep/aghast/blob/master/specification.adoc#statisticfilter)
      * [Covariance](https://github.com/diana-hep/aghast/blob/master/specification.adoc#covariance)
      * [ParameterizedFunction](https://github.com/diana-hep/aghast/blob/master/specification.adoc#parameterizedfunction)
      * [Parameter](https://github.com/diana-hep/aghast/blob/master/specification.adoc#parameter)
      * [EvaluatedFunction](https://github.com/diana-hep/aghast/blob/master/specification.adoc#evaluatedfunction)
      * [BinnedEvaluatedFunction](https://github.com/diana-hep/aghast/blob/master/specification.adoc#binnedevaluatedfunction)
      * [Ntuple](https://github.com/diana-hep/aghast/blob/master/specification.adoc#ntuple)
      * [Column](https://github.com/diana-hep/aghast/blob/master/specification.adoc#column)
      * [NtupleInstance](https://github.com/diana-hep/aghast/blob/master/specification.adoc#ntupleinstance)
      * [Chunk](https://github.com/diana-hep/aghast/blob/master/specification.adoc#chunk)
      * [ColumnChunk](https://github.com/diana-hep/aghast/blob/master/specification.adoc#columnchunk)
      * [Page](https://github.com/diana-hep/aghast/blob/master/specification.adoc#page)
      * [RawInlineBuffer](https://github.com/diana-hep/aghast/blob/master/specification.adoc#rawinlinebuffer)
      * [RawExternalBuffer](https://github.com/diana-hep/aghast/blob/master/specification.adoc#rawexternalbuffer)
      * [Metadata](https://github.com/diana-hep/aghast/blob/master/specification.adoc#metadata)
      * [Decoration](https://github.com/diana-hep/aghast/blob/master/specification.adoc#decoration)
